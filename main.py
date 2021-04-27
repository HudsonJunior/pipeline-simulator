busca = 0
decodificacao = 1
execucao = 2 
escrita = 3

class Registrador:
	def __init__(self, valor, destino):
		self.valor = valor
		self.destino = destino

def criar_banco_registradores(registradores):
	for i in range(10):
		registradores.append(Registrador(0,False));



def busca_instrucao(memoria_instrucao, PC, IR):
	IR = memoria_instrucao[PC]
	PC += 1
	return PC, IR

def decodificacao_func(instrucao, registradores, pipeline, flag_execucao_print):
	instrucao = instrucao.replace('\n', '')
	instrucao = instrucao.split(" ")
	operacao = instrucao[0]
	flag_dependencia = False
	operando3 = -1
	operando1 = -1
	operando2 = -1
	if operacao == "lw":
		instrucao[1] = instrucao[1].replace(',', '')
		instrucao[1] = instrucao[1].replace('$', '')
		operando1 = instrucao[1].replace('r','')
		instrucao[2] = instrucao[2].replace('[','')
		instrucao[2] = instrucao[2].replace(']','')
		operando2 = instrucao[2]

		return operacao, operando1, operando2, operando3,flag_execucao_print,flag_dependencia
	elif operacao == "sw":
		instrucao[1] = instrucao[1].replace(',', '')
		instrucao[1] = instrucao[1].replace('$', '')
		operando1 = instrucao[1].replace('r','')
		instrucao[2] = instrucao[2].replace('[','')
		instrucao[2] = instrucao[2].replace(']','')
		operando2 = instrucao[2]
		return operacao,operando1,operando2, operando3,flag_execucao_print,flag_dependencia
	elif operacao == "li":
		instrucao[1] = instrucao[1].replace(',', '')
		instrucao[1] = instrucao[1].replace('$', '')
		operando1 = instrucao[1].replace("r","")
		operando2 = instrucao[2]

		return operacao,operando1,operando2, operando3, flag_execucao_print,flag_dependencia
	elif operacao == "move":
		instrucao[1] = instrucao[1].replace(',', '')
		instrucao[1] = instrucao[1].replace('$', '')
		operando1 = instrucao[1].replace('r','')
		instrucao[2] = instrucao[2].replace(',', '')
		instrucao[2] = instrucao[2].replace('$', '')
		operando2 = instrucao[2].replace('r','')
		if registradores[int(operando2)-1].destino == True:
			flag_execucao_print = False
			flag_dependencia = True
		return operacao, operando1, operando2, operando3, flag_execucao_print, flag_dependencia
	elif operacao == "add":
		instrucao[1] = instrucao[1].replace(',', '')
		instrucao[1] = instrucao[1].replace('$', '')
		operando1 = instrucao[1].replace('r','')
		instrucao[2] = instrucao[2].replace(',', '')
		instrucao[2] = instrucao[2].replace('$', '')
		operando2 = instrucao[2].replace('r','')
		instrucao[3] = instrucao[3].replace(',', '')
		instrucao[3] = instrucao[3].replace('$', '')
		operando3 = instrucao[3].replace('r','')
		if registradores[int(operando2)-1].destino == True or registradores[int(operando3)-1].destino == True:
			flag_execucao_print = False
			flag_dependencia = True
		return operacao, operando1, operando2, operando3, flag_execucao_print, flag_dependencia
	elif operacao == "addi":
		instrucao[1] = instrucao[1].replace(',', '')
		instrucao[1] = instrucao[1].replace('$', '')
		operando1 = instrucao[1].replace('r','')
		instrucao[2] = instrucao[2].replace(',', '')
		instrucao[2] = instrucao[2].replace('$', '')
		operando2 = instrucao[2].replace('r','')
		operando3 = instrucao[3]
		if registradores[int(operando2)-1].destino == True:
			flag_execucao_print = False
			flag_dependencia = True
		return operacao, operando1, operando2, operando3, flag_execucao_print, flag_dependencia
	elif operacao == "sub":
		instrucao[1] = instrucao[1].replace(',', '')
		instrucao[1] = instrucao[1].replace('$', '')
		operando1 = instrucao[1].replace('r','')
		instrucao[2] = instrucao[2].replace(',', '')
		instrucao[2] = instrucao[2].replace('$', '')
		operando2 = instrucao[2].replace('r','')
		instrucao[3] = instrucao[3].replace(',', '')
		instrucao[3] = instrucao[3].replace('$', '')
		operando3 = instrucao[3].replace('r','')
		if registradores[int(operando2)-1].destino == True or registradores[int(operando3)-1].destino == True:
			flag_execucao_print = False
			flag_dependencia = True
		return operacao, operando1, operando2, operando3, flag_execucao_print, flag_dependencia
	elif operacao == "subi":
		instrucao[1] = instrucao[1].replace(',', '')
		instrucao[1] = instrucao[1].replace('$', '')
		operando1 = instrucao[1].replace('r','')
		instrucao[2] = instrucao[2].replace(',', '')
		instrucao[2] = instrucao[2].replace('$', '')
		operando2 = instrucao[2].replace('r','')
		operando3 = instrucao[3]
		if registradores[int(operando2)-1].destino == True:
			flag_execucao_print = False
			flag_dependencia = True
		return operacao, operando1, operando2, operando3, flag_execucao_print, flag_dependencia
	elif operacao == "j":
		operando1 = instrucao[1]
		return operacao, operando1, operando2, operando3, flag_execucao_print, flag_dependencia
	elif operacao == "beq":
		instrucao[1] = instrucao[1].replace(',', '')
		instrucao[1] = instrucao[1].replace('$', '')
		operando1 = instrucao[1].replace('r','')
		instrucao[2] = instrucao[2].replace(',', '')
		instrucao[2] = instrucao[2].replace('$', '')
		operando2 = instrucao[2].replace('r','')
		operando3 = instrucao[3]
		if registradores[int(operando2)-1].destino == True or registradores[int(operando1)-1].destino == True:
			flag_execucao_print = False
			flag_dependencia = True
		return operacao, operando1, operando2, operando3, flag_execucao_print, flag_dependencia
	else:
		return -1, -1, -1, -1, flag_execucao_print, flag_dependencia

