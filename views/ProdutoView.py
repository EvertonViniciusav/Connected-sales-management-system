import flet as ft
from database.conector import Conector
from controllers.ProdutoController import ProdutoController

def produtoView(page):

    conexao = Conector.conectar()

    elementos = []

    if conexao != None:

        produtos = ProdutoController.listar(conexao)

        page.snack_bar = ft.SnackBar(ft.Text("Conexão Estabelecida!!!"))
        page.snack_bar.open = True

        descricaoField = ft.TextField(label = "Descrição")
        valorField = ft.TextField(label = "Descrição")
        quantidadeField = ft.TextField(label = "Descrição")
        salvarButton = ft.ElevatedButton(text="Salvar")

        divisor = ft.Divider(height = 5)
        tabela = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("ID")),
                ft.DataColumn(ft.Text("Produto")),
                ft.DataColumn(ft.Text("Valor")),
                ft.DataColumn(ft.Text("Quantidade"))
            ],
            rows=[]
        )

        
        datarows = []
        for produto in produtos:
            datarow = ft.DataRow(cells=[
                ft.DataCell(ft.Text(produto.cod)),
                ft.DataCell(ft.Text(produto.descricao)),
                ft.DataCell(ft.Text(produto.preco)),
                ft.DataCell(ft.Text(produto.qtd))])
            datarows.append(datarow)
        tabela.rows = datarows

        elementos.append(descricaoField)
        elementos.append(valorField)
        elementos.append(quantidadeField)
        elementos.append(salvarButton)
        elementos.append(divisor)
        elementos.append(tabela)

    else:
        page.snack_bar = ft.SnackBar(ft.Text("Conexão Não Estabelecida!!!"))
        page.snack_bar.open = True
        

    return ft.Column(elementos)