import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound
import random

#  speech recognizer
r = sr.Recognizer()

# Function for generate
def get_auto_response(query):
    responses = {
        "नाम": "आपका नाम क्या है?",
        "कैसे हो": "मैं ठीक हूँ। आपको कैसे सेवा कर सकता हूँ?",
        "आज का मौसम": "आज का मौसम बहुत अच्छा है।",
        "प्यार": "प्यार में धोखा मत खाना।",
        "खुश": "खुश रहें, सब ठीक होगा।",
        "राज्य": "भारत के प्रमुख राज्य हैं महाराष्ट्र, गुजरात, मध्य प्रदेश और राजस्थान।",
        "संस्कृति": "भारतीय संस्कृति में विविधता है जैसे की विभिन्न भाषाएं, खानपान, और परंपराएं।",
        "दर्शनीय स्थल": "भारत में विभिन्न दर्शनीय स्थल हैं जैसे की ताजमहल, गोवा, जम्मू कश्मीर।"
        # Add more response
    }
    
    if query in responses:
        return responses[query]
    else:
        return "मुझे क्षमा करें, मैं समझ नहीं पाया।"

#  take voice input, process, and generate 
def chatbot():
    for _ in range(10):  
        with sr.Microphone() as source:
            print("Speak something in Hindi about Indian culture or states:")
            audio = r.listen(source, timeout=5, phrase_time_limit=5)

        try:
            # using Google Speech Recognition
            query = r.recognize_google(audio, language='hi-IN')
            print("You said:", query)

            
            response = get_auto_response(query)

            # Convert the response to speech
            tts = gTTS(text=response, lang='hi')
            tts.save("response.mp3")

        
            playsound("response.mp3")

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Run 
chatbot()
