import flet as ft
from database.conector import Conector

def produtoView(page):

    conexao = Conector.conectar()

    elementos = []

    if conexao != None:
        page.snack_bar = ft.SnackBar(ft.Text("Conexão Estabelecida!!!"))
        page.snack_bar.open = True

    else:
        dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text("Atenção"),
            content=ft.Text("Não foi possivel conectar com o banco de dados!!!"),
            actions=[
                ft.TextButton("Sair", on_click=lambda e: print("Sair")),
            ],
        )

        elementos.append(dlg)

    return ft.Column(
        controls = elementos
    )