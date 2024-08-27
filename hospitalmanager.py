import os
import time
from datetime import datetime
import inquirer
import json

lista_pacientes = []
lista_medicos = []
lista_consultas = []

areas_atendidas = {
  "1": "Dermatologia",
  "2": "Cardiologia",
  "3": "Oncologia",
  "4": "Pediatria",
  "5": "Ginecologia e obstetrícia",
  "6": "Radiologia",
  "7": "Pneumologia",
  "8": "Geriatria",
  "9": "Endocrinologia",
  "10": "Ortopedia",
  "11": "Infectologia"
}

def clear_terminal():
  os.system("cls")

def cadastrar_paciente():
  clear_terminal()
  print("Bem vindo ao cadastro do paciente, por favor, preencha os campos a seguir")

  while True:
    clear_terminal()
    registrar_paciente = str(input("Insira o nome completo do paciente -> "))
    try:
      registrar_CPF = str(input("Insira seu CPF -> "))
    except:
      print("CPF inválido, por favor, insira um CPF válido.")
      time.sleep(2)
      continue
    
    try:
      registrar_idade = int(input("Insira sua idade -> "))
    except:
      print("Erro ao digitar idade, por favor, digite um valor numérico.")
      time.sleep(2)
      continue
    
    registrar_endereco = str(input("Insira seu endereço -> "))
    registrar_sexo = str(input("[M]asculino / [F]eminino / [O]utro -> ").upper())
    if registrar_sexo not in ["M", "F", "O"]:
      print("Sexo inválido, por favor, insira novamente.")
      time.sleep(2)
      continue
    
    registro_completo = {
      "nome": registrar_paciente,
      "cpf": registrar_CPF,
      "idade": registrar_idade,
      "endereco": registrar_endereco,
      "sexo": registrar_sexo
    }
    lista_pacientes.append(registro_completo)
    print("Paciente registrado com sucesso!")
    time.sleep(2)
    break
  return lista_pacientes

def buscar_paciente():
  clear_terminal()
  cpf_recebido = str(input("Por favor, insira o CPF do paciente -> "))
  for paciente in lista_pacientes:
    if paciente["cpf"] == cpf_recebido:
      print(f"Paciente encontrado: {paciente['nome']}\n"
            f"CPF: {paciente['cpf']}\n"
            f"Idade: {paciente['idade']}\n"
            f"sexo: {paciente['sexo']}\n"
            f"endereço: {paciente['endereco']}\n")
      time.sleep(6)
      return paciente
  print("Paciente não encontrado.")
  time.sleep(2)
  return None

def cadastrar_medicos():
  while True:
    clear_terminal()
    registrar_nome = str(input("Insira o nome completo do médico -> "))
    registrar_CRM = str(input("Insira seu CRM -> "))
    registrar_especialidade = str(input(
      "Insira sua especialidade [Índice] \n"
      "1- Dermatologia;\n"
      "2- Cardiologia;\n"
      "3- Oncologia;\n"
      "4- Pediatria;\n"
      "5- Ginecologia e obstetrícia;\n"
      "6- Radiologia;\n"
      "7- Pneumologia;\n"
      "8- Geriatria;\n"
      "9- Endocrinologia;\n"
      "10- Ortopedia;\n"
      "11- Infectologia.\n"
      "Opção -> "))
    especialidade = areas_atendidas.get(registrar_especialidade, "Opção inválida.")
    registrar_endereco = str(input("Insira seu endereço -> "))
    registrar_sexo = str(input("[M]asculino / [F]eminino / [O]utro -> "))
    try: 
      registrar_hora_entrada = datetime.strptime(input("Qual horário de entrada? Siga o sistema 24h (ex: 08:00). -> "), "%H:%M").time()
    except:
      print("Horário inválido. Por favor, insira um horário válido.")
      time.sleep(2)
      continue
    
    try:
      registrar_hora_saida = datetime.strptime(input("Qual horário de saída? Siga o sistema 24h (ex: 17:00). -> "), "%H:%M").time()
    except:
      print("Horário inválido. Por favor, insira um horário válido.")
      time.sleep(2)
      continue

    medico_completo = {
      "nome": registrar_nome,
      "CRM": registrar_CRM,
      "especialidade": especialidade,
      "hora_entrada": registrar_hora_entrada,
      "hora_saida": registrar_hora_saida,
      "sexo": registrar_sexo,
      "endereco": registrar_endereco
    }
    lista_medicos.append(medico_completo)
    print("Médico registrado com sucesso!")
    time.sleep(2)
    return medico_completo

def buscar_medicos(especialidade_busca):
  clear_terminal()
  hora_atual = datetime.now().time()
  medicos_encontrados = []

  for medico in lista_medicos:
    if (especialidade_busca == medico["especialidade"] and
      medico["hora_entrada"] <= hora_atual <= medico["hora_saida"]):
      medicos_encontrados.append(medico)

  if medicos_encontrados:
    for medico in medicos_encontrados:
      print(f"Médico disponível: {medico['nome']}, CRM: {medico['CRM']}, Especialidade: {medico['especialidade']}, fim do expediente: {medico['hora_saida']}")
    time.sleep(6)
  else:
    print("Nenhum médico encontrado dentro do horário de trabalho / área especificada")
    time.sleep(2)
  return medicos_encontrados

