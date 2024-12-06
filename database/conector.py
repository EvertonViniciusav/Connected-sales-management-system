import mysql.connector

user = "EvertonViniciusMaster"
senha = "Vinicius2210!"
host = "localhost"
banco = "lanchonete"

class Conector:

    def conectar():
        conexao = None

        try:
            conexao = mysql.connector.connect(
                host = host,
                user = user,
                password = senha,
                database = banco
            )

        except mysql.connector.Error as e:
            print(f"Erro ao Conectar ao Banco de Dados: {e}!!!")

        return conexao
    
    def fecharConexao(conexao):
        if conexao.is_connected():
            conexao.close()
            print("Conexão encerrada")