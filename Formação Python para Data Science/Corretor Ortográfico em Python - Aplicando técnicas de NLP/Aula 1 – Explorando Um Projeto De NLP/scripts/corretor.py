# -*- coding: utf-8 -*-
"""Corretor

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13NQPcUsZ70fx-y7V5I5CJS7RDCZWSku0

# <font color = green>Aula 1 – Explorando Um Projeto De NLP

## <font color = blackpink>Importando Um Corpus Textual
"""

with open('artigos.txt', 'r') as f:
  artigos = f.read()

print(artigos[:500])

"""---

## <font color = blackpink>Tokenização
"""

len(artigos)

texto_exemplo = 'Olá, tudo bem?'
tokens = texto_exemplo.split()
print(tokens)

len(artigos.split())