def execucao_func(operacao, operando1, operando2, operando3, memoria_dados, registradores, memoria_instrucao, PC, labels):
	if operacao == "lw":
		palavra_carregada = memoria_dados[int(operando2)] ## -1 pois a lista de registradores começa com 0
		return palavra_carregada	

	elif operacao == "sw":
		valor_carregado = registradores[int(operando1) - 1].valor
		return valor_carregado

	elif operacao == "li":
		imediato = int(operando2)
		return imediato

	elif operacao == "move":
		r2 = registradores[int(operando2) - 1].valor
		return r2

	elif operacao == "add":
		soma = registradores[int(operando2)-1].valor + registradores[int(operando3) - 1].valor
		return soma

	elif operacao == "addi":
		soma = registradores[int(operando2)-1].valor + int(operando3)

		return soma

	elif operacao == "sub":
		sub = registradores[int(operando2) -1].valor - registradores[int(operando3) - 1].valor
		return sub

	elif operacao == "subi":
		sub = registradores[int(operando2) -1].valor - int(operando3)
		return sub

	elif operacao == "j":
		return labels[operando1]

	elif operacao == "beq":
		if registradores[int(operando1) - 1].valor == registradores[int(operando2) - 1].valor:
			return labels[operando3] 
		else:
			return PC

def escrita_resultado(operacao, operando1, operando2, resultado, registradores, memoria_dados, flag_dependencia):
	if operacao == "lw":
		registradores[int(operando1) - 1].valor = resultado
	elif operacao == "sw":
		memoria_dados[int(operando2)] = resultado
	elif operacao == "li":
		registradores[int(operando1) - 1].valor = resultado
	elif operacao == "move":
		registradores[int(operando1) - 1].valor = resultado
	elif operacao == "add":
		registradores[int(operando1) - 1].valor = resultado
	elif operacao == "addi":
		registradores[int(operando1) - 1].valor = resultado
	elif operacao == "sub":
		registradores[int(operando1) - 1].valor = resultado
	elif operacao == "subi":
		registradores[int(operando1) - 1].valor = resultado

	if (registradores[int(operando1)-1].destino == True):
		registradores[int(operando1)-1].destino = False
		flag_dependencia = False

def printpipe(clock, memoria_dados, registradores, PC, memoria_instrucao, pipeline):
	
	print("Ciclo de clock: " , clock)
	print("Memoria de dados:\tRegistradores:\t\t\tRegistradores internos:")
	print("Posicao\t| Valor\t\tRegistrador | Valor\t\tRegistrador | Valor")
	for x in range(20) :
		if x == 0:
			print("  ",x,"\t|  ",memoria_dados[x],end="")
			print("              ",x+1,"      |  ",registradores[x].valor,"\t\t     PC    ",end="")
			if PC == '-':
				print("   ",PC)
			else:
				print("   ",PC+1)
		elif x < 10:
			print("  ",x,"\t|  ",memoria_dados[x],end="")
			print("              ",x+1,"      |  ",registradores[x].valor)
		else:
			print("  ",x,"\t|  ",memoria_dados[x])

	print("\n\t\t    Pipeline:")
	print("\tBusca de intrucao: ", end = "")
	print(pipeline[busca],end = "")

	print("\tDecodificação: ", end = "")
	print(pipeline[decodificacao],end="")
	
	print("\tExecução: ", end = "")
	print(pipeline[execucao],end="")
	
	print("\tEscrita do resultado: ", end = "")
	print(pipeline[escrita])
	print("---------------------------------------------------")




