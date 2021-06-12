class Fraccion:

    def __init__(self, numerador, denominador):
        self.nume = numerador
        self.deno = denominador

    def show(self):
        return '» {} ÷ {}'.format(self.nume, self.deno)


obj_fraccion1 = Fraccion(21, 23)
obj_fraccion2 = Fraccion(35, 36)
obj_fraccion3 = Fraccion(5, 5)
print('Método show de la clase Fraccion...')
print(obj_fraccion1.show())
print(obj_fraccion2.show())
print(obj_fraccion3.show())
