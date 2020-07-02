import pygame, time, random, sys

nome = input("Digite seu nome: ")
while True:
    email = input("Digite seu email: ")
    if email.count("@") > 0 and email.count(".") > 0:
        break
    else:
        print("email invalido")

arquivo = open("HistoricoUsuarios.txt","a")
arquivo.write("Nome: ")
arquivo.write(nome)
arquivo.write("     ")
arquivo.write("Email: ")
arquivo.write(email)
arquivo.write("\n")
arquivo.close()