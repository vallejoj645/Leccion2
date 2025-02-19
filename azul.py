import random 
elementos = "¿122344567890-abcdefghijklmnñopqrstuvwxyz"
pass_length= int(input"Introduzca la longitud del pase: ")

password = ""
for i in range (pass_length):
    password += random.choice(elementos)

print(password)

