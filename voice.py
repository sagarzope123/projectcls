import speech_recognition as sr
recognizer = sr.Recognizer()
with sr.microphone() as source:
    while True:
        audio = recognizer.listen(source)
        print(recognizer.recognize_sphinx(audio))
