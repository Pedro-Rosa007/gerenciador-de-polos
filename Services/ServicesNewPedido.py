import pandas as pd
from customtkinter import END

class ServicesNewPedidos:
    def __init__(self, view):

        self.view = view



    def open_Frontend(self, tela_atual):

        tela_atual.destroy()  
        from Interface.Frontend import Application
        app = Application()
        app.mainloop()




    def limpar_entradas(self):

        self.view.entrie_nome.delete(0, END)
        self.view.entrie_quantidade.delete(0, END)
        self.view.var_termo.set(0)
        self.view.var_entrega.set(0)



    def coleta_dados_new(self):

        self.nome = self.view.entrie_nome.get().strip()
        self.emissao = self.view.entrie_data.get()
        self.tamanho = self.view.combo_tamanho.get()
        self.quantidade = self.view.entrie_quantidade.get().strip()
        self.termo = self.view.var_termo.get()
        self.tipo = self.view.combo_tipo.get()
        self.entrega = self.view.var_entrega.get()

        self.termo_var = "SIM" if self.termo == 1 else "NÃO"
        self.entrega_var = "SIM" if self.entrega == 1 else "NÃO"


    def datavalidation(self):

        self.coleta_dados_new()
        if not self.quantidade.isdigit():
            self.atualiza_faltadados_info()
            self.limpar_entradas()
            return False
        if self.nome.isdigit() or self.nome == "":
            self.atualiza_faltadados_info()
            self.limpar_entradas()
            return False
        if self.emissao == "":
            self.atualiza_faltadados_info()
            return False
        return True





    def inserir_planilha(self):

        if not self.datavalidation():
            return
        quantidade_int = int(self.quantidade)
        caminho_estoque = "Planilhas/estoque_roupas.xlsx"
        caminho_pedidos = "Planilhas/pedidos_registrados.xlsx"
        try:
            estoque_df = pd.read_excel(caminho_estoque)
        except FileNotFoundError:
            self.atualiza_faltaplanilha_info()
            return
        estoque_df.columns = [col.upper() for col in estoque_df.columns]
        for col in ["TIPO", "TAMANHO", "QUANTIDADE"]:
            if col not in estoque_df.columns:
                self.atualiza_erro_info()
                return
        item_estoque = estoque_df[
            (estoque_df["TIPO"] == self.tipo) &
            (estoque_df["TAMANHO"] == self.tamanho)
        ]
        if item_estoque.empty:
            self.atualiza_erro_info()
            return
        if item_estoque.iloc[0]["QUANTIDADE"] < quantidade_int:
            self.atualiza_faltaroupa_info()
            return
        estoque_df.loc[
            (estoque_df["TIPO"] == self.tipo) &
            (estoque_df["TAMANHO"] == self.tamanho),
            "QUANTIDADE"
        ] -= quantidade_int
        estoque_df.to_excel(caminho_estoque, index=False)

        novo_pedido = {
            "NOME COLABORADOR": self.nome,
            "TIPO DE VESTIMENTA": self.tipo,
            "TAMANHO": self.tamanho,
            "QUANTIDADE": quantidade_int,
            "DATA DO PEDIDO": self.emissao,
            "TERMO ASSINADO": self.termo_var,
            "ENTREGA": self.entrega_var
        }

        try:
            pedidos_df = pd.read_excel(caminho_pedidos)
        except FileNotFoundError:
            pedidos_df = pd.DataFrame(columns=[
                "NOME COLABORADOR", "TIPO DE VESTIMENTA", "TAMANHO",
                "QUANTIDADE", "DATA DO PEDIDO", "TERMO ASSINADO", "ENTREGA"
            ])
        pedidos_df = pd.concat([pedidos_df, pd.DataFrame([novo_pedido])], ignore_index=True)
        pedidos_df.to_excel(caminho_pedidos, index=False)
        self.atualiza_sucesso_info()
        self.limpar_entradas()
        



    def atualiza_sucesso_info(self):
        self._set_info("PEDIDO REGISTRADO COM SUCESSO!")

    def atualiza_erro_info(self):
        self._set_info("ERRO AO REGISTRAR PEDIDO!")

    def atualiza_faltaroupa_info(self):
        self._set_info("ROUPAS INSUFICIENTES NO ESTOQUE!")

    def atualiza_faltaplanilha_info(self):
        self._set_info("PLANILHA DE ESTOQUE NÃO ENCONTRADA!")

    def atualiza_faltadados_info(self):
        self._set_info("INSIRA OS DADOS CORRETAMENTE!")

    def limpar_info(self):
        self._set_info("")

    def _set_info(self, texto):
        self.view.info_add.configure(state="normal")
        self.view.info_add.delete("0.0", "end")
        self.view.info_add._textbox.tag_configure("center", justify="center")
        self.view.info_add.insert("0.0", texto, "center")
        self.view.info_add.tag_add("center", "0.0", "end")
        self.view.info_add.configure(state="disabled")