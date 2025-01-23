# Financial QA Bot

This project is a **Financial Question-Answering (QA) Bot** designed to extract, store, and retrieve financial data from PDFs. It uses a **Retrieval-Augmented Generation (RAG)** pipeline to provide accurate and context-aware answers to user queries.

## Features
- Extracts financial data (e.g., P&L statements) from PDFs.
- Stores data embeddings using FAISS for efficient retrieval.
- Generates responses using a generative language model.
- Interactive interface built with Streamlit.
- Fully functional Colab notebook for experimentation.

---

## Setup Instructions

### Prerequisites
1. **Docker**: Install Docker Desktop from [Docker's website](https://www.docker.com/products/docker-desktop).
2. **Python**: Ensure Python 3.9+ is installed for local testing.
3. **Google Colab**: For running the notebook.

---

### Run Locally Using Docker
1. Clone the repository:
   ```bash
   git clone https://github.com/nsain25/financial-qa-bot.git
   cd financial-qa-bot
   ```

2. Build the Docker image:
   ```bash
   docker build -t financial-qa-bot .
   ```

3. Run the Docker container:
   ```bash
   docker run -p 8501:8501 financial-qa-bot
   ```

4. Open your browser and navigate to:
   ```
   http://localhost:8501
   ```

---

### Run in Colab
1. Open the Colab notebook: [Financial QA Bot Colab Notebook](https://colab.research.google.com/your-notebook-link).
2. Upload a sample financial PDF.
3. Run the cells to extract data, query, and generate responses.

---

## Usage Instructions

### Streamlit Interface
1. Upload a financial PDF.
2. Enter a query (e.g., "What is the revenue for Q3?").
3. View the retrieved data and generated response.

### Colab Notebook
1. Extract and parse financial data from PDFs.
2. Store embeddings in FAISS.
3. Query the data interactively.

---

## Approach

1. **PDF Parsing**:
   - Extract text from PDFs using PyPDF2.
   - Parse financial data (e.g., revenue, expenses, profit) into a structured DataFrame.

2. **Retrieval**:
   - Generate embeddings using Sentence Transformers.
   - Store embeddings in FAISS for efficient similarity search.

3. **Response Generation**:
   - Use a generative model (e.g., GPT-2) to generate contextual answers.

4. **Interactive Interface**:
   - Built with Streamlit for uploading PDFs and querying data.

---

## Example Queries and Outputs

| **Query**                       | **Retrieved Data**                         | **Generated Response**                   |
|----------------------------------|--------------------------------------------|------------------------------------------|
| What is the revenue for Q3?      | Revenue Q1: 100, Q2: 200, Q3: 300...       | The revenue for Q3 is 300.               |
| What was the total profit in Q4? | Profit Q1: 50, Q2: 100, Q3: 150, Q4: 200...| The total profit in Q4 was 200.          |

---

## File Structure
```
financial-qa-bot/
│
├── app.py                # Streamlit app code
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker build instructions
├── colab_notebook.ipynb  # Fully functional Colab notebook
└── README.md             # Documentation
```

---

## Contributions
Feel free to fork this repository and submit pull requests for improvements.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

