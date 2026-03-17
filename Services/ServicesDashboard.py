import pandas as pd

class ServicesDashboard:

    def __init__(self, master=None):
        super().__init__()
        self.master = master

    def normalizar_data(self, data):
        """
        Converte datas do formato dd/mm/yyyy ou outros para yyyy-mm-dd
        Retorna string ou mantém original se não conseguir converter.
        """
        try:
            dt = pd.to_datetime(data, dayfirst=True, errors="coerce")
            if pd.isna(dt):
                return str(data)
            return dt.strftime("%Y-%m-%d")
        except:
            return str(data)

    def carregar_planilha(self):
        caminho = "Planilhas/pedidos_registrados.xlsx"
        try:
            df = pd.read_excel(caminho)
        except:
            return []  

        df.columns = [col.upper() for col in df.columns]

        dados = []
        for _, row in df.iterrows():
            dados.append((
                row["NOME COLABORADOR"],
                row.get("TIPO", ""),
                row.get("TAMANHO", ""),
                row.get("QUANTIDADE", ""),
                self.normalizar_data(row["DATA DO PEDIDO"]),
                row["TERMO ASSINADO"],
                row.get("ENTREGA", "")
            ))
        return dados

    def atualizar_entrega(self, nome, data):
        caminho = "Planilhas/pedidos_registrados.xlsx"
        try:
            df = pd.read_excel(caminho)
        except:
            from Modals.ModaisPlanilha import modals
            app = modals()
            app.mainloop()
            return False, 

        df.columns = [col.upper() for col in df.columns]

        # Normaliza todas as datas da planilha
        df["DATA DO PEDIDO"] = pd.to_datetime(df["DATA DO PEDIDO"], dayfirst=True, errors="coerce").dt.strftime("%Y-%m-%d")
        data = self.normalizar_data(data)

        df["NOME COLABORADOR"] = df["NOME COLABORADOR"].astype(str).str.strip()
        nome = str(nome).strip()

        filtro = (
            (df["NOME COLABORADOR"] == nome) &
            (df["DATA DO PEDIDO"] == data)
        )

        if not filtro.any():
            from Modals.ModaisErros import modals
            app = modals()
            app.mainloop()
            return False,

        termo = df.loc[filtro, "TERMO ASSINADO"].values[0]
        if str(termo).strip().upper() == "NÃO":
            from Modals.ModaisErros import modals
            app = modals()
            app.mainloop()
            return False, 

        df.loc[filtro, "ENTREGA"] = "SIM"
        df.to_excel(caminho, index=False)

        from Modals.ModaisSucesso import modals
        app = modals()
        app.mainloop()
        return True, 

    def assinar_termo(self, nome, data):
        caminho = "Planilhas/pedidos_registrados.xlsx"
        try:
            df = pd.read_excel(caminho)
        except:
            from Modals.ModaisPlanilha import modals
            app = modals()
            app.mainloop()
            return False, 

        df.columns = [col.upper() for col in df.columns]

        # Normaliza todas as datas da planilha
        df["DATA DO PEDIDO"] = pd.to_datetime(df["DATA DO PEDIDO"], dayfirst=True, errors="coerce").dt.strftime("%Y-%m-%d")
        data = self.normalizar_data(data)

        df["NOME COLABORADOR"] = df["NOME COLABORADOR"].astype(str).str.strip()
        nome = str(nome).strip()

        filtro = (
            (df["NOME COLABORADOR"] == nome) &
            (df["DATA DO PEDIDO"] == data)
        )

        if not filtro.any():
            from Modals.ModaisRegistro import modals
            app = modals()
            app.mainloop()
            return False, 

        df.loc[filtro, "TERMO ASSINADO"] = "SIM"
        df.to_excel(caminho, index=False)

        from Modals.ModaisTermo import modals
        app = modals()
        app.mainloop()
        return True, 

    def open_Frontend(self, tela_atual):
        tela_atual.destroy()
        from Interface.Frontend import Application
        app = Application()
        app.mainloop()