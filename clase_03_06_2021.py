class Fraccion:

    def __init__(self, numerador, denominador):
        self.nume = numerador
        self.deno = denominador

    def show(self):
        return '» {} ÷ {}'.format(self.nume, self.deno)
