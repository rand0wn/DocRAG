import streamlit as st
from crewai_tools import DirectorySearchTool
from crewai import Agent, Task, Crew
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Directory to save uploaded files
UPLOAD_DIR = 'kb/'
os.makedirs(UPLOAD_DIR, exist_ok=True)

# For fixed directory searches
kb_tool = DirectorySearchTool(directory=UPLOAD_DIR)

# Create agents
researcher = Agent(
    role='Document Analyst',
    goal='Provide information from knowledge base',
    backstory='An expert analyst with a knowledge obtained from knowledge base.',
    tools=[kb_tool],
    verbose=True
)

# Define tasks
research = Task(
    description=("Analyse the following user query from context of Knowledge Base: {user_query}. "
                 "Do not assume anything only rely on context from knowledge base."
                 "Answer in one line and be very specific and to the point."),
    expected_output='Output of user query in text derived from knowledge base',
    agent=researcher
)

# Assemble a crew
run_crew = Crew(
    agents=[researcher],
    tasks=[research],
    verbose=True
)

# Streamlit app
st.title('Query Answering System')

# File uploader
st.subheader('Upload Files')
uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True, type=['txt', 'pdf', 'docx'])

if uploaded_files:
    for uploaded_file in uploaded_files:
        # Save each uploaded file
        file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())
        st.write(f"Saved file: {uploaded_file.name}")

# Input field for user query
user_query = st.text_input("Enter your query:")

if st.button("Submit"):
    if user_query:
        # Run the crew to get the response
        reply = run_crew.kickoff_for_each(inputs=[{"user_query": user_query}])
        st.write(f"Response: {reply[0]}")
    else:
        st.write("Please enter a query.")
