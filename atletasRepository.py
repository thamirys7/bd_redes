import mysql.connector

class AtletasRepository:
    def __init__(self, host, usuario, senha, banco):
        self.host = host
        self.usuario = usuario
        self.senha = senha
        self.banco = banco

    def conectar(self):
        conexao = mysql.connector.connect(
            host=self.host,
            user=self.usuario,
            password=self.senha,
            database=self.banco
        )
        return conexao
    
    def listarPorId(self, id):
        conexao = self.conectar()

        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM medicos WHERE id = %s", [id])

        registro = cursor.fetchone()

        return registro
    
    def alterar(self, nome, nascimento, sexo, id):
        conexao = self.conectar()

        cursor = conexao.cursor()

        sql = "UPDATE medicos SET nome=%s, nascimento=%s, sexo=%s WHERE id=%s"
        valores = (nome, nascimento, sexo, id)
        cursor.execute(sql, valores)

        conexao.commit()
        total_afetados = cursor.rowcount
        
        cursor.close()
        conexao.close()

        return total_afetados
    
    def listarComEspecialidades(self):
        conexao = self.conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT m.nome, e.nome FROM medicos m
                JOIN especialidades e
                ON id_especialidade = e.id
        """)

        registros = cursor.fetchall()
        cursor.close()
        conexao.close()

        return registros