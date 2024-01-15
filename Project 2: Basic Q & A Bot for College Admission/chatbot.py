import gradio as gr
import requests
import json
from googlesearch import search

class AdmissionChatbot:
    def __init__(self, api_key):
        self.api_key = api_key
        self.user_info = {}

    def generate_content(self, prompt):
        headers = {'Content-Type': 'application/json'}
        data = {
            "contents": [
                {"parts": [{"text": prompt}]}
            ]
        }
        params = {'key': self.api_key}

        response = requests.post(api_url, headers=headers, data=json.dumps(data), params=params)

        if response.status_code == 200:
            try:
                candidates = response.json().get('candidates', [])
                if candidates:
                    content = candidates[0].get('content', {}).get('parts', [])[0].get('text', '')
                    return content
                else:
                    return f"Error: 'candidates' not found in response"
            except (IndexError, KeyError):
                return f"Error: Unexpected response structure - {response.json()}"
        else:
            return f"Error: {response.status_code}, {response.text}"

    def process_query(self, query):
        search_results = list(search(query, num=3, stop=3, pause=2))
        if search_results:
            additional_info = self.generate_content(f"Tell me about {search_results[0]}")
            response = f"{additional_info}\nHere are some links that might help:\n"
            for i, result in enumerate(search_results, start=1):
                response += f"{i}. {result}\n"
        else:
            response = "I couldn't find relevant information for your query. Please try again with a different question."
        return response

    def chat(self, user_input):
        # Process user input and update context
        response = self.process_query(user_input)

        # Update context based on user input
        if "name" in user_input.lower():
            self.user_info["name"] = user_input

        # Enhance contextual understanding (remember user information)
        if "my name" in user_input.lower():
            response = f"Nice to meet you, {self.user_info.get('name', 'there')}! {response}"
        return response

api_key = "####"
api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

admission_chatbot = AdmissionChatbot(api_key)

# Define Gradio interface
iface = gr.Interface(fn=admission_chatbot.chat, inputs="text", outputs="text", live=False)
iface.launch()
