import mysql.connector

class ModalidadesRepository:
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

        cursor.execute("SELECT * FROM modalidades WHERE id = %s", [id])

        registro = cursor.fetchone()
        
        cursor.close()
        conexao.close()

        return registro
    
    def alterar(self, nome, id):
        conexao = self.conectar()

        cursor = conexao.cursor()

        sql = "UPDATE modalidades SET nome=%s WHERE id=%s"
        valores = (nome, id)
        cursor.execute(sql, valores)

        conexao.commit()
        
        total_afetados = cursor.rowcount

        cursor.close()
        conexao.close()

        return total_afetados
    
