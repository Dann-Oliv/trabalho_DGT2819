arquivo = open("texto.txt", "w")

texto = list()
texto.append("Primeira frase do arquivo.\n")
texto.append("Segunda frase do arquivo.\n")
texto.append("Terceira frase do arquivo.\n")

arquivo.writelines(texto)
arquivo.close()
