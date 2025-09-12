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

  sql = "INSERT INTO modalidades (nome) VALUES (%s)"
  valores = (nome, )
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

  cursor.execute("SELECT * FROM modalidades")

  registros = cursor.fetchall()

  print('ID\tNome')
  for id, nome in registros:
    print(f'{id}\t{nome}')

def listar_por_nome():
  nome = input('Nome: ')

  conexao = mysql.connector.connect(
    host="10.1.1.109",
    user="admin",
    password="admin",
    database="atletas"
  )

  cursor = conexao.cursor()

  cursor.execute("SELECT * FROM modalidades WHERE nome like %s", [f'%{nome}%'])

  registros = cursor.fetchall()

  print('ID\tNome')
  for id, nome in registros:
    print(f'{id}\t{nome}')

def listar_por_id():
  id = input('ID: ')

  id, nome = modalidadesRepository.listarPorId(id)

  print(f'{id}\t{nome}')

def alterar():
  id = int(input('ID: '))
  id, nome = modalidadesRepository.listarPorId(id)
  novo_nome = input(f'Nome [{nome}]: ')
  if novo_nome == '':
     novo_nome = nome
       
  total_registros = modalidadesRepository.alterar(novo_nome, id)

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

  sql = "DELETE FROM modalidades WHERE id=%s"
  valores = (id,)
  cursor.execute(sql, valores)

  conexao.commit()

  print(cursor.rowcount, "registro apagado.")

def listar_modalidades_atletas():
  atletas_tem_modalidades = atletas_Tem_ModalidadesRepository.listarComModalidades()

  print('Atleta\tModalidade')
  for modalidade, atleta in atletas_tem_modalidades:
      print(f'{modalidade}\t{atleta}')

def listar_atletas():
  atletas = atletasRepository.listar()

  print('ID\tNome')
  for id, nome in atletas:
      print(f'{id}\t{nome}')

while True:
    print('1. Cadastrar modalidades')
    print('2. Listar modalidades')
    print('3. Alterar modalidades')
    print('4. Apagar modalidades')
    print('5. Listar modalidades por nome')
    print('6. Listar modalidades por id')
    print('7. Listar modalidades por atletass')
    print('8. Listar atletas')
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
        listar_modalidades_atletas()
    elif opcao == 8:
        listar_atletas()
    elif opcao == 9:
        print('tchau')
        break