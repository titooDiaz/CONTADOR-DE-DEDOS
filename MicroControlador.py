from machine import Pin, Timer
import time

# Variable para controlar el estado del LED Y MOTOR
encendido = False
direccion = 2

# Configurar el pin del LED
led = Pin(15, Pin.OUT)

# Configurar los pines del motor
DIR = Pin(19, Pin.OUT)
STEP = Pin(20, Pin.OUT)

# Función de control del LED
def control_led(timer):
    global encendido
    if encendido:
        led.on()  # Encender el LED
    else:
        led.off()  # Apagar el LED
    encendido = encendido  # Alternar el estado

# Configurar el temporizador para controlar el LED cada segundo (1000 ms)
timer = Timer()
timer.init(freq=1, mode=Timer.PERIODIC, callback=control_led)

DIR.off()
# Bucle principal para hacer girar el motor continuamente
while True:
    if direccion == 1:
        DIR.on()  # Establecer el pin DIR en alto
        STEP.on()  # Establecer el pin STEP en alto
        time.sleep(0.01)  # Esperar 1 ms
        STEP.off()  # Establecer el pin STEP en bajo
        time.sleep(0.01)  # Esperar 1 ms
    elif direccion == 2:
        STEP.on()  # Establecer el pin STEP en alto
        time.sleep(0.01)  # Esperar 1 ms
        STEP.off()  # Establecer el pin STEP en bajo
        time.sleep(0.01)  # Esperar 1 ms
    elif direccion == 3:
        pass
    
    
