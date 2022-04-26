
from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador

from unittest import TestCase


class TestAvaliador(TestCase):
    def test_avalia_asc(self):
        user1 = Usuario('User 1')
        user2 = Usuario('User 2')

        lance1 = Lance(user1, 50.0)
        lance2 = Lance(user2, 100.0)

        leilao = Leilao('Celular')

        leilao.lances.append(lance1)
        leilao.lances.append(lance2)

        ava = Avaliador()
        ava.avalia(leilao)

        menor_valor_esperado = 50.0
        maior_valor_esperado = 100.0

        self.assertEqual(menor_valor_esperado, ava.menor_lance)
        self.assertEqual(maior_valor_esperado, ava.maior_lance)

    def test_avalia_desc(self):
        user1 = Usuario('User 1')
        user2 = Usuario('User 2')

        lance1 = Lance(user1, 50.0)
        lance2 = Lance(user2, 100.0)

        leilao = Leilao('Celular')

        leilao.lances.append(lance2)
        leilao.lances.append(lance1)

        ava = Avaliador()
        ava.avalia(leilao)

        menor_valor_esperado = 50.0
        maior_valor_esperado = 100.0

        self.assertEqual(menor_valor_esperado, ava.menor_lance)
        self.assertEqual(maior_valor_esperado, ava.maior_lance)

    def test_avalia_single_lance(self):
        user1 = Usuario('User 1')

        lance1 = Lance(user1, 50.0)

        leilao = Leilao('Celular')

        leilao.lances.append(lance1)

        ava = Avaliador()
        ava.avalia(leilao)

        menor_valor_esperado = 50.0
        maior_valor_esperado = 50.0

        self.assertEqual(menor_valor_esperado, ava.menor_lance)
        self.assertEqual(maior_valor_esperado, ava.maior_lance)

    def test_avalia_multiple_lances(self):
        user1 = Usuario('User 1')
        user2 = Usuario('User 2')
        user3 = Usuario('User 3')

        lance1 = Lance(user1, 50.0)
        lance2 = Lance(user2, 100.0)
        lance3 = Lance(user3, 30.0)

        leilao = Leilao('Celular')

        leilao.lances.append(lance1)
        leilao.lances.append(lance2)
        leilao.lances.append(lance3)

        ava = Avaliador()
        ava.avalia(leilao)

        menor_valor_esperado = 30.0
        maior_valor_esperado = 100.0

        self.assertEqual(menor_valor_esperado, ava.menor_lance)
        self.assertEqual(maior_valor_esperado, ava.maior_lance)
