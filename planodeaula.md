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
    - [Modificação](#modificação)
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
- [Avançado](#avançado)
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
_Conhecer o time e experiências: Background de curso, experiência de trabalho, langs, inglês, de onde é, o que já viu de Py_
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

Introdução à biblioteca `math`
`round()`
Introdução à biblioteca `random` (`randint`,`random`)

> 1. Leia três números reais e imprima a média dos três
> 2. Leia um valor de temperatura expresso na escala Celsius e imprima a mesma em graus Fahrenheit. OBS: F = (9/5) * C + 32
## Álgebra Booleana
_Realizar perguntas de teste_
1. Métodos e operações de bool
2. Comparadores (>,<,==,!=)
### [Ordem de execução](https://www.inf.pucrs.br/pinho/PCB/ComandosDeDecisao/Decisao.htm)
![](assets/operadores.png)

# Manipulação de string

1. print detalhado
2. f-string
3. Operações
4. Methods (replace, isany, count, len, index,upper,lower,find)
5. operador in
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

Introdução ao `sleep` para o exercício
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
O que é um Iterable?

## Tuplas
1. Criação
2. Operações
3. Imutabilidade
4. Slice
5. `len`
6. `sum`
7. `sorted`
8. `.index`
9. `.count`
## Listas
Mostrar o args na função `def foo(*args):`

> Crie uma função que retorne uma lista aleatoria com tamanho definido pela entrada da função.

> Crie uma função que ordene uma lista, usando qualquer algoritmo(sem a função pronta)

> Crie uma função para cadastrar pessoas em uma lista. Cada pessoa é representada por uma tupla(Nome, idade, local). Retorne e exiba a lista

> Em uma cidade do interior, sabe-se que, de janeiro a abril de 1976(121 dias), não ocorreu temperatura inferior a 15ºC nem superior a 40ºC.
As temperaturas verificadas em cada dia serão lidas e armazenadas em um vetor.
Fazer um programa que calcule e imprima: • A menor temperatura ocorrida;
• A maior temperatura ocorrida;
• A temperatura média;
• O número de dias nos quais a temperatura foi inferior à temperatura média.

> Carregar um vetor com uma frase e responder quantas letras existem de cada tipo. Contar também o total de caracteres especiais (que não são letras).

> Escrever um programa que gere n valores e conte quantos deles estão no intervalo [j,k] e quantos deles estão fora do intervalo, escrevendo estas informações ao final. Obs: n,j,k são valores arbitrários.

1. Criação
2. Operações com listas(+,-,*,**,/)

### Modificação
1. `.append`
2. `.insert`
3. `.extend`
4. `.remove`
5. `.pop`
6. `.clear`

### Ponteiro
Explicar o bait do ponteiro
`.copy()`
### Listas de listas
1. Testes de itens dentro de itens
2. Criação de uma matriz
3. Preenchimento
4. Exibição
5. Pesquisa

### List comprehension
Criação de listas usando for
## Dicionários
### Dict comprehension
## Set
Explicar a utilidade(valores únicos e conjuntos)
1. Criação
2. Funções

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
> Leia um arquivo txt com elementos separados por espaço e crie uma lista desses elementos

> Leia um arquivo txt com informações de pessoas separados por espaço em cada linha e crie uma matriz desses elementos

> Leia um arquivo csv com o mesmo conteúdo do de pessoas e crie uma matriz

> Crie uma agenda: Função de adicionar, deletar, ver pessoas, modificar pessoa. Salve em txt
`.txt`,`.csv`,`.json`
## Write modes
read, write, append, binary

# Tratamento de erro e exceção
<q><b>É melhor pedir desculpa do que permissão</b></q>

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
6. Recursão
7. Reduce, Filter, All & Any
# Avançado
1. Análise de dados com Pandas e Numpy
2. Machine Learning & Redes Neurais(TensorFlow, Pytorch, Sklearn)
3. Visão Computacional(OpenCV, Manipulação de Imagem)
# Classes
> [^1]Crie uma classe para representar um horario (hora, minuto e segundo). Implemente os métodos para fazer as operacões de incremento (de segundos) no horário e diferença entre dois horarios.

> [^1]Crie uma classe que modele um carro
(a) Atributos: marca, ano e preço
(b) Metodos: mostrar preço e de exibição dos dados
Leia os dados de 5 carros e um valor p, Mostre as informacões de todos os carros com preço menor que p.

> [^1]Crie uma classe que modele uma pessoa
(a) Atributos: nome, idade e enderec¸o
(b) Metodos: mostrar enderec¸o e alterar endereço
Em seguida, crie uma classe que modele uma aluno
(a) Atributos: nome, numero de matrícula e curso
(b) Metodos: mostrar curso e alterar curso

[^1]: https://www.facom.ufu.br/~backes/gbt017/ListaPython09.pdf
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
