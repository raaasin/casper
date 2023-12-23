from creds import key
import google.generativeai as genai


genai.configure(api_key=key)

def get_response(message):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(message)
    return response.text

def get_message(message):
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    response = chat.send_message("Okay, how about a more detailed explanation to a high schooler?", stream=True)
    return response
