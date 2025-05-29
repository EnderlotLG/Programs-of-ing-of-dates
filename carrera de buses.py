import threading
import time
import random
import os
import sys

meta = 50
ganador = None
lock = threading.Lock()

# Bus ASCII compacto
def obtener_bus(nombre):
    return [
        " .-----------------------'  |",
        f"/| _ .---. .---. .---. {nombre[:4]:<4}|",   # nombre abreviado si es largo
        "|j||||___| |___| |___| |___||",
        "|=|||=======================|",
        "[_|j||(O)\\__________|(O)\\___]"
    ]

def limpiar_pantalla():
    # Usa el comando apropiado según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')

def dibujar_carrera(posiciones, nombres):
    # Limpia la pantalla antes de dibujar
    limpiar_pantalla()
    
    print("🏁 Carrera de Buses - CONSOLA ANIMADA 🛣️\n")
    
    # Dibuja los carriles
    for i, nombre in enumerate(nombres):
        print(f"🚌 {nombre}")
        print("+" + "-" * (meta + 30) + "+")
        
        # Obtener el bus para este competidor
        bus = obtener_bus(nombre)
        pos = min(posiciones[i], meta)
        
        # Dibujar carril con el bus en la posición correcta
        for linea in bus:
            print("|" + " " * pos + linea + " " * (meta + 28 - len(linea) - pos) + "|")
        
        print("+" + "-" * (meta + 30) + "+")
        print()
    
    # Si hay un ganador, mostrarlo
    if ganador:
        print(f"\n🚨 ¡{ganador} ha ganado la carrera!")

class Bus(threading.Thread):
    def __init__(self, nombre, indice, nombres, posiciones):
        super().__init__()
        self.nombre = nombre
        self.indice = indice
        self.nombres = nombres
        self.posiciones = posiciones
        
    def run(self):
        global ganador
        while self.posiciones[self.indice] < meta and ganador is None:
            time.sleep(random.uniform(0.1, 0.3))
            self.posiciones[self.indice] += random.randint(1, 3)
            
            # Actualizar la pantalla después de cada movimiento
            with lock:
                dibujar_carrera(self.posiciones, self.nombres)
                
                # Verificar si este bus es el ganador
                if self.posiciones[self.indice] >= meta and ganador is None:
                    ganador = self.nombre

def carrera():
    global ganador
    ganador = None
    
    # Configuración de la carrera
    nombres = ["REDBULL", "MONSTER"]
    posiciones = [0, 0]  # Posiciones iniciales
    
    # Dibujo inicial
    dibujar_carrera(posiciones, nombres)
    
    # Crear e iniciar los buses
    buses = []
    for i, nombre in enumerate(nombres):
        bus = Bus(nombre, i, nombres, posiciones)
        buses.append(bus)
        bus.start()
    
    # Esperar a que todos terminen
    for bus in buses:
        bus.join()
    
    # Mostrar resultado final
    dibujar_carrera(posiciones, nombres)
    print(f"\n🚨 ¡{ganador} ha ganado la carrera!")

# Ejecutar la carrera
if __name__ == "__main__":
    carrera()