def remover_paciente():
  clear_terminal()
  cpf_recebido = input("Qual o CPF do paciente que você quer deletar? -> ")

  for i, paciente in enumerate(lista_pacientes):
    if paciente["cpf"] == cpf_recebido:
      print(f"Paciente encontrado: {paciente['nome']}")
      confirmacao = input("Tem certeza que deseja remover este paciente? (s/n) -> ").lower()
      if confirmacao == 's':
        del lista_pacientes[i]
        print("Paciente removido com sucesso!")
      else:
        print("Operação cancelada.")
      time.sleep(2)
      return
  print("Paciente não encontrado.")
  time.sleep(2)

def remover_medico():
  clear_terminal()
  crm_recebido = input("Qual o CRM do médico que você quer deletar? -> ")

  for i, medico in enumerate(lista_medicos):
    if medico["CRM"] == crm_recebido:
      print(f"Médico encontrado: {medico['nome']}")
      confirmacao = input("Tem certeza que deseja remover este médico? (s/n) -> ").lower()
      if confirmacao == 's':
        del lista_medicos[i]
        print("Médico removido com sucesso!")
      else:
        print("Operação cancelada.")
      time.sleep(2)
      return
  print("Médico não encontrado.")
  time.sleep(2)

def marcar_consulta():
  paciente = buscar_paciente()
  if paciente is None:
    return

  clear_terminal()
  especialidade_busca = str(input("Por favor, insira a especialidade que o paciente busca -> "))
  medicos_disponiveis = buscar_medicos(especialidade_busca)
  if not medicos_disponiveis:
    return
  indice_escolhido = int(input("Por favor, insira o indice do médico escolhido [0/...] -> "))
  medico_escolhido = medicos_disponiveis[indice_escolhido]
  hora_consulta = datetime.now().strftime("%H:%M")

  consulta_detalhes = f"Paciente: {paciente['nome']}, Hora da Consulta: {hora_consulta}, Médico: {medico_escolhido['nome']}"
  lista_consultas.append(consulta_detalhes)

  print(f"Consulta marcada com sucesso!\n{consulta_detalhes}")
  time.sleep(2)
  input("")


def salvar_dados():
    print("Salvando dados...")
    time.sleep(2)

    for medico in lista_medicos:
        medico["hora_entrada"] = medico["hora_entrada"].strftime("%H:%M")
        medico["hora_saida"] = medico["hora_saida"].strftime("%H:%M")

    dados = {
        "pacientes": lista_pacientes,
        "medicos": lista_medicos,
        "consultas": lista_consultas
    }

    with open("hospital_data.json", "w") as arquivo_json:
        json.dump(dados, arquivo_json, indent=2)
    
    print("Dados salvos com sucesso!")
    time.sleep(3)
    clear_terminal()


def carregar_dados():
    global lista_pacientes, lista_medicos, lista_consultas

    try:
        with open("hospital_data.json", "r") as arquivo_json:
            dados = json.load(arquivo_json)

        for medico in dados.get("medicos", []):
            medico["hora_entrada"] = datetime.strptime(medico["hora_entrada"], "%H:%M").time()
            medico["hora_saida"] = datetime.strptime(medico["hora_saida"], "%H:%M").time()

        lista_pacientes = dados.get("pacientes", [])
        lista_medicos = dados.get("medicos", [])
        lista_consultas = dados.get("consultas", [])

        print("Dados carregados com sucesso!")
    except FileNotFoundError:
        print("Arquivo de dados não encontrado, iniciando com listas vazias.")
        lista_pacientes = []
        lista_medicos = []
        lista_consultas = []
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON. Iniciando com listas vazias.")
        lista_pacientes = []
        lista_medicos = []
        lista_consultas = []

    time.sleep(2)

# Menu Principal

carregar_dados()
while True:
  clear_terminal()
  question = [
    inquirer.List(
      "selecao",
      message="=== Sistema de Gerenciamento Hospitalar ===",
      choices=[
        "Gerenciar paciente",
        "Gerenciar Médicos",
        "Agendar Consultas",
        "Sair",
      ],
    )
  ]
  answer = inquirer.prompt(question)
  selecao = answer.get("selecao")
  
  

  if selecao == "Gerenciar paciente":
    while True:
      clear_terminal()
      question = [
        inquirer.List(
          "selecao2",
          message="Escolha uma das seguintes opções",
          choices=[
            "Cadastrar paciente",
            "Buscar paciente",
            "Apagar paciente",
            "Voltar",
          ],
        )
      ]
      answer = inquirer.prompt(question)
      selecao2 = answer.get("selecao2")
      
      if selecao2 == "Cadastrar paciente":
        cadastrar_paciente()
      elif selecao2 == "Buscar paciente":
        buscar_paciente()
      elif selecao2 == "Apagar paciente":
        remover_paciente()
      elif selecao2 == "Voltar":
        break
    
    
    
    
  elif selecao == "Gerenciar Médicos":
    while True:
      clear_terminal()
      question = [
        inquirer.List(
          "selecao3",
          message="Escolha uma das seguintes opções",
          choices=[
            "Cadastrar Médico",
            "Buscar Médico",
            "Apagar Médico",
            "Voltar",
          ],
        )
      ]
      answer = inquirer.prompt(question)
      selecao3 = answer.get("selecao3")
      
      if selecao3 == "Cadastrar Médico":
        cadastrar_medicos()
      elif selecao3 == "Buscar Médico":
        especialidade_busca = str(input("Por favor, insira a especialidade a buscar -> "))
        buscar_medicos(especialidade_busca)
      elif selecao3 == "Apagar Médico":
        remover_medico()
      elif selecao3 == "Voltar":
        break
        
 
    
  elif selecao == "Agendar Consultas":
    marcar_consulta()
  elif selecao == "Sair":
    salvar_dados()
    break
