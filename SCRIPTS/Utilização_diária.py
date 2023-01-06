from Construcao_de_cardapio import ler_codigos_e_linhas, recebe_codigo, recebe_quantidade, recebe_informacao_valida


def ler_escolha_continuar():
	print('Abaixo as opções de seguimento:')
	print('[1] Continuar com novos pedidos')
	print('[2] Finalizar pedido')
	escolha = recebe_informacao_valida('Digite sua escolha: ', 2)
	return escolha


def pergunta_continuar():
	opcao_cont = ler_escolha_continuar()
	if opcao_cont == 1:
		return True
	return False


def recebe_pedido(dict_codigos):
	preco = 0
	mesa = input('Digite o código da mesa: ')
	dict_mesa = {}
	itens_pedidos = {}
	dict_mesa[mesa] = itens_pedidos
	novo_pedido = True
	while novo_pedido:
		codigo_pedido = recebe_codigo('Digite o código do produto que deseja pedir: ')
		while codigo_pedido not in dict_codigos:
			print('ITEM NÃO ENCONTRADO')
			codigo_pedido = recebe_codigo('Digite o código do produto que deseja pedir: ')
		if codigo_pedido in itens_pedidos:
			print('ITEM JA ADICIONADO.')
		else:
			qtd_pedido = recebe_quantidade(f'Digite a quantidade do item {codigo_pedido}: ')
			while not 0 < qtd_pedido <= int(dict_codigos[codigo_pedido][3]):
				print(f'A CANTINA NÃO POSSUI ESSA QUANTIDADE DE ITENS, ESCOLHA UMA QUANTIDADE ATÉ '
						f'{dict_codigos[codigo_pedido][3][:-1]}')
				qtd_pedido = recebe_quantidade(f'Digite a quantidade do item {codigo_pedido}: ')
			
			preco_por_item = float(dict_codigos[codigo_pedido][2]) * qtd_pedido
			itens_pedidos[codigo_pedido] = {'codigo': codigo_pedido,
											'nome': dict_codigos[codigo_pedido][1],
											'quantidade': qtd_pedido,
											'preco': preco_por_item}
			
			preco += preco_por_item
			
			novo_pedido = pergunta_continuar()
	
	print('PEDIDO FEITO:')
	print('CODIGO  NOME            QUANTIDADE	PRECO PARCIAL')
	for codigo in itens_pedidos:
		print(f'{itens_pedidos[codigo]["codigo"]}\t{itens_pedidos[codigo]["nome"]}\t'
				f'{itens_pedidos[codigo]["quantidade"]:>10}\t{itens_pedidos[codigo]["preco"]:>13.2f}')
	print(7 * '\t', f' TOTAL: R${preco:>13.2f}')
	return dict_mesa



def mostra_cardapio(list_linhas):
	for linha in list_linhas:
		if not linha[0] == 'C':
			codigo, nome, preco, quantidade = linha.split('\t')
			if not int(quantidade) > 0:
				continue
		print(linha[:-1])


def registra_pedido(dict_mesa, dict_codigos, list_linhas):
	for key in dict_mesa:
		dict_pedido = dict_mesa[key]
	for key in dict_pedido:
		dict_codigos[key][3] = int(dict_codigos[key][3]) - int(dict_pedido[key]["quantidade"])
	
	registra_no_cardapio(list_linhas, dict_codigos, dict_pedido)
	registra_na_conta(dict_pedido)


def registra_no_cardapio(list_linhas, dict_codigos, dict_pedido):
	arquivo = open('REGISTROS\\CARDAPIO.txt', 'w')
	for linha in list_linhas:
		if not linha[0] == 'C':
			codigo_linha = linha.split('\t')[0]
			if codigo_linha in dict_pedido:
				arquivo.write(f'{dict_codigos[codigo_linha][0]}\t{dict_codigos[codigo_linha][1]}\t'
								f'{dict_codigos[codigo_linha][2]}\t{dict_codigos[codigo_linha][3]:}\n')
				continue
		arquivo.write(linha)
	arquivo.close()


def ler_escolha_menu():
	print('Abaixo as opções da máquina:')
	print('[1] Cadastrar novo pedido')
	print('[2] Alterar pedido existente')
	print('[3] Gerar conta de mesa existente')
	print('[4] ENCERRAR PROGRAMA')
	escolha = recebe_informacao_valida('Digite sua escolha: ', 4)
	return escolha


if __name__ == '__main__':
	print('SEJA BEM VINDO À CANTINA.')
	while True:
		opcao = ler_escolha_menu()
		if opcao == 1:
			codigos, linhas = ler_codigos_e_linhas()
			mostra_cardapio(linhas)
			pedido = recebe_pedido(codigos)
			registra_pedido(pedido, codigos, linhas)
		if opcao == 2:
			pass
		if opcao == 3:
			pass
		if opcao == 4:
			break
	gera_relatorio_do_dia()
