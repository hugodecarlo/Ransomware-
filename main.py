import os
import sys
from cryptography.fernet import Fernet

# Gerando a chave
key = Fernet.generate_key()

# Salvando a chave em arquivo
with open("thekey.key", "wb") as key_file:
    key_file.write(key)

# Criptografa o arquivo
file_name = "file.txt"

with open(file_name, "rb") as f:
    original_data = f.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(original_data)

# Sobrescreve o arquivo com os dados criptografados
with open(file_name, "wb") as f:
    f.write(encrypted_data)

# Lê a chave do arquivo
with open("thekey.key", "rb") as key_file:
    key = key_file.read()
    fernet = Fernet(key)

# Decripta o arquivo
with open(file_name, "rb") as f:
    encrypted_data = f.read()
    decrypted_data = fernet.decrypt(encrypted_data)

with open(file_name, "wb") as f:
    f.write(decrypted_data)
# Exibe o conteúdo do arquivo original, criptografado, chave e decriptografado
print("Conteúdo original: ", original_data)
print("Conteúdo criptografado: ", encrypted_data)
print("Chave: ", key)
print("Conteúdo decriptografado: ", decrypted_data)
