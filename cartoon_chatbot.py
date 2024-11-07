def chatbot():
    responses = {
        "doraemon": "Doraemon is a Japanese Anime.",
        "shizuka": "Shizuka is a character in an Anime named Doraemon. She is the best friend of Nobita.",
        "nobita": "Nobita is a character in Doraemon, who often gets into trouble and asks Doraemon for help.",
        "tom": "Tom is a cat from the cartoon Tom and Jerry."
    }

    print("Welcome to Cartoon Talks! Ask me about cartoon characters.")
    
    while True:
        user_input = input("You: ").lower()

        # Find matching character
        found = False
        for character, response in responses.items():
            if character in user_input:
                print(f"Bot: {response}")
                found = True
                break

        if not found:
            if "exit" in user_input:
                print("Bot: Goodbye!")
                break
            else:
                print("Bot: I'm not sure about that character. Try asking about someone else!")

if __name__ == "__main__":
    chatbot()
