import google.generativeai as genai

API_KEY = "AIzaSyCvnsxyM7yefjnFOGJpHkFzqxB7BHzpo20"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

print("Chat started with Gemini 2.0 Flash model.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chat.")
        break
    response = chat.send_message(user_input)
    print(f"Gemini: {response.text}")