import customtkinter as ctk
from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkComboBox, CTkEntry, END
from tkinter import ttk
from Services.ServicesEstoque import ServicesEstoque
import os
import sys


class estoque(ctk.CTk):

    def __init__(self):
        super().__init__()
        
        self.iconbitmap(self.resource_path("Arts/icon.ico"))
        self.service = ServicesEstoque()
        ctk.set_appearance_mode("light")
        self.title("Estoque de Polos")
        self.buildapp()

    def buildapp(self):

        self.tela()
        self.frame_principal()
        self.labels()
        self.controles_estoque()
        self.treeview()
        dados = self.service.carregar_planilha()
        self.carregar_treeview(dados)

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except AttributeError:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def tela(self):

        width = 1200
        height = 700
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width/2) - (width/2))
        y = int((screen_height/2) - (height/2))
        self.geometry(f"{width}x{height}+{x}+{y}")
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
            self.framemain,
            text ="ESTOQUE DE POLOS",
            font=("SEGOE IU", 45, "bold"),
            bg_color="#f0f0f0",
            text_color="black"
        )
        self.title.place(relx=0.3,rely=0.1)


    def controles_estoque(self):

        self.frame_controle = CTkFrame(self.framemain, fg_color="#f7f7f7")
        self.frame_controle.place(relx=0.037, rely=0.265, relwidth=0.22, relheight=0.60)

        self.label_tipo = CTkLabel(self.frame_controle, text="Tipo")
        self.label_tipo.pack(pady=(15,5))
    
        self.combo_tipo = CTkComboBox(
            self.frame_controle,
            values=["Masculina", "Feminina"]
        )
        self.combo_tipo.pack(pady=5, padx=10)
    
        self.label_tamanho = CTkLabel(
            self.frame_controle, 
            text="Tamanho"
            )
        self.label_tamanho.pack(pady=(15,5))
    
        self.combo_tamanho = CTkComboBox(
            self.frame_controle,
            values=["PP", "P", "M", "G", "GG", "XG", "XGG"]
        )
        self.combo_tamanho.pack(pady=5, padx=10)
    
        self.label_qtd = CTkLabel(
            self.frame_controle, 
            text="Nova quantidade Total"
            )
        self.label_qtd.pack(pady=(14,5))
    
        self.entry_quantidade = CTkEntry(
            self.frame_controle,
            placeholder_text="Quantidade",
            justify = "center"
        )
        self.entry_quantidade.pack(pady=5, padx=10)

        self.btn_enviar = CTkButton(
            self.frame_controle,
            text="ENVIAR PARA TABELA",
            text_color="White",
            corner_radius= 20,
            border_width=2,
            fg_color="#00cfeb",
            border_color="#00c0da",
            bg_color="transparent",
            hover_color="#008fb3",
            font=("SEGOE IU", 14, "bold"),
            command=self.enviar_dados
        )
        self.btn_enviar.pack(pady=10, padx=10, fill="x")
        
        
        self.btn_voltar = CTkButton(
            self.frame_controle,
            text="VOLTAR",
            text_color="White",
            corner_radius= 20,
            border_width=2,
            fg_color="#dedede",
            border_color="#e0e0e0",
            bg_color="transparent",
            hover_color="#b6b6b6",
            font=("SEGOE IU", 14, "bold"),
            command=lambda: self.service.open_Frontend(self)
        )
        self.btn_voltar.pack(pady=10, padx=10, fill="x")
        

    def treeview(self):

        self.tree = ttk.Treeview(
            self.framemain,
            columns=("tipo", "tamanho", "quantidade"),
            show="headings"
        )
        self.tree.heading("tipo", text="TIPO", anchor="center")
        self.tree.heading("tamanho", text="TAMANHO", anchor="center")
        self.tree.heading("quantidade", text="QUANTIDADE", anchor="center")
        self.tree.column("tipo", width=150, anchor="center")
        self.tree.column("tamanho", width=150, anchor="center")
        self.tree.column("quantidade", width=150, anchor="center")
        self.tree.place(relx=0.28, rely=0.25, relwidth=0.67, relheight=0.65)

    def carregar_treeview(self, dados):

        for item in dados:
            self.tree.insert("", "end", values=item)

    def atualizar_treeview(self):

        self.tree.delete(*self.tree.get_children())
        dados = self.service.carregar_planilha()
        self.carregar_treeview(dados)

    def atualizar_quantidade(self):

        tipo = self.combo_tipo.get()
        tamanho = self.combo_tamanho.get()
        quantidade = self.entry_quantidade.get()
        self.service.atualizar_quantidade(tipo, tamanho, quantidade)
        self.atualizar_treeview()
        
    def enviar_dados(self):

    
        tipo = self.combo_tipo.get()
        tamanho = self.combo_tamanho.get()
        quantidade = self.entry_quantidade.get()
        self.service.atualizar_quantidade(tipo, tamanho, quantidade)
        self.atualizar_treeview()
        self.entry_quantidade.delete(0, END)