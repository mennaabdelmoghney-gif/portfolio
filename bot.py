
rules = {
    "hello": "Hi there! 😄 How's your day going?",
    "what is ai": "AI is like teaching computers to think, just like humans do! 🤖",
    "how are you": "I'm just a bot, but thanks for asking! Feeling electric ⚡",
    "bye": "Goodbye! Hope you have a fantastic day! 🌟",
    "thanks": "You're welcome! 😊"
}

def get_response(user_input):
    user_input = user_input.lower()

    for key in rules:
        if key in user_input:
            return rules[key]

    fallback_responses = [
        "Hmm... I'm not sure about that 😅",
        "I wish I could understand everything! 🤔",
        "Let's talk about something else! 😎"
    ]
    import random
    return random.choice(fallback_responses)

def chat():
    print("Bot: Hello! 😃 I am your friendly chatbot. You can ask me anything.")
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Bot:", response)

        if "bye" in user_input.lower():
            break

chat()