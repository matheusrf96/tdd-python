from src.leilao.dominio import Leilao, Usuario


def test_subtract_wallet_value():
    user1 = Usuario('User 1', 100.0)
    leilao = Leilao('Celular')

    user1.propoe_lance(leilao, 50.0)

    assert user1.carteira == 50.0
