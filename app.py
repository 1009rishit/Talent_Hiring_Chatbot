import gradio as gr
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory

# Initialize LLM and memory
llm = ChatGroq(
    temperature=0.7,
    model="llama-3.3-70b-versatile",
    api_key="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"  # Replace with actual API key
)
memory = ConversationBufferMemory(memory_key="chat_history")

# Conversation Handling
def generate_questions(tech_stack):
    """Generate technical questions based on the declared tech stack."""
    prompt = f"Generate 3-5 interview questions for a candidate skilled in {tech_stack}."
    response = llm.invoke(prompt)
    return response.content

def handle_response(user_input, candidate_info):
    # Check for exit commands
    if user_input.lower() in ["bye", "exit", "quit", "stop"]:
        return "Thank you for your time! A recruiter will contact you soon."
    
    # Generate technical questions based on tech stack
    if candidate_info.get("tech_stack"):
        questions = generate_questions(candidate_info["tech_stack"])
        return f"Here are your technical questions based on your tech stack:\n{questions}"
    
    # Continue conversation
    response = llm.invoke(
        f"Continue technical screening interview. Last response: {user_input}"
    )
    return response.content

# Gradio Interface
def chat_interface(message, chat_history, full_name, email, phone, years_experience, desired_position, location, tech_stack):
    candidate_info = {
        "full_name": full_name,
        "email": email,
        "phone": phone,
        "years_experience": years_experience,
        "desired_position": desired_position,
        "location": location,
        "tech_stack": tech_stack,
    }
    
    bot_response = handle_response(message, candidate_info)
    chat_history.append((message, bot_response))
    return "", chat_history

with gr.Blocks(title="TalentScout Hiring Assistant", theme=gr.themes.Soft()) as demo:
    gr.Markdown("## 🧑‍💼 TalentScout AI Hiring Assistant")
    
    full_name = gr.Textbox(label="Full Name", placeholder="Enter your full name")
    email = gr.Textbox(label="Email Address", placeholder="Enter your email")
    phone = gr.Textbox(label="Phone Number", placeholder="Enter your phone number")
    years_experience = gr.Number(label="Years of Experience", minimum=0, maximum=50)
    desired_position = gr.Textbox(label="Desired Position", placeholder="Enter your desired position")
    location = gr.Textbox(label="Current Location", placeholder="Enter your location")
    tech_stack = gr.Textbox(label="Tech Stack", placeholder="Enter your tech skills (e.g., Python, Django, React)")
    
    chatbot = gr.Chatbot(height=500)
    message = gr.Textbox(label="Your Message", placeholder="Type here...")
    
    clear_btn = gr.ClearButton([message, chatbot, full_name, email, phone, years_experience, desired_position, location, tech_stack])
    
    message.submit(
        chat_interface,
        [message, chatbot, full_name, email, phone, years_experience, desired_position, location, tech_stack],
        [message, chatbot]
    )

demo.launch(share=True)
