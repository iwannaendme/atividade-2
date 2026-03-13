class Bebida:
    def get_descricao(self):
        return "Bebida desconhecida"

    def get_custo(self):
        return 0.0

class CafePuro(Bebida):
    def get_descricao(self):
        return "Café Puro"

    def get_custo(self):
        return 2.00

class Cha(Bebida):
    def get_descricao(self):
        return "Chá Simples"

    def get_custo(self):
        return 1.50

class DecoradorBebida(Bebida):
    def __init__(self, bebida):
        self._bebida = bebida

    def get_descricao(self):
        return self._bebida.get_descricao() 

    def get_custo(self):
        return self._bebida.get_custo()

class Leite(DecoradorBebida):
    def __init__(self, bebida):
        super().__init__(bebida)

    def get_descricao(self):
        return self._bebida.get_descricao() + ", Leite"

    def get_custo(self):
        return self._bebida.get_custo() + 0.50

class Acucar(DecoradorBebida):
    def __init__(self, bebida):
        super().__init__(bebida)

    def get_descricao(self):
        return self._bebida.get_descricao() + ", Açúcar"

    def get_custo(self):
        return self._bebida.get_custo() + 0.10

class Chantilly(DecoradorBebida):
    def __init__(self, bebida):
        super().__init__(bebida)

    def get_descricao(self):
        return self._bebida.get_descricao() + ", Chantilly"

    def get_custo(self):
        return self._bebida.get_custo() + 1.00

if __name__ == "__main__":

    meu_cafe = CafePuro()
    print(f"{meu_cafe.get_descricao()} - R${meu_cafe.get_custo():.2f}")

    cafe_com_leite = Leite(CafePuro())
    print(f"{cafe_com_leite.get_descricao()} - R${cafe_com_leite.get_custo():.2f}")

    cafe_com_leite_e_acucar = Acucar(Leite(CafePuro()))
    print(f"{cafe_com_leite_e_acucar.get_descricao()} - R${cafe_com_leite_e_acucar.get_custo():.2f}")

    cha_especial = Chantilly(Cha())
    print(f"{cha_especial.get_descricao()} - R${cha_especial.get_custo():.2f}")

    cafe_completo = Chantilly(Acucar(Leite(CafePuro())))
    print(f"{cafe_completo.get_descricao()} - R${cafe_completo.get_custo():.2f}")