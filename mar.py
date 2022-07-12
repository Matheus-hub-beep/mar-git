class Mar:
    def __init__(self, classificao, minutos, quantidade_episodios=1):
        self.__classificacao = classificao
        self.__minutos = minutos
        self.__quantidade_episodios = quantidade_episodios
        self.minutos_totais = self.calcula_total_minutos()

    def __radd__(self, other):
        return other + self.minutos_totais

    @property
    def classificacao(self):
        return self.__classificacao

    @property
    def minutos(self):
        return self.__minutos

    @property
    def quantidade_episodios(self):
        return self.__quantidade_episodios

    def calcula_total_minutos(self):
        return self.__minutos * self.__quantidade_episodios

    def adicionar_minutos_extra(self, minutos_extra):
        self.minutos_totais += minutos_extra

    def funcao_teste(self):
        pass

class Suporte_mar:
    def __init__(self):
        self.__lista = []

    def adicionar_programa(self, programa):
        self.__lista.append(programa)

    def imprimi_horas_de_mar(self):
        return sum(self.__lista) // 60



