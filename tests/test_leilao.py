
from src.leilao.dominio import Usuario, Lance, Leilao

from unittest import TestCase


class TestLeilao(TestCase):

    def setUp(self):
        self.user1 = Usuario('User 1')
        self.user2 = Usuario('User 2')
        self.user3 = Usuario('User 3')

        self.lance1 = Lance(self.user1, 50.0)
        self.lance2 = Lance(self.user2, 100.0)
        self.lance3 = Lance(self.user3, 130.0)
        self.lance4 = Lance(self.user1, 75.0)

        self.leilao = Leilao('Celular')

    def test_avalia_asc(self):
        self.leilao.propoe(self.lance1)
        self.leilao.propoe(self.lance2)

        menor_valor_esperado = 50.0
        maior_valor_esperado = 100.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_shouldnt_allow_lances_desc_order(self):
        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance2)
            self.leilao.propoe(self.lance1)

    def test_avalia_single_lance(self):
        self.leilao.propoe(self.lance1)

        menor_valor_esperado = 50.0
        maior_valor_esperado = 50.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_avalia_multiple_lances(self):
        self.leilao.propoe(self.lance1)
        self.leilao.propoe(self.lance2)
        self.leilao.propoe(self.lance3)

        menor_valor_esperado = 50.0
        maior_valor_esperado = 130.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_create_lance_when_theres_no_lances(self):
        self.leilao.propoe(self.lance1)
        self.assertEqual(1, len(self.leilao.lances))

    def test_allow_lance_when_user_is_different_from_the_previous(self):
        self.leilao.propoe(self.lance1)
        self.leilao.propoe(self.lance2)

        self.assertEqual(2, len(self.leilao.lances))

    def test_doesnt_allow_lance_from_the_same_user_twice_in_sequence(self):
        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance1)
            self.leilao.propoe(self.lance4)
