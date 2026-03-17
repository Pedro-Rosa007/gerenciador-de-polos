import customtkinter as ctk
from customtkinter import CTkFrame, CTkLabel, CTkButton
from tkinter import ttk
from Services.ServicesDashboard import ServicesDashboard
from Modals.ModaisErros import modals
import os

import sys




class dashboard(ctk.CTk):

    def __init__(self):
        super().__init__()
        
        self.iconbitmap(self.resource_path("Arts/icon.ico"))
        self.service = ServicesDashboard(self)
        self.title("ENTREGAS")
        ctk.set_appearance_mode("light")
        self.buildapp_dashboard()


    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except AttributeError:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def buildapp_dashboard(self):

        self.tela_inicial_start_dashboard()
        self.frame_principal()
        self.labels()
        self.treeview()
        self.bottons()
        self.atualizar_treeview()
        

    def center_window(self, width, height):

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        self.geometry(f"{width}x{height}+{x}+{y}")

    def tela_inicial_start_dashboard(self):

        self.width = 1200
        self.height = 700
        self.center_window(self.width, self.height)
        self.configure(fg_color="#d3d3d3")
        self.resizable(False, False)

    def frame_principal(self):

        self.framemain = CTkFrame(
            self,
            bg_color= "transparent",
            fg_color= "white",
            corner_radius=35,
            border_color="#f0f0f0",
            border_width= 22
        )
        self.framemain.place(relx = 0.05, rely = 0.05, relheight = 0.9, relwidth = 0.9)

        self.frametitulo = CTkFrame(
            self.framemain,
            bg_color="transparent",
            fg_color="#f0f0f0",
            border_color="#e9e9e9",
            border_width= 5,
            corner_radius= 20
        )
        self.frametitulo.place(relx = 0.05, rely = 0.07, relheight = 0.15, relwidth = 0.9)

    def labels(self):

        self.title = CTkLabel(
            self.frametitulo,
            text="ENTREGAS DE POLOS",
            font=("SEGOE IU", 40, "bold"),
            text_color="black"
        )
        self.title.place(relx=0.3, rely=0.3)

    


    def treeview(self):

        self.tree = ttk.Treeview(
            self.framemain,
            columns=("NOME", "TIPO", "TAMANHO", "QUANTIDADE", "DATA", "TERMO", "ENTREGA"),
            show="headings"
        )

        for col in ("NOME", "TIPO", "TAMANHO", "QUANTIDADE", "DATA", "TERMO", "ENTREGA"):
            self.tree.heading(col, text=col, anchor="center")
            self.tree.column(col, width=120, anchor="center")
        self.tree.place(relx=0.1, rely=0.27, relwidth=0.8, relheight=0.6)
        self.scrollbar = ttk.Scrollbar(
            self.framemain,
            orient="vertical",
            command=self.tree.yview
        )
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.place(relx=0.9, rely=0.27, relheight=0.6)

    def carregar_treeview(self, dados):

        for item in dados:
            self.tree.insert("", "end", values=item)

    def atualizar_treeview(self):

        if hasattr(self, 'tree') and self.tree.winfo_exists():
            self.tree.delete(*self.tree.get_children())
            for item in self.tree.get_children():
               self.tree.delete(item)
            dados = self.service.carregar_planilha()
            for linha in dados:
                self.tree.insert("", "end", values=linha)
    
    
    def marcar_entregue(self):

        selecionado = self.tree.selection()
        if not selecionado:
            print("Selecione um item")
            return
        valores = self.tree.item(selecionado[0], "values")
        nome = valores[0]
        data = valores[4]
        sucesso = self.service.atualizar_entrega(nome, data)
        if sucesso:
            self.atualizar_treeview()


    def bottons(self):

        self.botao_entregar = CTkButton(
            self.framemain,
            text="MARCAR COMO ENTREGUE",
            fg_color="#14eb00",
            border_color="#21c500",
            bg_color="transparent",
            hover_color="#2ab400",
            text_color="white",
            font=("SEGOE IU", 14, "bold"),
            command=self.marcar_entregue
        )
        self.botao_entregar.place(relx=0.6, rely=0.88, relwidth=0.2, relheight = 0.07)

        self.botao_voltar = CTkButton(
            self.framemain,
            text="VOLTAR",
            fg_color="#dedede",
            border_color="#e0e0e0",
            bg_color="transparent",
            hover_color="#b6b6b6",
            text_color="white",
            font=("SEGOE IU", 14, "bold"),
            command=lambda: self.service.open_Frontend(self)
        )
        self.botao_voltar.place(relx=0.82, rely=0.88, relwidth=0.12, relheight = 0.07)

        self.botao_termo = CTkButton(
            self.framemain,
            text="ASSINAR TERMO",
            fg_color="#ebe700",
            hover_color="#c7ca00",
            text_color="white",
            font=("SEGOE IU", 14, "bold"),
            command=self.assinar_termo
        )
        self.botao_termo.place(relx=0.39, rely=0.88, relwidth=0.2, relheight=0.07)

        self.btn_atualizar = ctk.CTkButton(
            self.framemain, 
            bg_color= "transparent",
            fg_color="#00b8d8",
            hover_color="#008db8",
            text_color="white",
            font=("SEGOE IU", 14, "bold"),
            text="ATUALIZAR DADOS",
            command=self.atualizar_treeview)
        
        self.btn_atualizar.place(relx=0.18, rely=0.88, relwidth=0.2, relheight=0.07)


    def assinar_termo(self):

        selecionado = self.tree.selection()
        if not selecionado:
            print("Selecione um item")
            return
        valores = self.tree.item(selecionado[0], "values")
        nome = valores[0]
        data = valores[4]
        sucesso = self.service.assinar_termo(nome, data)
        if sucesso:
            self.atualizar_treeview()



    def voltar_frontend(self):
        self.destroy()
        from Services.ServicesMain import ServicesMain
        ServicesMain().open_Frontend()