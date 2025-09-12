import mysql.connector

class Atletas_Tem_ModalidadesRepository:
    def __init__(self, host, usuario, senha, banco):
        self.host = host
        self.usuario = usuario
        self.senha = senha
        self.banco = banco

    def conectar(self):
        return mysql.connector.connect(
            host=self.host,
            user=self.usuario,
            password=self.senha,
            database=self.banco
        )

    def vincular(self, atletas_id, modalidades_id):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO atletas_tem_modalidades (atletas_id, modalidades_id) VALUES (%s, %s)", (atletas_id, modalidades_id))
        conexao.commit()
        cursor.close()
        conexao.close()

    def listarVinculos(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT atm.id, a.nome, m.nome
            FROM atletas_tem_modalidades atm
            JOIN atletas a ON atm.atletas_id = a.id
            JOIN modalidades m ON atm.modalidades_id = m.id
        """)
        registros = cursor.fetchall()
        cursor.close()
        conexao.close()
        return registros

    def apagar(self, id):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM atletas_tem_modalidades WHERE id = %s", [id])
        conexao.commit()
        cursor.close()
        conexao.close()