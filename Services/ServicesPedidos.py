import pandas as pd

class ServicesPedidos:
    
    def __init__(self):
        self.arquivo = "Planilhas/pedidos_registrados.xlsx"

    def carregar_planilha(self):

        df = pd.read_excel(self.arquivo)

        dados = []

        for _, row in df.iterrows():
            dados.append((
                row["NOME COLABORADOR"],
                row["TIPO DE VESTIMENTA"],
                row["TAMANHO"],
                row["QUANTIDADE"],
                row["DATA DO PEDIDO"],
                row["TERMO ASSINADO"]
            ))

        return dados

    def atualizar_quantidade(self, nome, tipo_de_vestimenta, tamanho, quantidade, data_do_pedido, termo_assinado):

        import pandas as pd
    
        df = pd.read_excel(self.arquivo)
    

        df.columns = df.columns.str.strip().str.upper()
    
        if tipo_de_vestimenta == "Masculina":
            tipo_de_vestimenta = "MASCULINO"
        else:
            tipo_de_vestimenta = "FEMININO"
    
        tamanho = tamanho.upper()
    
        linha = (df["TIPO DE VESTIMENTA"] == tipo_de_vestimenta) & (df["TAMANHO"] == tamanho)
    
        if linha.any():
            df.loc[linha, "QUANTIDADE"] = int(quantidade)
        else:
    
         df.to_excel(self.arquivo, index=False)

    def open_Frontend(self, tela_atual):
        tela_atual.destroy()  
        from Interface.Frontend import Application
        app = Application()
        app.mainloop()

    
        