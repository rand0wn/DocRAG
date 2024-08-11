# DocRAG System

This is a Streamlit app that allows users to upload files and query a knowledge base using a Retrieve and Generate (RAG) methodology.

## Running the Application

### Prerequisites

- Docker and Docker Compose installed on your machine.

### Installation and Running

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/rand0wn/DocRAG.git
   cd DocRAG
   ```

2. **Build and Start the Docker Containers:**

   ```bash
   docker-compose up --build
   ```

3. **Access the App:**

   Open a web browser and go to `http://localhost:8501` to interact with the application.

### Usage

1. **Upload Files:**
   - Use the file uploader to upload multiple files (e.g., txt, pdf, docx) to the knowledge base directory.

2. **Enter Queries:**
   - Type your query in the input field and click "Submit" to get responses based on the uploaded files.