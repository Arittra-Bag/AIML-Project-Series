import gradio as gr
import requests
import json

api_key = "####"
api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

memory = {}

def generate_content(prompt):
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }
    params = {'key': api_key}

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

def chatbot(user_input):
    global memory
    if 'history' not in memory:
        memory['history'] = []

    # Remember user input
    memory['history'].append(user_input)

    # Generate response based on user input and history
    prompt = ' '.join(memory['history'])  # Combine previous inputs
    response = generate_content(prompt)

    # Remember generated response
    memory['history'].append(response)
    return response

# Define Gradio interface
iface = gr.Interface(fn=chatbot, inputs="text", outputs="text")
iface.launch()
