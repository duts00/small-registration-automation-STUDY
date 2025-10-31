# Projetos de Cadastro e Registro em Python

> Sobre o projeto: Scripts criados para praticar lógica de programação e manipulação de listas em Python. Estes exercícios foram desenvolvidos de forma educacional, como parte de um aprendizado progressivo em programação.

---

## 1. `cadastro.py`

### Objetivo

Criar um mini sistema de cadastro de alunos com menu interativo no terminal.

### Funcionalidades

* Adicionar aluno — pede o nome e adiciona à lista (validação para evitar duplicados e números)
* Listar alunos — exibe todos os nomes cadastrados
* Remover aluno — exclui um aluno informado pelo nome
* Sair — encerra o programa

### Execução

```bash
python3 cadastro.py
```

### Exemplo de menu

```
inicio
1 - Adicionar aluno
2 - Listar alunos
3 - Remover aluno
4 - Sair
```

---

## 2. `registro.py`

### Objetivo

Simular um sistema simples de registro de alunos em uma academia.

Cada aluno possui:

* ID numérico
* Nome
* Tipo de assinatura (1, 3 ou 6 meses)
* Valor correspondente

### Funcionamento

O usuário digita seu nome ao passar na catraca, e o sistema mostra:

* Mensagem de boas-vindas
* Tipo de plano contratado
* Valor do plano

Se o nome não estiver cadastrado, o sistema informa: `Usuário não encontrado!`

### Execução

```bash
python3 registro.py
```

### Exemplo de saída

```
Digite aqui seu nome pra entrar na academia: yudy

Bem-vindo, yudy!
Assinatura: pacote de 3 meses
Valor: R$ 120
```

---

## Conceitos praticados

* Estruturas de repetição (`for`, `while`)
* Estruturas condicionais (`if`, `elif`, `else`)
* Listas e dicionários (`list`, `dict`)
* Manipulação de strings (`.strip()`, `.lower()`, `.title()`)
* Interação com o usuário via terminal

---

---

## Como contribuir

1. Faça um fork do repositório.
2. Crie uma nova branch para sua alteração: `git checkout -b feat/nova-funcionalidade`
3. Faça commits claros e objetivos.
4. Abra um Pull Request descrevendo o que mudou e por quê.

---

## Nota final

Esses projetos são de caráter educacional, criados para consolidar conceitos de lógica e Python. A intenção é praticar e evoluir, não criar um sistema de produção.

---

