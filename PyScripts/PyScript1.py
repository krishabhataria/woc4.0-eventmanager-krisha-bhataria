import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone() as source:
    print("Clearing background noise...")
    r.adjust_for_ambient_noise(source,duration=1)
    print("Speak anything")
    audio = r.listen(source)
    print("Done recording")
    try:
        text = r.recognize_google(audio,language="en-US")
        print("you said: {} ".format(text))
    except:
        print("sorry could not recognize your voice")
