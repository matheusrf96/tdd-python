from src.leilao.dominio import Leilao, Usuario


def generate_wallet_value(wallet_value: float, lance_value: float) -> float:
    user = Usuario('User 1', wallet_value)
    leilao = Leilao('Celular')

    user.propoe_lance(leilao, lance_value)

    return user.carteira

def test_subtract_wallet_value():
    wallet = generate_wallet_value(100.0, 50.0)
    assert wallet == 50.0


def test_lance_value_less_than_wallet_value():
    wallet = generate_wallet_value(100.0, 1.0)
    assert wallet == 99.0


def test_lance_value_equal_wallet_value():
    wallet = generate_wallet_value(50.0, 50.0)
    assert wallet == 0.0


def test_doesnt_allow_lance_value_greater_than_wallet_value():
    wallet = generate_wallet_value(50.0, 100.0)
    assert wallet == 50.0