def main():
	global busca,decodificao
	memoria_instrucao = ["" for i in range(25)]
	memoria_dados = [0 for i in range(20)]
	pipeline = ["-\n" for i in range(4)]  
	registradores = []
	criar_banco_registradores(registradores)
	PC = 0
	IR = ""
	labels = {}
	clock = 1
	instrucoes = open("instrucoes.txt", 'r')
	instrucao = instrucoes.readline()
	i = 0
	while len(instrucao) > 0:
		label_identifier = instrucao.split(" ")
		if label_identifier[1] != ':\n' and label_identifier[1] != ':':
			memoria_instrucao[i] = instrucao
			i += 1
		else:
			labels.update({label_identifier[0]: i})

		instrucao = instrucoes.readline()

	memoria_instrucao[i-1] = memoria_instrucao[i-1] + "\n" 
	qnt_instrucoes = i
	# --------------------------------------PIPELINE-------------------------------------------------
	flag_busca_print = True
	flag_decodificacao_print = False
	flag_escrita_print = False
	flag_execucao_print = False
	flag_dependencia = False
	flag_jump = False
	flagAtraso = False
	operacao = ""
	operando1 = 0
	operando2 = 0
	operando3 = 0
	resultado = 0
	operando1_aux = 0
	operando2_aux = 0
	operando3_aux = 0
	

	while clock == 1 or (pipeline[busca] != "-\n" or pipeline[decodificacao]!= "-\n" or pipeline[execucao] != "-\n" or pipeline[escrita] != "-\n" ):
		
		if flag_escrita_print == True: 
			pipeline[escrita] = pipeline[execucao]
		else:
			pipeline[escrita] = '-\n'

		if flag_execucao_print == True: #decod
			if operacao in ('add','sub','lw','sw') and flagAtraso == False:
				flagAtraso = True
				pipeline[execucao] = pipeline[decodificacao]
			else:
				if flagAtraso == True:
					flagAtraso = False
				else:
					pipeline[execucao] = pipeline[decodificacao]
		else:
			pipeline[execucao] = '-\n'

		if flag_decodificacao_print == True: 
				pipeline[decodificacao] = IR
		else:
			pipeline[decodificacao] = '-\n'


		if flag_busca_print == True: 
			pipeline[busca] = memoria_instrucao[PC]
		else:
			pipeline[busca] = '-\n'

		
		printpipe(clock, memoria_dados, registradores,PC,memoria_instrucao,pipeline)

		clock += 1

		if pipeline[escrita] != '-\n': #escrita
			flag_dependecia = escrita_resultado(operacao_aux,operando1_aux,operando2_aux,resultado,registradores,memoria_dados,flag_dependencia)

		if pipeline[execucao] != '-\n' and flagAtraso == False: # exec
			
			operando1_aux = operando1
			operando2_aux = operando2
			operando3_aux = operando3
			operacao_aux = operacao
			flag_escrita_print = True


			resultado = execucao_func(operacao,operando1,operando2,operando3,memoria_dados,registradores, memoria_instrucao,PC,labels)
			if (operacao == "beq" or operacao == "j"):
				if PC != resultado:
					PC = resultado
					flag_escrita_print = False
					flag_execucao_print = False
					flag_decodificacao_print = False
					flag_jump = True

				else:
					flag_escrita_print = False
		else:
			flag_escrita_print = False


		if pipeline[decodificacao] != '-\n' and flag_jump == False: #decod
			if flagAtraso == False:
				operacao,operando1,operando2,operando3,flag_execucao_print,flag_dependencia = decodificacao_func(pipeline[decodificacao],registradores,pipeline,flag_execucao_print)

			if flag_dependencia == False:
				if(operacao != 'j' and operacao != 'beq'):
					registradores[int(operando1)-1].destino = True
				flag_execucao_print = True
			else:
				flag_decodificacao_print = True


		if pipeline[busca] != '-\n' and flag_dependencia == False and flag_jump == False: #busca
			if flagAtraso == False:
				PC,IR = busca_instrucao(memoria_instrucao, PC, IR)
				flag_decodificacao_print = True
		else:
			if flagAtraso == False and flag_dependencia == False:
				flag_decodificacao_print = False

		if PC != '-':
			if PC >= qnt_instrucoes:
				flag_busca_print = False
				PC = '-'
		flag_jump = False

main()

