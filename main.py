import pyttsx3  # <-- this module is text to speech module for windows

if __name__ == '__main__':  # the code runs only when executed directly and not when it is imported as a module
    engine = pyttsx3.init()  # initializing the engine using pyttsx3 library

    engine.setProperty('rate', 137)

    voices = engine.getProperty('voices')  # geta all the available voices in the module
    engine.setProperty('voice', voices[2].id)  # <-- changes the voice of the speaker

    print("Welcome to RoboSpeaker! created by Rohit")
    while True:
        x = input("Enter what you want to say: ")
        if x == "exit":
            engine.say("bye bye friend")
            engine.runAndWait()
            break

        engine.say(x)  # adds the text to be spoken
        engine.runAndWait()  # processes and speaks the added texto