def codigo(str_pergunta):
	recebimento = input(str_pergunta)
	if not (recebimento.isnumeric()):
		print('DIGITE UMA INFORMAÇÃO NUMÉRICA.')
		return codigo(str_pergunta)
	if recebimento == '0':
		return recebimento
	if not len(recebimento) == 4:
		print('CÓDIGO INVÁLIDO, DIGITE UM CÓDIGO DE 4 DIGITOS')
		return codigo(str_pergunta)
	return recebimento


def nome(str_pergunta):
	recebimento = input(str_pergunta)
	if len(recebimento) > 15:
		print('NOME GRANDE DEMAIS, USE NO MÁXIMO 15 CARACTERES.')
		return nome(str_pergunta)
	espaco_disponivel = 15 - len(recebimento)
	recebimento += espaco_disponivel*' '
	return recebimento



def preco(str_pergunta):
	recebimento = input(str_pergunta)
	try:
		float(recebimento)
	except ValueError:
		print('DIGITE UM VALOR NO FORMATO XX.XX')
		return preco(str_pergunta)
	return float(recebimento)


def quantidade(str_pergunta):
	recebimento = input(str_pergunta)
	if not (recebimento.isnumeric()):
		print('DIGITE UMA INFORMAÇÃO NUMÉRICA.')
		return quantidade(str_pergunta)
	recebimento = int(recebimento)
	if not 0 < recebimento:
		print('QUANTIDADE INVÁLIDA.')
		return quantidade(str_pergunta)
	return recebimento


def opcao_valida(str_pergunta, int_qtd):
	recebimento = input(str_pergunta)
	if not (recebimento.isdigit()):
		print('DIGITE APENAS UM NÚMERO DENTRE AS OPÇÕES.')
		return opcao_valida(str_pergunta, int_qtd)
	recebimento = int(recebimento)
	if recebimento not in range(1, int_qtd+1):
		print('OPÇÃO INVÁLIDA. DIGITE UM NÚMERO DENTRE AS OPÇÕES.')
		return opcao_valida(str_pergunta, int_qtd)
	return recebimento
