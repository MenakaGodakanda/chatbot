# GenAI Chatbot Project
This project demonstrates a Generative AI (GenAI)-based chatbot built using open-source tools. The chatbot uses a pre-trained model from the Hugging Face Transformers library to generate responses to user inputs. A Flask web application provides the interface for user interaction, and the project is designed to run on Ubuntu 22.04.

## Overview
<img width="1336" alt="Screenshot 2025-01-29 at 3 01 21 pm" src="https://github.com/user-attachments/assets/5e87257a-afca-41f4-9db3-7ca8790feee3" />

### Explanation:
#### 1. User Input (Frontend UI - `index.html`)
- User enters a message in the chatbox.
#### 2. Flask Web App (`app.py`)
- Handles user request and routes it to chatbot logic.
#### 3. Chatbot Logic (`chatbot_logic.py`)
- Loads AI model and processes user input.
#### 4. AI Model (GPT-2 from `transformers`)
- Generates a response using a pre-trained transformer model.
#### 5. Response Sent Back to Flask
- Flask sends the chatbot’s response back to the user interface.
#### 6. User Receives Response
- The response is displayed dynamically in the chatbox.

## Features

- Generative AI-powered chatbot using a pre-trained GPT-like model.
- Flask-based web interface for real-time interaction.
- Simple and clean frontend with dynamic updates.
- Built with open-source tools, no hardware dependencies.

## Prerequisites

Ensure your system meets the following requirements:
- **Ubuntu 22.04**
- **Python 3.8+**
- **Pip** (Python package installer)
- **Virtualenv** (optional but recommended for isolated environments)

## Setup Instructions

### 1. Clone the Repository
```
git clone https://github.com/MenakaGodakanda/chatbot.git
cd chatbot
```

### 2. Create a Virtual Environment (Optional)
- Install virtualenv for isolated Python environments:
```
sudo apt install python3-virtualenv
```
![Screenshot 2025-01-13 044202](https://github.com/user-attachments/assets/d950a20e-640c-40b8-b076-5f0c3d740199)

- Create a virtual environment:
```
virtualenv chatbot_env
source chatbot_env/bin/activate
```

### 3. Install Dependencies

Install the required Python libraries:
```
pip install torch transformers flask
```

### 4. Run the Application

Start the Flask web application:
```
python app.py
```
![Screenshot 2025-01-13 044739](https://github.com/user-attachments/assets/1bd8246c-04e8-45eb-87ab-07639e7bd14f)


### 5. Access the Chatbot

Open your browser and navigate to:
```
http://127.0.0.1:5000
```

### Example Interaction

- User Input:
```
Hello, chatbot!
```
- Bot Response:
![Screenshot 2025-01-13 044659](https://github.com/user-attachments/assets/24471ba6-e03d-45e0-848b-7954d2427cd2)

- User Input:
```
What is AI?
```
- Bot Response:
![Screenshot 2025-01-13 044733](https://github.com/user-attachments/assets/99a596e3-2037-4db3-9ac9-289940a0d948)

- User Input:
```
Tell me a joke.
```
- Bot Response:
![Screenshot 2025-01-13 044810](https://github.com/user-attachments/assets/ee52d9b7-6760-4d1a-8011-7fe34e2aa416)


### Chat Flow:

- User types a message into the input box.
- The chatbot generates a response using the AI model.
- Both the user's message and the bot's response are displayed in the chatbox.


## Project Structure
```
chatbot/
|
├── app.py               # Main application code
├── chatbot_logic.py     # Chatbot response generation logic
├── templates/
|   └── index.html       # Frontend interface
└── static/
    └── style.css        # CSS styles for the interface
```

### File Descriptions
- `app.py`: Initializes the Flask app, sets up routes, and integrates the chatbot logic.
- `chatbot_logic.py`: Loads the pre-trained GPT-like model and generates responses.
- `templates/index.html`: Defines the frontend structure of the chatbot interface.
- `static/style.css`: Provides styling for the chatbot interface.

### Dependencies
The project relies on the following Python libraries:
- `torch`: For running the GPT model.
- `transformers`: To load and use the pre-trained model.
- `flask`: For creating the web interface.


## Troubleshooting

### Common Issues:

1. `ModuleNotFoundError`:
- Ensure the file structure matches the provided layout.
- Check the import statement in `app.py`: `from chatbot_logic import Chatbot` (do not include `.py` in imports).

2. `Flask app not running`:
- Ensure you are in the correct virtual environment (if created).
- Run `python app.py` from the project directory.

3. `Model download issues`:
- Verify your internet connection.
- Manually download the model by running:
```
from transformers import AutoModelForCausalLM, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")
```

## License

This project is licensed under the MIT License.
