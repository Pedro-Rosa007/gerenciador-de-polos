import pandas as pd
from customtkinter import END
class ServicesNewPedidos:

    def open_Frontend(self, tela_atual):
        tela_atual.destroy()  
        from Interface.Frontend import Application
        app = Application()
        app.mainloop()



    def limpar_entradas(self):

        self.entrie_nome.delete(0,END)
        self.entrie_quantidade.delete(0, END)
        self.var_termo.set(0)

    def coleta_dados_new(self):
        self.nome = self.entrie_nome.get().strip()
        self.emissao = self.entrie_data.get()
        self.tamanho = self.combo_tamanho.get()
        self.quantidade = self.entrie_quantidade.get().strip()  
        self.termo = self.var_termo.get()
        self.tipo = self.combo_tipo.get()
    
        self.termo_var = "SIM" if self.termo == 1 else "NÃO"
        
    def datavalidation(self):

        self.coleta_dados_new()
        if not self.quantidade.isdigit():
            print("ERRO MODAL DADOS INCOMPLETOS")
            self.limpar_entradas()
        else:
            pass
        if self.nome.isdigit():
            print("ERRO MODAL DADOS INCOMPLETOS")
            self.limpar_entradas()
        else:
            pass

    def validar_quantidade(self):

        self.datavalidation()
        self.caminho_estoque = "Planilhas/estoque_roupas.xlsx" 

 
        self.estoque_df = pd.read_excel(self.caminho_estoque)

        self.tipo_vestimenta = self.tipo
        self.tamanho = self.tamanho
        self.quantidade = self.quantidade

        
        self.item_estoque = self.estoque_df[
            (self.estoque_df["TIPO"] == self.tipo_vestimenta) & 
            (self.estoque_df["TAMANHO"] == self.tamanho)
        ]
        if not self.item_estoque.empty and self.item_estoque.iloc[0]["QUANTIDADE"] >= self.quantidade:
         print("Estoque suficiente! Pode registrar o pedido.")
        else:
         print("ERRO: Estoque insuficiente!")





    def inserir_planilha(self, nome, tamanho, quantidade, tipo, emissao, termo):
        
        self.limpar_entradas()
        self.limpar_info() 
        
        # --- Recebe dados ---
        self.nome = nome
        self.tamanho = tamanho
        self.tipo_vestimenta = tipo
        self.emissao = emissao
        self.termo_var = "SIM" if termo == 1 else "NÃO"

        # Converte quantidade para inteiro
        try:
            quantidade_int = int(quantidade)
        except ValueError:
            self.atualiza_faltadados_info()
            self.limpar_entradas()
            return

        # --- Caminhos das planilhas ---
        caminho_estoque = "Planilhas/estoque_roupas.xlsx"
        caminho_pedidos = "Planilhas/pedidos_registrados.xlsx"

        # --- Carrega estoque ---
        try:
            estoque_df = pd.read_excel(caminho_estoque)
        except FileNotFoundError:
            self.limpar_entradas()
            self.atualiza_faltaplanilha_info()
            return

        # --- Normaliza nomes das colunas para maiúsculas ---
        estoque_df.columns = [col.upper() for col in estoque_df.columns]

        # --- Verifica se colunas necessárias existem ---
        for col in ["TIPO", "TAMANHO", "QUANTIDADE"]:
            if col not in estoque_df.columns:
                self.limpar_entradas()
                self.atualiza_erro_info()
                return

        # --- Busca item no estoque ---
        item_estoque = estoque_df[
            (estoque_df["TIPO"] == self.tipo_vestimenta) & 
            (estoque_df["TAMANHO"] == self.tamanho)
        ]

        if item_estoque.empty:
            self.limpar_entradas()
            self.atualiza_erro_info()
            return

        if item_estoque.iloc[0]["QUANTIDADE"] < quantidade_int:
            self.atualiza_erro_info()
            self.limpar_entradas()
            self.atualiza_faltaroupa_info()
            return

        # --- Atualiza estoque ---
        estoque_df.loc[
            (estoque_df["TIPO"] == self.tipo_vestimenta) & 
            (estoque_df["TAMANHO"] == self.tamanho),
            "QUANTIDADE"
        ] -= quantidade_int
        estoque_df.to_excel(caminho_estoque, index=False)

        # --- Adiciona pedido ---
        novo_pedido = {
            "NOME COLABORADOR": self.nome,
            "TIPO DE VESTIMENTA": self.tipo_vestimenta,
            "TAMANHO": self.tamanho,
            "QUANTIDADE": quantidade_int,
            "DATA DO PEDIDO": self.emissao,
            "TERMO ASSINADO": self.termo_var
        }

        try:
            pedidos_df = pd.read_excel(caminho_pedidos)
        except FileNotFoundError:
            pedidos_df = pd.DataFrame(columns=[
                "NOME COLABORADOR", "TIPO DE VESTIMENTA", "TAMANHO",
                "QUANTIDADE", "DATA DO PEDIDO", "TERMO ASSINADO"
            ])

        pedidos_df = pd.concat([pedidos_df, pd.DataFrame([novo_pedido])], ignore_index=True)
        pedidos_df.to_excel(caminho_pedidos, index=False)

        print("Pedido registrado com sucesso!")
        self.limpar_entradas()
        self.atualiza_sucesso_info()

        
    def atualiza_sucesso_info(self):

        
        self.info_add.configure(state="normal")

        self.info_add.delete("0.0", "end")

        self.info_add._textbox.tag_configure("center", justify="center")
        
        self.info_add.insert("0.0", "PEDIDO REGISTRADO COM SUCESSO!", "center")
        
        self.info_add.tag_add("center", "0.0", "end")
        
        self.info_add.configure(state="disabled")
        
        
    def atualiza_erro_info(self):
        
        
        self.info_add.configure(state="normal")

        self.info_add.delete("0.0", "end")

        self.info_add._textbox.tag_configure("center", justify="center")
        
        self.info_add.insert("0.0", "ERRO AO REGISTRAR PEDIDO!", "center")
        
        self.info_add.tag_add("center", "0.0", "end")
        
        self.info_add.configure(state="disabled")
        
        
        
    def limpar_info(self):
        
        
        self.info_add.configure(state="normal")

        self.info_add.delete("0.0", "end")

        self.info_add._textbox.tag_configure("center", justify="center")
        
        self.info_add.insert("0.0", "", "center")
        
        self.info_add.tag_add("center", "0.0", "end")
        
        self.info_add.configure(state="disabled")
        
        
    def atualiza_faltaroupa_info(self):
        
        
        self.info_add.configure(state="normal")

        self.info_add.delete("0.0", "end")

        self.info_add._textbox.tag_configure("center", justify="center")
        
        self.info_add.insert("0.0", "ROUPAS INSUFICIENTES NO ESTOQUE!", "center")
        
        self.info_add.tag_add("center", "0.0", "end")
        
        self.info_add.configure(state="disabled")
        
        
        
    def atualiza_faltaplanilha_info(self):
        
        
        self.info_add.configure(state="normal")

        self.info_add.delete("0.0", "end")

        self.info_add._textbox.tag_configure("center", justify="center")
        
        self.info_add.insert("0.0", "PLANILHA DE ESTOQUE NÃO ENCONTRADA!", "center")
        
        self.info_add.tag_add("center", "0.0", "end")
        
        self.info_add.configure(state="disabled")
        
        
        
    def atualiza_faltadados_info(self):
        
        
        self.info_add.configure(state="normal")

        self.info_add.delete("0.0", "end")

        self.info_add._textbox.tag_configure("center", justify="center")
        
        self.info_add.insert("0.0", "INSIRA OS DADOS CORRETAMENTE!", "center")
        
        self.info_add.tag_add("center", "0.0", "end")
        
        self.info_add.configure(state="disabled")
        
        
        
        
        
    
                