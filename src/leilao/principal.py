from src.leilao.dominio import Avaliador, Usuario, Lance, Leilao

user1 = Usuario('User 1')
user2 = Usuario('User 2')

lance1 = Lance(user1, 50.0)
lance2 = Lance(user2, 100.0)

leilao = Leilao('Celular')

leilao.lances.append(lance1)
leilao.lances.append(lance2)

for lance in leilao.lances:
    print(f'O usuário "{ lance.usuario.nome }" deu um lance de "{ lance.valor }".')

ava = Avaliador()
ava.avalia(leilao)

print(f'O menor lance foi de "{ ava.menor_lance }". O maior lance foi de "{ ava.maior_lance }"')
