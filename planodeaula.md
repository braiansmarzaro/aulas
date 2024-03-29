- [Introdução](#introdução)
- [Pra que serve o Python?](#pra-que-serve-o-python)
- [Tipos de variáveis e sintaxe básica](#tipos-de-variáveis-e-sintaxe-básica)
  - [Matemática](#matemática)
  - [Álgebra Booleana](#álgebra-booleana)
    - [Ordem de execução](#ordem-de-execução)
- [Manipulação de string](#manipulação-de-string)
- [Condicionais](#condicionais)
- [Loop](#loop)
  - [For](#for)
  - [While](#while)
    - [While True](#while-true)
  - [break](#break)
  - [continue](#continue)
  - [For aninhado](#for-aninhado)
  - [Mistura de for's e while's](#mistura-de-fors-e-whiles)
- [Estruturas compostas](#estruturas-compostas)
  - [Tuplas](#tuplas)
  - [Listas](#listas)
    - [Ponteiro](#ponteiro)
    - [Listas de listas](#listas-de-listas)
    - [List comprehension](#list-comprehension)
  - [Dicionários](#dicionários)
    - [Dict comprehension](#dict-comprehension)
  - [Set](#set)
- [Funções](#funções)
  - [Escopo](#escopo)
  - [Multiplos parâmetros](#multiplos-parâmetros)
  - [Return](#return)
  - [Valores Default e argumentos opcionais](#valores-default-e-argumentos-opcionais)
  - [Tipagem e docstring](#tipagem-e-docstring)
- [Manipulação de arquivos](#manipulação-de-arquivos)
  - [Write modes](#write-modes)
- [Tratamento de erro e exceção](#tratamento-de-erro-e-exceção)
- [Lambda](#lambda)
  - [Reduce](#reduce)
  - [Filter](#filter)
  - [All \& Any](#all--any)
- [Opcionais](#opcionais)
- [Classes](#classes)
  - [Definição](#definição)
  - [self](#self)
  - [Interação entre objetos](#interação-entre-objetos)
  - [init](#init)
  - [Exemplos](#exemplos)
  - [Dunders len,str,repr](#dunders-lenstrrepr)
  - [Inheritance](#inheritance)
  - [@staticmethod](#staticmethod)
  - [@property](#property)
- [API](#api)
  - [O que é](#o-que-é)
  - [Métodos HTTP](#métodos-http)


# Introdução
_Conhecer o time e experiências_
_Background de curso, experiência de trabalho, langs, ingles, de onde é, o que já viu de Py_
# [Pra que serve o Python?](https://www.freecodecamp.org/portuguese/news/para-que-serve-o-python-mais-de-10-casos-de-utilizacao-da-linguagem-de-programacao-python/)
![](assets/graficos.png)
- Linguagem interpretada.
- Pode ser utilizado em terminal, script ou notebook.
- Linguagem de alto nível, portanto mais lenta que C.
- Não é fortemente tipado.
- Orientado a objetos.
- "Fácil" de escrever e compreender.

1. Análise de dados
2. Automatização (arquivos, fluxos de trabalho)
3. Gráficos
4. Joguinhos
5. Inteligência Artifical
6. Redes Neurais
7. Visão Computacional
8. Robótica
9. API
10. Backend
# Tipos de variáveis e sintaxe básica
1. `type()`
2. `int`, `float`, `bool`, `string`
3. `input()`
4. `print()`
## Matemática
+,-,*,**,/,//,%

introdução à biblioteca `math`
`round()`

> 1. Leia três números reais e imprima a média dos três
> 2. Leia um valor de temperatura expresso na escala Celsius e imprima a mesma em graus Fahrenheit. OBS: F = (9/5) * C + 32
## Álgebra Booleana
_Realizar perguntas de teste_
1. Métodos e operações de bool
2. Comparadores (>,<,==,!=)
### [Ordem de execução](https://www.inf.pucrs.br/pinho/PCB/ComandosDeDecisao/Decisao.htm)
![](assets/operadores.png)

# Manipulação de string

1. Operações
2. Methods (replace, isany, count, len, index,upper,lower,find)
3. operador in
4. print detalhado
5. f-string
6. slices

> Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

# Condicionais
1. If
2. Else
3. If aninhado
4. Elif
5. Curiosidades com outros elementos na condição
> 1. Escreva um programa que leia a idade e classifique como na tabela abaixo
> ![exercicio](assets/tabelaif.png)
> 2. Leia duas notas de um aluno, do tipo float, calcule a média e imprima:
> • Aprovado, se média maior ou igual a 7 e menor ou igual a 10;
> • Recuperação, se média maior ou igual a 5 e menor que 7;
> • Reprovado, se média maior ou igual a 0 (zero) e menor que 5.
# Loop
## For
Syntaxe e utilizações
1. Input
2. If
3. Inverso
> Escreva um programa que simula uma contagem regressiva de 10 até 0 com atraso(sleep) e imprima "Boom!" ao final

> Escrever um programa que gera e escreve os números ímpares entre 100 e 200. (Demonstrar diversos meios de fazer)
## While
Casos de uso, como input
Utilização com limite de loop indefinido

> Construir um programa que calcule a média aritmética de vários valores inteiros positivos, lidos externamente. O final da leitura acontecerá quando for lido um valor negativo

> Leia um número inteiro positivo entre 0 e 20 e calcule o seu fatorial.
### While True
> Insira numeros até que haja um número <=0, tire a média aritmética dos numeros entre 13 e 73
## break
## continue
## For aninhado
> Escrever de 00 a 99 usando for aninhado

> Fazer uma tabuada (De um número, ou desenhar uma grande tabela usando o espaçamento igualado e barras.)
> _Tente fazer das duas formas_
> Ex: 
> `1 | 2 | 3 | 4 | 5...`
> `2 | 4 | 6...`
> OU
> `1 x 1 = 1`
> `1 x 2 = 2`
> `1 x 3 = 3`
> `...`
## Mistura de for's e while's
Explicar a ordem de execução e possíveis casos, como a repetição de uma tarefa de repetição.
> Leia 5 números inteiros positivo entre 0 e 20 e calcule o fatorial de cada e exiba os fatoriais e ao final exiba a média dos fatoriais.
# Estruturas compostas
O que é um Iterable
Falar do `iter()` ao final
## Tuplas
1. Criação
2. Operações
3. Imutabilidade
4. Slice
5. Testes de itens dentro de itens
## Listas
1. Operações com listas(+,-,*,**,/)
2. `len`
3. `sum`
4. `.append`
5. `.index`
6. `.count`

### Ponteiro
Explicar o bait do ponteiro
`.copy()`
### Listas de listas
### List comprehension
## Dicionários
### Dict comprehension
## Set

# Funções
`def function(args):`
Importância, utilização, organização de código
Mostrar ao final a transformação de um processo fixado em uma função genérica.

Importância dos parenteses na chamada da função

> Crie uma função que receba uma string e uma substring e conte quantas vezes a substring está dentro da string. Ex:
> `>>>contar('a','maria')`
> `2`

> Crie uma função "matematica" que recebe 5 notas e possa inserir uma operação. O resultado é essa operação executada com os 5 números. As operações são: média, maior, menor.

> Crie uma função que tire a média ponderada da quantidade de números escolhida pelo usuário. O usuário deve poder preencher os números seguidos do seu peso associado. Por exemplo, ao digita 5, depois 3, 5 representa o número e 3 representa o peso.

> Refazer todas as tarefas anteriores utilizando def e generalizando os números fixos
## Escopo
Exemplificar valores de variáveis de mesmo nome em diferentes escopos
## Multiplos parâmetros
## Return
Salvar resultados e matemática
Encerrar o código direto
## Valores Default e argumentos opcionais
Parâmetros e argumentos com `=`
## Tipagem e docstring
Explicar a utilidade e clareza de código

# Manipulação de arquivos
`.txt`,`.csv`,`.json`
## Write modes
read, write, append, binary

# Tratamento de erro e exceção
> É melhor pedir desculpa do que permissão

`try,except,else,finally`

# Lambda
`lambda x: func`
## Reduce
## Filter
## All & Any

# Opcionais
1. Datas e tempo
2. Manipulação de bits
3. Bases numéricas diversas
4. Números complexos
5. Vetores
# Classes

## Definição
Classe vs Objeto
Atributos e métodos

## self
Mostrar escopos dos def
## Interação entre objetos
Gatos e cachorros
## init
Demonstrar que o init pertence ao objeto
## Exemplos
- Cat and Dog
- Jogo de cartas(Modelagem de múltiplas classes: Jogador, Carta, Jogo inteiro)
- Calculadora(Múltiplos métodos e operações)
  - Criar uma classe número para brincar
## Dunders len,str,repr
## Inheritance
Exemplo do Employee
## @staticmethod
## @property

# API
## O que é
## Métodos HTTP
GET, POST, PUT, DELETE
Explicação sobre como as APIs utilizam esses métodos para interação.
