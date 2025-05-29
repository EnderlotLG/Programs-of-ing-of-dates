import speech_recognition as sp 
import pyaudio

#Extraer texto del audio proveniente del microfono
recognizer = sp.Recognizer()
with sp.Microphone() as source:
    print("Diga algo....")
    audio = recognizer.listen(source)
    
    #Convertir el audio obtenido en texto
    try:
        #Uso del motor de Google
        texto=recognizer.recognize_google(audio, language="es-ES")
        print("Texto reconocido: ", texto)
    except sp.UnknownValueError:
        print("No se pudo entender el audio")
    except sp.UnknownValueError:
        print("Error con el servicio de reconocimiento")