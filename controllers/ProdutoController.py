import mysql.connector
from models.Produto import Produto

class ProdutoController:

    def inserir(conexao, descricao, preco, quantidade):
        try:
            cursor = conexao.cursor()
            query = "INSERT INTO produto(descricao, preco, quantidade) VALUES(%s, %s, %s)"
            cursor.execute(query, (Produto.descricao, Produto.preco, Produto.qtd))
            conexao.commit()
            print(f"{descricao} Registrado com sucesso!")

        except mysql.connector.Error as e:
            print(f"Erro ao inserir produtos: {e}!!!")

        finally:
            cursor.close()

    def listar(conexao):
        try:
            cursor = conexao.cursor()
            query = "Select * from produto"
            cursor.execute(query)
            registros = cursor.fetchall()

            for produto in registros:
                print(produto)

        except mysql.connector.Error as e:
            print(f"Erro ao listar produtos: {e}!!!")

        finally:
            cursor.close()

    def update(conexao, id_produto, preco, quantidade):
        try:
            cursor = conexao.cursor()
            if quantidade == None:
                query = "UPDATE produto SET preco = %s WHERE id_produto = %s"
                cursor.execute(query, (preco, id_produto))
            elif preco == None:
                query = "UPDATE produto SET quantidade = %s WHERE id_produto = %s"
                cursor.execute(query, (quantidade, id_produto))
            else:
                query = "UPDATE produto SET preco = %s, quantidade = %s WHERE id_produto = %s"
                cursor.execute(query, (preco, quantidade, id_produto))
            conexao.commit()
            print(f"{id_produto} Registrado com sucesso!")

        except mysql.connector.Error as e:
            print(f"Erro ao Atualizar produtos: {e}!!!")

        finally:
            cursor.close()

    def delete(conexao, id_produto):
        try:
            cursor = conexao.cursor()
            query = "DELETE FROM produto WHERE id_produto = %s"
            cursor.execute(query, (id_produto,))
            conexao.commit()
            print(f"{id_produto} Excluido com sucesso!")

        except mysql.connector.Error as e:
            print(f"Erro ao Deletar produtos: {e}!!!")

        finally:
            cursor.close()

    def buscar(conexao, busca):
        listaProduto = []
        try:
            cursor = conexao.cursor()
            query = "SELECT * FROM produto WHERE descricao LIKE %s"
            cursor.execute(query, ("%"+busca+"%",))
            registros = cursor.fetchall()
            for produto in registros:
                objeto = Produto(*produto)
                listaProduto.append(objeto)

        except mysql.connector.Error as e:
            print(f"Erro ao Buscar produtos: {e}!!!")

        finally:
            cursor.close()
        
        return listaProduto