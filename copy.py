import os
import sys
from cryptography.fernet import Fernet

files = []
files_exception =['thekey.key','main.py']

# Gera e grave chave
chave = Fernet.generate_key()
with open("chave_file.key","wb") as arquivo:
  arquivo.write(chave)



with open("arq_teste.txt","r") as arquivo:
  texto = arquivo.read()
print(texto)

texto = Fernet(chave).encrypt(str.encode(texto))
print(texto)

  
with open("chave_file.key","rb") as arquivo:
  chave_secreta = arquivo.read()

print("############")
print(chave)
print(chave_secreta)  
print("############")


texto = Fernet(chave_secreta).decrypt(texto)
print(texto)

exit(0)


if len(sys.argv) !=3 :
  print("Esperado dois argumentos:\n \
  argumento 1: cript/decript\n \
  argumento 2: diretorio")
  exit()

tipo = sys.argv[1]
diretorio = sys.argv[2]
  
key =Fernet.generate_key()
with open("theky.key","wb") as thekey:
  thekey.write(key)

for file in os.listdir(sys.argv[2]):
  if (file != sys.argv[0]):
    files.append(diretorio+'/'+file)
if tipo == "cript":
  for file in files:
    with open(file,"rb") as thefile:
      contents = thefile.read()
    contents_encripted = Fernet(key).encrypt(contents)
  
    with open(file,"wb") as thefile:
      thefile.write(contents_encripted)
  
    print(f'Arquivo {file} encriptado')
if tipo == "decript":
  print("desencriptando")
  with open("theky.key","rb") as key:
    secretkey = key.read()
  print(secretkey)
  secretkey = secretkey.replace("b'","")
  print(secretkey)


  for file in files:
    with open(file,"rb") as thefile:
      contents = thefile.read()

    #contents_decripted = Fernet(secretkey).decrypt(contents)
  

  
