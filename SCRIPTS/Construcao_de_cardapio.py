from time import sleep
import recebe_func


def cadastra_item():
	print('VOCÊ SELECIONOU "CADASTRAR ITEM"')
	codigo = recebe_func.codigo('Digite o código do produto (0 para retornar ao menu anterior): ')
	if codigo == '0':
		return True
	
	codigos, linhas = recebe_func.ler_codigos_e_linhas()
	
	if codigo in codigos:
		print('CODIGO JA CADASTRADO. OPERAÇÃO CANCELADA.')
		return True
		
	nome = recebe_func.nome('Digite o nome do produto: ')
	preco = recebe_func.preco('Digite o preco do produto: ')
	quantidade = recebe_func.quantidade('Digite a quantidade atual desse produto: ')
	
	arquivo = open('REGISTROS\\CARDAPIO.txt', 'w')
	for linha in linhas:
		arquivo.write(linha)
	arquivo.write(f'{codigo}\t{nome}\t{preco:>5.2f}\t{quantidade}\n')
	arquivo.close()
	
	
def altera_item():
	print('VOCÊ SELECIONOU "ALTERAR ITEM"')
	
	codigos, linhas = recebe_func.ler_codigos_e_linhas()
	
	codigo = recebe_func.codigo('Digite o código do produto a ser alterado (0 para retornar ao menu anterior): ')
	if codigo == '0':
		return True
	while codigo not in codigos:
		print('O CÓDIGO SELECIONADO NÃO ESTÁ NO BANCO DE DADOS. SELECIONE UM CÓDIGO DO BANCO.')
		codigo = recebe_func.codigo('Digite o código do produto a ser alterado: ')
	
	arquivo = open('REGISTROS\\CARDAPIO.txt', 'w')
	
	for linha in linhas:
		if linha[0] == 'USUARIOS':
			arquivo.write(linha)
			continue
		if codigo == linha.split('\t')[0]:
			novo_codigo = codigo_atual = linha.split('\t')[0]
			novo_nome = nome_atual = linha.split('\t')[1]
			novo_preco = preco_atual = float(linha.split('\t')[2])
			novo_quantidade = quantidade_atual = linha.split('\t')[3]
			
			print('ABAIXO SEGUE O ITEM SELECIONADO: ')
			print('CODIGO  NOME            PRECO   QUANTIDADE')
			print(f'{codigo_atual}\t{nome_atual}\t{preco_atual:>5.2f}\t{quantidade_atual}')
			
			print('DENTRE AS CATEGORIAS, QUAL VOCÊ DESEJA ALTERAR')
			print('[1] CODIGO')
			print('[2] NOME')
			print('[3] PRECO')
			print('[4] QUANTIDADE')
			opcao_alteracao = recebe_func.opcao_valida('Digite a opção desejada: ', 4)
			
			if opcao_alteracao == 1:
				novo_codigo = recebe_func.codigo('Digite o código novo do produto: ')
				while novo_codigo in codigos:
					print('O CÓDIGO SELECIONADO JÁ ESTÁ NO BANCO DE DADOS. SELECIONE UM CÓDIGO NOVO.')
					novo_codigo = recebe_func.codigo('Digite o código novo do produto: ')
				novo_nome = nome_atual
				novo_preco = preco_atual
				novo_quantidade = quantidade_atual
			elif opcao_alteracao == 2:
				novo_codigo = codigo_atual
				novo_nome = recebe_func.nome('Digite o nome novo do produto: ')
				novo_preco = preco_atual
				novo_quantidade = quantidade_atual
			elif opcao_alteracao == 3:
				novo_codigo = codigo_atual
				novo_nome = nome_atual
				novo_preco = recebe_func.preco('Digite o novo preço do produto: ')
				novo_quantidade = quantidade_atual
			elif opcao_alteracao == 4:
				novo_codigo = codigo_atual
				novo_nome = nome_atual
				novo_preco = preco_atual
				novo_quantidade = recebe_func.quantidade('Digite a nova quantidade do produto: ')
				novo_quantidade = f'{novo_quantidade}\n'
			arquivo.write(f'{novo_codigo}\t{novo_nome}\t{novo_preco:>5.2f}\t{novo_quantidade}')
			continue
		arquivo.write(linha)
	arquivo.close()
	

def excliur_item():
	print('VOCÊ SELECIONOU "EXCLUIR ITEM"')
	
	codigos, linhas = recebe_func.ler_codigos_e_linhas()
	
	codigo = recebe_func.codigo('Digite o código do produto a ser excluído (0 para retornar ao menu anterior): ')
	if codigo == '0':
		return True
	while codigo not in codigos:
		print('O CÓDIGO SELECIONADO NÃO ESTÁ NO BANCO DE DADOS. SELECIONE UM CÓDIGO DO BANCO.')
		codigo = recebe_func.codigo('Digite o código do produto a ser excluído: ')
	
	arquivo = open('REGISTROS\\CARDAPIO.txt', 'w')
	for linha in linhas:
		if linha[0] == 'USUARIOS':
			arquivo.write(linha)
			continue
		if codigo == linha.split('\t')[0]:
			codigo_excluir = linha.split('\t')[0]
			nome_excluir = linha.split('\t')[1]
			preco_excluir = float(linha.split('\t')[2])
			quantidade_excluir = linha.split('\t')[3]
			
			print('ABAIXO SEGUE O ITEM SELECIONADO: ')
			print('CODIGO  NOME            PRECO   QUANTIDADE')
			print(f'{codigo_excluir}\t{nome_excluir}\t{preco_excluir:>5.2f}\t{quantidade_excluir}')
			
			print('O ITEM SERÁ EXCLUÍDO E A OPERAÇÃO NÃO PODERÁ SER REVERTIDA.')
			print('[1] CONTINUAR')
			print('[2] CANCELAR OPERAÇÃO')
			opcao_exclusao = recebe_func.opcao_valida('Digite a opção desejada: ', 2)
			if opcao_exclusao == 2:
				arquivo.write(linha)
			continue
		arquivo.write(linha)
	print('OPERAÇÃO CANCELADA, ITEM MANTIDO.')


def verifica_senha(time=1):
	senha_correta = '040520'
	senha_tentativa = input('Digite a senha do administrador: ')
	if senha_tentativa == senha_correta:
		return
	print('SENHA INCORRETA')
	time *= 2
	print(f'TENTE NOVAMENTE EM {time} SEGUNDOS')
	sleep(time)
	return verifica_senha(time)


def mostra_menu():
	print('Abaixo as opções da máquina:')
	print('[1] Cadastrar novo item')
	print('[2] Alterar item existente')
	print('[3] Excluir item existente')
	print('[4] ENCERRAR PROGRAMA')
	escolha = recebe_func.opcao_valida('Digite sua escolha: ', 4)
	return escolha


if __name__ == '__main__':
	verifica_senha()
	while True:
		opcao = mostra_menu()
		if opcao == 1:
			cadastra_item()
		if opcao == 2:
			altera_item()
		if opcao == 3:
			excliur_item()
		if opcao == 4:
			break
	print('PROGRAMA FINALIZADO. VERIFIQUE O ARQUIVO "CARDAPIO.txt".')
		