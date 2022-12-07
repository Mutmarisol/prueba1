#PROGRAMA PARA CONVERTIR SEGUNDOS A MINUTOS



def conversion(segundos):

    minutos = int(segundos / 60 )

    print(minutos)

segundos = input("Ingresa el tiempo en segundos")
conversion(int(segundos))