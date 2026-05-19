arquivo = open("loremipsum.txt", "r")
print(arquivo.read())

arquivo.seek(0)
print(arquivo.readline())

arquivo.seek(0)
print(arquivo.read(3))

arquivo.close()

with open("loremipsum.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
