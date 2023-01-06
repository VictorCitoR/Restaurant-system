arquivo = open('CARDAPIO.txt', 'r')
list_linhas = arquivo.readlines()
arquivo.close()

dict_codigos = {}
for linha in list_linhas:
	if linha[0] == 'C':
		continue
	linha = linha[:-1]
	dict_codigos[linha.split('\t')[0]] = linha.split('\t')

for key in dict_codigos:
	print(dict_codigos[key])

dict_pedido = {'0100': {"quantidade": 5}}

for key in dict_pedido:
	dict_codigos[key][3] = int(dict_codigos[key][3]) - int(dict_pedido[key]["quantidade"])

for key in dict_codigos:
	print(dict_codigos.key)