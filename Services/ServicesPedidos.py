import pandas as pd


class ServicesPedidos:
    
    
    def __init__(self):

        self.arquivo = "Planilhas/pedidos_registrados.xlsx"




    def carregar_planilha(self):

        try:
            df = pd.read_excel(self.arquivo)
        except FileNotFoundError:
            return []
        

        df.columns = df.columns.str.strip().str.upper()
        if "ENTREGA" not in df.columns:
            df["ENTREGA"] = ""
        dados = list(df.itertuples(index=False, name=None))

        return dados

    def atualizar_quantidade(self, nome, tipo_de_vestimenta, tamanho, quantidade, data_do_pedido):

        try:
            df = pd.read_excel(self.arquivo)
        except FileNotFoundError:
            print("Arquivo de pedidos não encontrado.")
            return
        

        df.columns = df.columns.str.strip().str.upper()
        if "ENTREGA" not in df.columns:
            df["ENTREGA"] = ""


        nome = nome.strip().upper()
        tipo_de_vestimenta = tipo_de_vestimenta.strip().upper()
        tamanho = tamanho.strip().upper()
        try:
            quantidade = int(quantidade)


        except ValueError:
            print("Quantidade inválida.")
            return
    
        df["NOME COLABORADOR"] = df["NOME COLABORADOR"].astype(str).str.strip().str.upper()
        df["TIPO DE VESTIMENTA"] = df["TIPO DE VESTIMENTA"].astype(str).str.strip().str.upper()
        df["TAMANHO"] = df["TAMANHO"].astype(str).str.strip().str.upper()
    

        if tipo_de_vestimenta.startswith("MASC"):
            tipo_de_vestimenta = "MASCULINO"
        else:
            tipo_de_vestimenta = "FEMININO"
    
        linha = (
            (df["NOME COLABORADOR"] == nome) &
            (df["TIPO DE VESTIMENTA"] == tipo_de_vestimenta) &
            (df["TAMANHO"] == tamanho) &
            (df["DATA DO PEDIDO"] == data_do_pedido)
        )
    
        if linha.any():
            df.loc[linha, "QUANTIDADE"] = quantidade
        else:
            print("Registro não encontrado para atualização.")
        df.to_excel(self.arquivo, index=False)





    def open_Frontend(self, tela_atual):
        tela_atual.destroy()  
        from Interface.Frontend import Application
        app = Application()
        app.mainloop()

    
        