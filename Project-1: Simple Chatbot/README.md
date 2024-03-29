# Chatbot using Gradio

This is a simple chatbot implementation using Gradio and the Generative Language API.

## Prerequisites

- Python 3.x
- Required Python libraries: `gradio`, `requests`

## Obtaining API Key

To use this chatbot, you need to obtain an API key from Google's Generative Language API. Follow these steps:

1. Visit the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project (or select an existing one).
3. Enable the "Generative Language" API for your project.
4. Create API credentials and obtain your API key.
- P.S: If you have an existing project in your Cloud Console, get it from [here](https://ai.google.dev/).

## Usage

1. Open a terminal and navigate to the directory containing `chatbot.py`.

2. Run the chatbot script:

   ```bash
   python chatbot.py
   ```

3. Access the chatbot interface in your web browser by visiting [http://localhost:7860](http://localhost:7860).

4. Enter text in the input box, and the chatbot will generate responses based on the conversation history.

5. To exit the chatbot, press `Ctrl+C` in the terminal where the script is running.

## Disclaimer
The generated output may not be accurate or precise. It is a machine-generated response and should be used at the user's discretion. The developer is not responsible for any inaccuracies or misuse of the information provided by the chatbot. Use the output safely and verify critical information from official sources.
