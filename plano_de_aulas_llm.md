<img width="800" height="1163" alt="image" src="https://github.com/user-attachments/assets/0edfa534-7d51-49cd-8b82-ba05d4487478" />



# O que é IA e o que é LLM?
- **IA**:
  - Descobre a "regra" entre entrada e saída
- **LLM**:
  - Calcula a estatística da próxima palavra (ou token)

## Por que isso é revolucionário?

**Escalabilidade**: Como ele processa tudo ao mesmo tempo, podemos treiná-lo com volumes massivos de dados (a internet inteira).

**Contexto Longo**: Ele consegue manter a **linha de raciocínio** de um texto inteiro, pois a **atenção** conecta o parágrafo atual com algo dito 10 páginas atrás.


## Use-cases conhecidos
1. Chatbots e assistentes
2. Doc scavenger
3. Creative
4. Agents (Tools)
5. text-to-text
6. text-to-image
7. text-to-audio
8. audio-to-text

# Como a LLM _pensa_?
- Analogia do Corretor de Celular
  O algoritmo não "entende" sentimentos, ele calcula a probabilidade da próxima peça do quebra-cabeça.

<img width="2001" height="1023" alt="image" src="https://github.com/user-attachments/assets/ec4b5f3e-e94f-4efc-8286-2980de2ee3e3" /> [^1]

- Multiplas matrizes (weights)


## Transformers: O Marco de 2017

> Imagine que, antes de 2017, as IAs liam textos como nós: uma palavra por vez, da esquerda para a direita. Se a frase fosse longa, elas "esqueciam" o início quando chegavam ao fim.

> O Transformer mudou isso ao permitir o Processamento Paralelo. Ele olha para a frase inteira de uma só vez, como se tirasse uma fotografia de todas as palavras simultaneamente.

<img width="809" height="648" alt="image" src="https://github.com/user-attachments/assets/4552678d-e50b-45c1-b5dc-a03d50d11e20" />

<img width="1751" height="985" alt="image" src="https://github.com/user-attachments/assets/b8a253b6-cafd-4f2a-9e0a-f6fce7bd243b" /> [^1]


## Self-Attention

**O Problema**: Palavras sozinhas são ambíguas. Exemplo: "O banco estava fechado, então ele sentou no banco da praça."

**A Solução**: O mecanismo de Atenção permite que cada palavra "olhe" para as outras ao seu redor para entender seu próprio significado.

- No primeiro "banco", a IA dá mais "atenção" à palavra "fechado" (financeiro).
- No segundo "banco", ela foca em "praça" e "sentou" (mobília).

## Treinamento

<img width="1938" height="1059" alt="image" src="https://github.com/user-attachments/assets/df8345ed-63a6-4879-a4ff-07aebe7f1758" /> [^1]


## Token
[Tokenizer OpenAI](https://platform.openai.com/tokenizer)

## Conceito de Embedding
> IA não entende letras, ela transforma palavras em números (vetores).
Exemplo: um mapa 3D onde palavras com significados próximos (ex: "cachorro" e "lobo") moram no mesmo bairro.

<img width="1124" height="761" alt="image" src="https://github.com/user-attachments/assets/dcaecb37-8082-43bc-874d-4d16e0f4db69" /> [^2]

<img width="1164" height="500" alt="image" src="https://github.com/user-attachments/assets/1e6a0054-f6b0-454b-b5db-aefca0b7c9fd" /> [^2]


# Engenharia de Prompt

## System Prompt & User input

## Personas

## Zero-Shot

## Few-Shot

## Chain-of-thought




# Limitações
1. Hallucination
2. Prompt Injection



[^1]: https://youtu.be/LPZh9BOjkQs?si=BEfW5IkJwdNYUgqt
[^2]: https://www.youtube.com/watch?v=eMlx5fFNoYc
