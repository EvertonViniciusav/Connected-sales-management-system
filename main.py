from database.conector import Conector
from controllers.ProdutoController import ProdutoController

conexao = Conector.conectar()

if conexao != None:
    print("Conectado com o banco de dados!")

    produtos = ProdutoController.buscar(conexao, "Pizza")
    if produtos!=[]:
        for produto in produtos:
            produto.listar()

    else:
        print("Nenhum Produto Encontrado!")
    
    Conector.fecharConexao(conexao)