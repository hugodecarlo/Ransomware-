import os
import sys
from cryptography.fernet import Fernet

files = []

with open("arq_teste.txt", "r") as arquivo:
  texto = arquivo.read()
print(texto)

# Gera e grave chave
chave = Fernet.generate_key()
with open("chave_file.key", "wb") as arquivo:
  arquivo.write(chave)

#abre arquivo
with open("arq_teste.txt", "r") as arquivo:
  texto = arquivo.read()

# Criptografa e grava aquivo
texto = Fernet(chave).encrypt(str.encode(texto))
with open("arq_teste.txt", "wb") as arquivo:
  arquivo.write(texto)

print("arquivo criptografado")

#recupera chave
with open("chave_file.key", "rb") as arquivo:
  chave_secreta = arquivo.read()

with open("arq_teste.txt", "r") as arquivo:
  texto = arquivo.read()

texto = Fernet(chave_secreta).decrypt(texto)
print(texto)

with open("arq_teste.txt", "w") as arquivo:
  arquivo.write(str(texto))
