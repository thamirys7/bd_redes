import mysql.connector
from atletasRepository import AtletasRepository
from modalidadesRepository import ModalidadesRepository
from atletas_tem_modalidadesRepository import Atletas_Tem_ModalidadesRepository

atletasRepository = AtletasRepository('10.1.1.109', 'admin', 'admin', 'atletas')
modalidadesRepository = ModalidadesRepository('10.1.1.109', 'admin', 'admin', 'atletas')
atletas_Tem_ModalidadesRepository = Atletas_Tem_ModalidadesRepository('10.1.1.109', 'admin', 'admin', 'atletas')

def inserir():
  nome = input('Nome: ')
  nascimento = input('Data de Nascimento (YYYY-MM-DD): ')
  sexo = input('Sexo (F - Feminino , M - Masculino): ')

  conexao = mysql.connector.connect(
    host="10.1.1.109",
    user="admin",
    password="admin",
    database="atletas"
  )

  cursor = conexao.cursor()

  sql = "INSERT INTO atletas (nome, nascimento, sexo) VALUES (%s, %s, %s)"
  valores = (nome, nascimento, sexo)
  print(sql)
  cursor.execute(sql, valores)

  conexao.commit()

  print(cursor.rowcount, "record inserted.")
  print(f'Inserido novo registro #{cursor.lastrowid}')

def listar():

  conexao = mysql.connector.connect(
    host="10.1.1.109",
    user="admin",
    password="admin",
    database="atletas"
  )

  cursor = conexao.cursor()

  cursor.execute("SELECT * FROM atletas")

  registros = cursor.fetchall()

  print('ID\tNome\tNascimento\tSexo')
  for id, nome, nascimento, sexo in registros:
    print(f'{id}\t{nome}\t{nascimento}\t{sexo}')

def listar_por_nome():
  nome = input('Nome: ')

  conexao = mysql.connector.connect(
    host="10.1.1.109",
    user="admin",
    password="admin",
    database="atletas"
  )

  cursor = conexao.cursor()

  cursor.execute("SELECT * FROM atletas WHERE nome like %s", [f'%{nome}%'])

  registros = cursor.fetchall()

  print('ID\tNome\tNascimento\tSexo')
  for id, nome, nascimento, sexo in registros:
    print(f'{id}\t{nome}\t{nascimento}\t{sexo}')

def listar_por_id():
  id = input('ID: ')

  id, nome, nascimento, sexo = atletasRepository.listarPorId(id)

  print(f'{id}\t{nome}\t{nascimento}\t{sexo}')

def alterar():
  id = int(input('ID: '))
  id, nome, nascimento, sexo = atletasRepository.listarPorId(id)
  novo_nome = input(f'Nome [{nome}]: ')
  if novo_nome == '':
     novo_nome = nome
  novo_nascimento = input(f'Nascimento [{nascimento}]: ')
  if novo_nascimento == '':
     novo_nascimento = nascimento
  novo_sexo = input(f'Sexo [{sexo}]: ')
  if novo_sexo == '':
     novo_sexo = sexo
     
  total_registros = atletasRepository.alterar(novo_nome, novo_nascimento, novo_sexo, id)

  print(total_registros, "registro alterado.")

def apagar():
  id = int(input('ID: '))

  conexao = mysql.connector.connect(
    host="10.1.1.109",
    user="admin",
    password="admin",
    database="atletas"
  )

  cursor = conexao.cursor()

  sql = "DELETE FROM atletas WHERE id=%s"
  valores = (id,)
  cursor.execute(sql, valores)

  conexao.commit()

  print(cursor.rowcount, "registro apagado.")

def listar_atletas_modalidades():
  atletas_tem_modalidades = atletas_Tem_ModalidadesRepository.listarComModalidades()

  print('Atleta\tModalidade')
  for atleta, modalidade in atletas_tem_modalidades:
      print(f'{atleta}\t{modalidade}')

def listar_modalidades():
  modalidades = modalidadesRepository.listar()

  print('ID\tNome')
  for id, nome in modalidades:
      print(f'{id}\t{nome}')

while True:
    print('1. Cadastrar atletas')
    print('2. Listar atletas')
    print('3. Alterar atletas')
    print('4. Apagar atletas')
    print('5. Listar atletas por nome')
    print('6. Listar atletaspor id')
    print('7. Listar atletas por modalidades')
    print('8. Listar modalidade')
    print('9. Sair')

    opcao = int(input())
    if opcao == 1:
        inserir()
    elif opcao == 2:
        listar()
    elif opcao == 5:
        listar_por_nome()
    elif opcao == 6:
        listar_por_id()
    elif opcao == 3:
        listar()
        alterar()
    elif opcao == 4:
        listar()
        apagar()
    elif opcao == 7:
        listar_atletas_modalidades()
    elif opcao == 8:
        listar_modalidades()
    elif opcao == 9:
        print('tchau')
        break