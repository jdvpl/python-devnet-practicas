
from machine import Pin,PWM
import utime

def main():
    servo=PWM(Pin(15), freq=50)

    # definiar la funcion map
    def map(X):
        return int((X-0)*(130-34)/(180-0)+34)
    
    while True:
        angulo=float(input("Ingrese el angulo entre 0 y 180: "))

        if angulo >=0 and angulo<=180:
            m=map(angulo)
            print("resolucion ",m)
            servo.duty(m)
        else:
            print("Digite un angulo entre 0 y 180. ")


if __name__=="__main__":
    main()