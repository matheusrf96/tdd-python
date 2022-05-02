
from src.leilao.excecoes import LanceInvalido


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0.0
        self.menor_lance = 0.0

    @property
    def lances(self) -> list:
        return self.__lances[:]

    def propoe(self, lance: Lance) -> bool:
        if self._lance_valido(lance):
            if not self._tem_lances():
                self.menor_lance = lance.valor

            self.maior_lance = lance.valor
            self.__lances.append(lance)

    def _tem_lances(self):
        return self.__lances

    def _usuarios_differentes(self, lance: Lance) -> bool:
        if self.__lances[-1].usuario != lance.usuario:
            return True

        raise LanceInvalido('O mesmo usuário não pode dar dois lances em sequência.')

    def _valor_maior_que_anterior(self, lance: Lance) -> bool:
        if lance.valor > self.__lances[-1].valor:
            return True

        raise LanceInvalido('O valor do lance tem que ser maior que a anterior.')

    def _lance_valido(self, lance: Lance) -> bool:
        return not self._tem_lances() or self._usuarios_differentes(lance) and self._valor_maior_que_anterior(lance)


class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def propoe_lance(self, leilao: Leilao, valor: float):
        if valor > self.__carteira:
            raise LanceInvalido('Não é permitido propor lance com valor maior que o da carteira.')

        lance = Lance(self, valor)
        leilao.propoe(lance)

        self.__carteira -= valor
