# Summarization & More

This project is a text summarization tool with additional features, utilizing Natural Language Processing (NLP) libraries in Python to perform various text-related tasks. It can extract data from a given URL and process it to provide useful insights. The frontend is built with React to offer a well-designed, dynamic user interface.

## Features

- **Summarization**: Generate concise summaries from larger text inputs.
- **Keywords Extraction**: Identify and extract key terms from the text.
- **Sentiment Analysis**: Analyze the sentiment of the text to determine its tone.
- **Well-Designed Dynamic UI**: Interactive and user-friendly interface built with React.

## Project Structure

- `app.py`: Main backend application file.
- `summary_maker.py`: Contains the summarization logic.
- `frontend/`: Contains the React frontend code.
  - `public/`: Contains static files.
  - `src/`: Contains the source code for the React application.
    - `app.js`
    - `footer.jsx`
    - `index.js`
    - `main.jsx`
  - `package.json`: Contains the list of dependencies and scripts for the frontend.

## Installation

### Prerequisites

- Python 3.x
- Node.js and npm (for React)
- Git

### Backend Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/summarization-and-more.git
    cd summarization-and-more
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Backend**:
    ```bash
    python app.py
    ```

### Frontend Setup

1. **Navigate to the Frontend Directory**:
    ```bash
    cd frontend
    ```

2. **Install Dependencies**:
    ```bash
    npm install
    ```

3. **Run the Frontend**:
    ```bash
    npm start
    ```

## Usage

1. Ensure the backend is running:
    ```bash
    python app.py
    ```
2. In a new terminal, navigate to the `frontend` directory and start the frontend:
    ```bash
    cd frontend
    npm start
    ```
3. Open your browser and go to `http://localhost:3000` to access the application.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
