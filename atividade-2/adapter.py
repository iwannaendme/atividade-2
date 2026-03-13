class Forma:
    def calcular_area(self):
        raise NotImplementedError("Método calcular_area deve ser implementado pelas subclasses.")

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14 * self.raio * self.raio

class RetanguloLegado:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def obter_area_retangular(self):
        return self.largura * self.altura

class RetanguloAdapter(Forma): 
    def __init__(self, retangulo_legado):
        self._retangulo_legado = retangulo_legado

    def calcular_area(self): 
        print("Usando o Adaptador para calcular a área do retângulo...")
        return self._retangulo_legado.obter_area_retangular()

if __name__ == "__main__":
    circulo = Circulo(5)
    print(f"Área do Círculo: {circulo.calcular_area()}")

    retangulo_antigo = RetanguloLegado(10, 5)

    retangulo_adaptado = RetanguloAdapter(retangulo_antigo)
    print(f"Área do Retângulo (via Adapter): {retangulo_adaptado.calcular_area()}")

    todas_as_formas = [circulo, retangulo_adaptado]
    print("\nCalculando áreas de todas as formas:")
    for forma in todas_as_formas:
        print(f"  - Área: {forma.calcular_area()}")