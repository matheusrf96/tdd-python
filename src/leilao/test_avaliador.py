
from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador

from unittest import TestCase


class TestAvaliador(TestCase):

    def setUp(self):
        self.user1 = Usuario('User 1')
        self.user2 = Usuario('User 2')
        self.user3 = Usuario('User 3')

        self.lance1 = Lance(self.user1, 50.0)
        self.lance2 = Lance(self.user2, 100.0)
        self.lance3 = Lance(self.user3, 30.0)

        self.leilao = Leilao('Celular')

    def test_avalia_asc(self):
        self.leilao.propoe(self.lance1)
        self.leilao.propoe(self.lance2)

        ava = Avaliador()
        ava.avalia(self.leilao)

        menor_valor_esperado = 50.0
        maior_valor_esperado = 100.0

        self.assertEqual(menor_valor_esperado, ava.menor_lance)
        self.assertEqual(maior_valor_esperado, ava.maior_lance)

    def test_avalia_desc(self):
        self.leilao.propoe(self.lance2)
        self.leilao.propoe(self.lance1)

        ava = Avaliador()
        ava.avalia(self.leilao)

        menor_valor_esperado = 50.0
        maior_valor_esperado = 100.0

        self.assertEqual(menor_valor_esperado, ava.menor_lance)
        self.assertEqual(maior_valor_esperado, ava.maior_lance)

    def test_avalia_single_lance(self):
        self.leilao.propoe(self.lance1)

        ava = Avaliador()
        ava.avalia(self.leilao)

        menor_valor_esperado = 50.0
        maior_valor_esperado = 50.0

        self.assertEqual(menor_valor_esperado, ava.menor_lance)
        self.assertEqual(maior_valor_esperado, ava.maior_lance)

    def test_avalia_multiple_lances(self):
        self.leilao.propoe(self.lance1)
        self.leilao.propoe(self.lance2)
        self.leilao.propoe(self.lance3)

        ava = Avaliador()
        ava.avalia(self.leilao)

        menor_valor_esperado = 30.0
        maior_valor_esperado = 100.0

        self.assertEqual(menor_valor_esperado, ava.menor_lance)
        self.assertEqual(maior_valor_esperado, ava.maior_lance)
