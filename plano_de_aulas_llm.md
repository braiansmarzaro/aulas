


# O que é IA e o que é LLM?
- **IA**:
  - Descobre a "regra" entre entrada e saída
- **LLM**:
  - Calcula a estatística do próximo token 

## Por que isso é revolucionário?
**Escalabilidade**: Como ele processa tudo ao mesmo tempo, podemos treiná-lo com volumes massivos de dados (a internet inteira).

**Contexto Longo**: Ele consegue manter a **linha de raciocínio** de um texto inteiro, pois a **atenção** conecta o parágrafo atual com algo dito 10 páginas atrás.


## Use-cases conhecidos
1. Chatbot
2. Doc scavenger
3. Creative
4. Agents (Tools)

# Como a LLM pensa?
- Exemplo do corretor do celular para algoritmo de previsão

## Transformers

> Imagine que, antes de 2017, as IAs liam textos como nós: uma palavra por vez, da esquerda para a direita. Se a frase fosse longa, elas "esqueciam" o início quando chegavam ao fim.

> O Transformer mudou isso ao permitir o Processamento Paralelo. Ele olha para a frase inteira de uma só vez, como se tirasse uma fotografia de todas as palavras simultaneamente.

<img width="809" height="648" alt="image" src="https://github.com/user-attachments/assets/4552678d-e50b-45c1-b5dc-a03d50d11e20" />


## Self-Attention

**O Problema**: Palavras sozinhas são ambíguas. Exemplo: "O banco estava fechado, então ele sentou no banco da praça."

**A Solução**: O mecanismo de Atenção permite que cada palavra "olhe" para as outras ao seu redor para entender seu próprio significado.

- No primeiro "banco", a IA dá mais "atenção" à palavra "fechado" (financeiro).
- No segundo "banco", ela foca em "praça" e "sentou" (mobília).

## Treinamento



## Token
[Tokenizer OpenAI](https://platform.openai.com/tokenizer)

## Conceito de Embedding
> IA não entende letras, ela transforma palavras em números (vetores).
Exemplo: um mapa 3D onde palavras com significados próximos (ex: "cachorro" e "lobo") moram no mesmo bairro.

## Principio de funcionamento simplificado
Modelo estatístico de texto


# Engenharia de Prompt

## System Prompt & User input

## Personas

## Zero-Shot

## Few-Shot

## Chain-of-thought




# Limitações
1. Hallucination
2. Prompt Injection
