import flet as ft
from views.ProdutoView import produtoView

def main(page: ft.Page):
    page.title = "Lanchonete do Siri Cascudo"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO
    page.window.height = 600
    page.window.width = 600

    def chamaProduto(e):
        coluna = produtoView(page)
        page.clean()
        page.add(coluna)

    page.add(ft.ElevatedButton("Produtos", on_click = chamaProduto))

ft.app(main)