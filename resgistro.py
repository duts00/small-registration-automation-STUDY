#NUMA NOVA ACADEMIA, HÁ 3 PESSOAS, ELAS FAZEM O CADASTRO DELAS, E TODA #VEZ QUE ELAS PASSAREM NA CATRACA, APARECERÁ O TANTO DE DIAS RESTANTES #ATÉ O PRÓXIMO PAGAMENTO DA MENSALIDADE... E TAMBÉM O PLANO QUE ELA #CADASTROU....
#1º pessoa; assinante do pacote de 6 meses...(R$105)
#2º pessoa, assinante do pacote de 3 meses...(R$120)
#3º pessoa, assinante do pacote de 1 mes... (R$145)

#print(f"id: {pessoa[0]['id']}  Nome: {pessoa[0]['nome']}  Assinatura: {pessoa[0]['assinante']}  Valor: {pessoa[0]['valor']}")

#print(f"{pessoa[0]['id']} {pessoa[0]['nome']} {pessoa[0]['assinante']} {pessoa[0]['valor']}")



pessoa = [
    {"id": 1, "nome": "edy", "assi": "pacote de 1 mês", "valor": "R$ 105"},
    {"id": 2, "nome": "yudy", "assi": "pacote de 3 meses", "valor": "R$ 120"},
    {"id": 3, "nome": "cleb", "assi": "pacote de 6 meses", "valor": "R$ 145"}
]
registro = input("Digite aqui seu nome pra entrar na academia: ").strip().lower()
for i in pessoa:
    if i["nome"] == registro:
        print(f"\nBem-vindo, {i['nome']}!")
        print(f"Assinatura: {i['assi']}")
        print(f"Valor: {i['valor']}")
        break
else:
    print("Usuário não encontrado!")
