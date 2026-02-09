welcoming = "Vana: Welcome! I'm Vana."
print(welcoming)
while True:
    vana = input("You: ")
    if vana == "hello":
        print("Vana: Hello There!")
    elif "how are you" in vana:
        print("Vana: I'm Good, You?")
    elif "what is your name" in vana:
        print("Vana: I'm Vana, Your Simple AI Assistant Created By Joel!")
    elif "author" in vana:
        print("Vana: The author i've been created is: Joel")
    elif "goodbye" in vana:
        print("Vana: Have a nice day!")
        break
    else:
        print("Vana: Sorry, I cannot understand.")
