# Modelar una clase Mate que describa el funcionamiento del mismo:
# a) Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
# b) Un atributo para el estado (lleno o vacío).
# c) El constructor debe recibir como parámetro n, la cantidad máxima de cebadas en base
# a la cantidad de yerba vertida en el recipiente.
# d) Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se
# debe lanzar una excepción que imprima el mensaje Çuidado! Te quemaste!"
# e) Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta
# beber un mate vacío, se debe lanzar una excepción que imprima el mensaje .El mate está
# vacío!"
# f) Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibes. En
# ese caso la cantidad de cebadas restantes se mantendrá en 0, y cada vez que se intente
# beber se debe imprimir un mensaje de aviso: .Advertencia: el mate está lavado.", pero no
# se debe lanzar una excepción.

class Mate:
    def __init__(self, n):
        self.cebadas = n
        self.lleno = True
        self.quedan_cebadas = n
    
    def cebar(self):
        if self.lleno:
            print("¡Cuidado! ¡Te vas a quemar!")
        else:
            print("Mate lleno")
            self.lleno = True

    def tomar(self):
        if not self.lleno:
            raise Exception("¡El mate está vacío!")
        else:
            print("Tomando mate")
            self.quedan_cebadas -= 1
            self.lleno = False
            if self.quedan_cebadas <= 0:
                print("No puedes tomar más mates, el mate está lavado.")
                self.lleno = False

mate = Mate(2)

mate.cebar()
mate.tomar()

for _ in range(7):
    try:
        mate.cebar()
        mate.tomar()
    except Exception as e:
        print(e)