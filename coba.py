import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

def translate_and_speak():
    recognizer = sr.Recognizer()

    try:
        
        with sr.Microphone() as source:
            print("Silakan bicara dalam bahasa Inggris...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

         
            print("Mengenali suara...")
            text = recognizer.recognize_google(audio, language="en-US")
            print(f"Teks yang dikenali: {text}")

     
            print("Menerjemahkan teks...")
            translated_text = GoogleTranslator(source='en', target='id').translate(text)
            print(f"Hasil terjemahan: {translated_text}")

            
            print("Mengonversi hasil terjemahan menjadi suara...")
            tts = gTTS(text=translated_text, lang="id")
            tts.save("hasil_terjemahan.mp3")

           
            print("Memutar suara hasil terjemahan...")
            os.system("start hasil_terjemahan.mp3" if os.name == "nt" else "mpg123 hasil_terjemahan.mp3")

    except sr.UnknownValueError:
        print("Maaf, suara tidak dapat dikenali.")
    except sr.RequestError as e:
        print(f"Kesalahan pada layanan pengenalan suara: {e}")
    except Exception as e:
        print(f"Kesalahan: {e}")

if __name__ == "__main__":
    translate_and_speak()
