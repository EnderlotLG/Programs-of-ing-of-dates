import speech_recognition as sp
import moviepy as mv

# Extraer audio del video con moviepy
video = mv.VideoFileClip(r"C:\Users\fdogs\OneDrive\Desktop\ING de Datos\vivsnd.mp4")
video.audio.write_audiofile (r"C:\Users\fdogs\OneDrive\Desktop\ING de Datos\vivsnd.wav")

print("listo")

# Extraer texto del audio del video 
recognizer = sp.Recognizer()
audio_file = sp.AudioFile (r"C:\Users\fdogs\OneDrive\Desktop\ING de Datos\vivsnd.wav")

with audio_file as source:
    audio = recognizer.record(source)
    # Uso del motor de Google
    try:
        texto = recognizer.recognize_google(audio, language='es-ES')
        print(texto)
    except sp.UnknownValueError:
        print("No se pudo reconocer el audio")
        texto = ""
    except sp.RequestError as e:
        print(f"Error en la solicitud a Google Speech Recognition: {e}")
        texto = ""

# Guardar el texto en un archivo
with open (r"C:\Users\fdogs\OneDrive\Desktop\ING de Datos\textovvsnd.txt", "w", encoding="utf-8") as file:
    file.write("Texto:\n")
    file.write(texto)

print("terminamos")
