import flet as ft
from database.conector import Conector

def produtoView(page):

    conexao = Conector.conectar()

    elementos = []

    if conexao != None:
        page.snack_bar = ft.SnackBar(ft.Text("Conexão Estabelecida!!!"))
        page.snack_bar.open = True
        descricaoField = ft.TextField(label = "Descrição")
        valorField = ft.TextField(label = "Descrição")
        quantidadeField = ft.TextField(label = "Descrição")
        salvarButton = ft.ElevatedButton(text="Salvar")

        elementos.append(descricaoField)
        elementos.append(valorField)
        elementos.append(quantidadeField)
        elementos.append(salvarButton)

    else:
        page.snack_bar = ft.SnackBar(ft.Text("Conexão Não Estabelecida!!!"))
        page.snack_bar.open = True
        

    return ft.Column(elementos)