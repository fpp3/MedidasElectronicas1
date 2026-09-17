import serial
import time

PUERTO = '/dev/ttyUSB0'
BAUDRATE = 9600

def enviar(ser, comando):
    ser.write((comando.strip() + '\n').encode('utf-8'))
    ser.flush()
    time.sleep(0.15)

def configurar_generador(ser):
    # Senoidal, unidad Vpp, 2.5 Vpp (da 5 Vpp en circuito abierto) y Offset 0V
    enviar(ser, ":FUNC:WAV 1")
    enviar(ser, ":AMPL:UNIT 1")
    enviar(ser, ":AMPL:VOLT 2.5")
    enviar(ser, ":OFFSet 0")

def esperar_conexion():
    print(f"Buscando conexion en {PUERTO}...")
    while True:
        try:
            ser = serial.Serial(PUERTO, BAUDRATE, timeout=1)
            time.sleep(1.5)
            enviar(ser, "*IDN?")
            resp = ser.readline().decode('utf-8', errors='ignore').strip()
            print(f"Conectado a {PUERTO}")
            if resp:
                print(f"Equipo: {resp}")
            return ser
        except Exception:
            print("No se detecta conexion. Reintentando en 2 segundos...")
            time.sleep(2)

def hacer_barrido(ser, frecuencias):
    configurar_generador(ser)

    modo = input("Modo (1: Automatico, 2: Manual [Enter]): ").strip()
    if modo == "1":
        try:
            dt = float(input("Tiempo entre pasos [segundos]: "))
        except ValueError:
            dt = 1.0
    else:
        dt = 0

    for i, f in enumerate(frecuencias, 1):
        print(f"[{i}/{len(frecuencias)}] Frecuencia: {f} Hz")
        enviar(ser, f":FREQ {f}")
        if modo == "1":
            time.sleep(dt)
        else:
            input("Presione ENTER para continuar...")

def main():
    ser = esperar_conexion()

    while True:
        print("\n1. Barrido grueso")
        print("2. Barrido fino")
        print("3. Salir")
        opcion = input("Opcion: ").strip()

        if opcion == "1":
            # Saltos definidos en la consigna del TP8
            frecuencias = [1000, 2000, 5000, 10000, 20000, 50000, 100000]
            hacer_barrido(ser, frecuencias)

        elif opcion == "2":
            try:
                f_inicio = float(input("Frecuencia inicio [Hz]: "))
                f_fin = float(input("Frecuencia fin [Hz]: "))
                paso = float(input("Paso [Hz]: "))
            except ValueError:
                print("Valores invalidos.")
                continue

            if paso <= 0 or f_fin < f_inicio:
                print("Rango o paso incorrecto.")
                continue

            frecuencias = []
            f = f_inicio
            while f <= f_fin:
                frecuencias.append(round(f, 2))
                f += paso

            hacer_barrido(ser, frecuencias)

        elif opcion == "3":
            ser.close()
            break
        else:
            print("Opcion incorrecta.")

if __name__ == "__main__":
    main()
