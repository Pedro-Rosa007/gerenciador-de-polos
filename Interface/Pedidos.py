import customtkinter as ctk
from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkCheckBox, END
from Services.ServicesPedidos import ServicesPedidos
from tkinter import ttk


class pedidos(ctk.CTk):

    def __init__(self):
        super().__init__()
        
        self.iconbitmap("Arts/icon.ico")

        self.service = ServicesPedidos()

        self.title("Tabela de Pedidos")
        ctk.set_appearance_mode("light")
        self.buildapp_pedido()

    def buildapp_pedido(self):
        self.tela_inicial_start_new()
        self.frame_principal()
        self.labels()
        self.bottons()
        self.treeview()
        self.atualizar_treeview()


    def center_window(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        self.geometry(f"{width}x{height}+{x}+{y}")

    def tela_inicial_start_new(self):
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
            self.framemain,
            text ="TABELA DE PEDIDOS",
            font=("SEGOE IU", 45, "bold"),
            bg_color="#f0f0f0",
            text_color="black"
        )
        self.title.place(relx=0.3,rely=0.1)
        
    
    
    
    def treeview(self):

        self.tree = ttk.Treeview(
            self.framemain,
            columns=("NOME DO COLABORADOR", "TIPO DE VESTIMENTA", "TAMANHO", "QUANTIDADE", "DATA DO PEDIDO", "TERMO ASSINADO"),
            show="headings"
        )
    
        self.tree.heading("NOME DO COLABORADOR", text="NOME DO COLABORADOR", anchor="center")
        self.tree.heading("TIPO DE VESTIMENTA", text="TIPO DE VESTIMENTA", anchor="center")
        self.tree.heading("TAMANHO", text="TAMANHO", anchor="center")
        self.tree.heading("QUANTIDADE", text="QUANTIDADE", anchor="center")
        self.tree.heading("DATA DO PEDIDO", text="DATA DO PEDIDO", anchor="center")
        self.tree.heading("TERMO ASSINADO", text="TERMO ASSINADO", anchor="center")
    
        self.tree.column("NOME DO COLABORADOR", width=80, anchor="center")
        self.tree.column("TIPO DE VESTIMENTA", width=80, anchor="center")
        self.tree.column("TAMANHO", width=80, anchor="center")
        self.tree.column("QUANTIDADE", width=80, anchor="center")
        self.tree.column("DATA DO PEDIDO", width=80, anchor="center")
        self.tree.column("TERMO ASSINADO", width=80, anchor="center")
    

        self.scrollbar = ttk.Scrollbar(
            self.framemain,
            orient="vertical",
            command=self.tree.yview
        )
    
        self.tree.configure(yscrollcommand=self.scrollbar.set)
    
        self.tree.place(relx=0.1, rely=0.24, relwidth=0.7, relheight=0.7)
    
        self.scrollbar.place(relx=0.8, rely=0.24, relheight=0.7)





    def carregar_treeview(self, dados):

        for item in dados:
            self.tree.insert("", "end", values=item)




    def atualizar_treeview(self):

        self.tree.delete(*self.tree.get_children())

        dados = self.service.carregar_planilha()

        self.carregar_treeview(dados)


        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    








    def bottons(self):
        

        self.botao_voltar = CTkButton(
            self.framemain,
            text= "VOLTAR",
            text_color="White",
            corner_radius= 20,
            border_width=2,
            fg_color="#777777",
            border_color="#5e5e5e",
            bg_color="transparent",
            hover_color="#535353",
            font=("SEGOE IU", 20, "bold"),
            command=lambda: self.service.open_Frontend(self)
        )
        self.botao_voltar.place(relx=0.85, rely = 0.85, relheight = 0.07, relwidth = 0.11)