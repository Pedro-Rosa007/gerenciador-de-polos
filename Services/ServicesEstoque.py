import pandas as pd


class ServicesEstoque:

    def __init__(self):
        self.arquivo = "Planilhas/estoque_roupas.xlsx"

    def carregar_planilha(self):

        df = pd.read_excel(self.arquivo)

        dados = []

        for _, row in df.iterrows():
            dados.append((
                row["TIPO"],
                row["TAMANHO"],
                row["QUANTIDADE"]
            ))

        return dados

    def atualizar_quantidade(self, tipo, tamanho, quantidade):

        import pandas as pd
    
        df = pd.read_excel(self.arquivo)
    

        df.columns = df.columns.str.strip().str.upper()
    
        if tipo == "Masculina":
            tipo = "MASCULINO"
        else:
            tipo = "FEMININO"
    
        tamanho = tamanho.upper()
    
        linha = (df["TIPO"] == tipo) & (df["TAMANHO"] == tamanho)
    
        if linha.any():
            df.loc[linha, "QUANTIDADE"] = int(quantidade)
        else:
    
         df.to_excel(self.arquivo, index=False)
        
    def open_Frontend(self, janela):

        janela.destroy()
        from Interface.Frontend import Application
        app = Application()
        app.mainloop()
        
    