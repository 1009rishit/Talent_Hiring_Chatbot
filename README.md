TalentScout AI Hiring Assistant

📌 Project Overview

TalentScout AI Hiring Assistant is an intelligent chatbot designed to streamline the candidate screening process for a fictional recruitment agency. Built using Gradio, LangChain, and Groq's Llama-3.3-70B, this chatbot collects essential candidate information and generates tailored technical interview questions based on their declared tech stack.

🚀 Features

Candidate Information Collection: Gathers details such as name, email, phone number, experience, desired role, location, and tech stack.

Dynamic Technical Question Generation: Uses AI to create 3-5 interview questions tailored to the candidate’s expertise.

Context-Aware Conversation Handling: Stores chat history using LangChain's ConversationBufferMemory.

Exit & Fallback Mechanisms: Recognizes exit keywords (bye, exit, quit) and provides meaningful fallback responses.

User-Friendly Interface: Built with Gradio for an intuitive chat-based UI.

🛠️ Tech Stack

Python - Primary programming language.

Gradio - UI for chatbot interaction.

LangChain - Manages prompts and conversation history.

Groq’s Llama-3.3-70B - LLM used for generating responses.

⚙️ Installation & Setup

Prerequisites

Ensure you have Python installed (version 3.8+ recommended). Install dependencies using:

pip install gradio langchain langchain_groq

Running the Application

Clone this repository:

git clone https://github.com/your-repo/talentscout-hiring-assistant.git
cd talentscout-hiring-assistant

Replace the api_key in the script with a valid Groq API key.

Run the chatbot:

python app.py

Open the Gradio UI link provided in the terminal.

🖥️ How It Works

The chatbot greets the candidate and requests their details.

Once the candidate declares their tech stack, the chatbot generates technical interview questions.

Candidates can interact with the chatbot for follow-up discussions.

The conversation can be exited using keywords like bye, exit, quit.

📂 Project Structure

├── app.py               # Main chatbot script
├── requirements.txt     # List of dependencies
├── README.md            # Project documentation
└── .gitignore           # Ignore unnecessary files

🔍 Prompt Engineering Strategy

Candidate Info Gathering: Prompt ensures all key details are collected systematically.

Tech-Specific Question Generation: AI generates relevant questions based on the provided tech stack.

Context Retention: Memory storage keeps track of candidate responses to ensure smooth interaction.

Fallback Handling: Provides meaningful responses when an unknown input is received.

🚀 Future Enhancements

Sentiment Analysis to gauge candidate confidence levels.

Multilingual Support for broader accessibility.

Cloud Deployment on AWS/GCP for scalability.

📜 License

This project is open-source. Feel free to modify and expand upon it!



