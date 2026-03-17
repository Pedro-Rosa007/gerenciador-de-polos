import customtkinter as ctk
from customtkinter import CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkComboBox, CTkCheckBox, CTkTextbox,END
from tkcalendar import DateEntry
from Services.ServicesNewPedido import ServicesNewPedidos
import tkinter as tk
import pandas as pd


class novopedido(ctk.CTk):

    def __init__(self):
        super().__init__()
        
        self.iconbitmap("Arts/icon.ico")

        self.service = ServicesNewPedidos()
    
        self.title("Novo Pedido")
        ctk.set_appearance_mode("light")
    
        self.buildapp_pedido()
    
    
        self.service.info_add = self.info_add
        self.service.entrie_nome = self.entrie_nome
        self.service.entrie_quantidade = self.entrie_quantidade
        self.service.var_termo = self.var_termo

    def buildapp_pedido(self):
        self.tela_inicial_start_new()
        self.frame_principal()
        self.labels()
        self.bottons()
        self.entries()
        


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

        self.label_title = CTkLabel(
            self.framemain,
            text ="ADICIONAR NOVOS PEDIDOS",
            font=("SEGOE IU", 45, "bold"),
            bg_color="#f0f0f0",
            text_color="black"
        )
        self.label_title.place(relx=0.22,rely=0.1)


        self.label_nome_colaborador = CTkLabel(
            self.framemain,
            text="NOME DO COLABORADOR",
            text_color="black",
            font=("Segoe UI", 12, "bold"),
            bg_color="transparent"
        )
        self.label_nome_colaborador.place(relx = 0.17, rely = 0.275)

        self.label_data_emissao = CTkLabel(
            self.framemain,
            text="DATA DO PEDIDO",
            text_color="black",
            font=("Segoe UI", 12, "bold"),
            bg_color="transparent"
        )
        self.label_data_emissao.place(relx = 0.19, rely = 0.395)


        self.label_tamanho = CTkLabel(
            self.framemain,
            text="TAMANHO",
            text_color="black",
            font=("Segoe UI", 12, "bold"),
            bg_color="transparent"
        )
        self.label_tamanho.place(relx = 0.21, rely = 0.51)

        self.label_quantidade = CTkLabel(
            self.framemain,
            text="QUANTIDADE",
            text_color="black",
            font=("Segoe UI", 12, "bold"),
            bg_color="transparent"
        )
        self.label_quantidade.place(relx = 0.2, rely = 0.63)


        self.label_tipo= CTkLabel(
            self.framemain,
            text="TIPO DE VESTIMENTA",
            text_color="black",
            font=("Segoe UI", 12, "bold"),
            bg_color="transparent"
        )
        self.label_tipo.place(relx = 0.185, rely = 0.75)



        



        







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



        self.gerar_pedido = CTkButton(
            self.framemain,
            text= "GERAR PEDIDO",
            text_color="White",
            corner_radius= 20,
            border_width=2,
            fg_color="#dedede",
            border_color="#e0e0e0",
            bg_color="transparent",
            hover_color="#b6b6b6",
            font=("SEGOE IU", 20, "bold"),
            command=lambda: self.service.inserir_planilha(
        nome=self.entrie_nome.get().strip(),
        tamanho=self.combo_tamanho.get(),
        quantidade=self.entrie_quantidade.get().strip(),
        tipo=self.combo_tipo.get(),
        emissao=self.entrie_data.get(),
        termo=self.var_termo.get()
    )
        )
        self.gerar_pedido.place(relx=0.6, rely = 0.45, relheight = 0.07, relwidth = 0.25)


        self.info_add = CTkTextbox(
            self.framemain,
            font=("SEGOE IU", 12, "bold"),   
            fg_color="#d6d6d6",
            text_color="black",
            corner_radius=10,
            border_color="#aaaaaa",
            border_width= 2,
            
        )
        self.info_add.configure(state="disabled")
        self.info_add.place(relx=0.6, rely = 0.54, relheight = 0.07, relwidth = 0.25)
        
        
        
        self.limpar_info = CTkButton(
            self.framemain,
            text= "LIMPAR STATUS",
            text_color="White",
            corner_radius= 20,
            border_width=2,
            fg_color="#dedede",
            border_color="#e0e0e0",
            bg_color="transparent",
            hover_color="#b6b6b6",
            font=("SEGOE IU", 20, "bold"),
            command= self.service.limpar_info
           )
        self.limpar_info.place(relx=0.6, rely = 0.635, relheight = 0.07, relwidth = 0.25)
        
















    def entries(self):

        self.entrie_nome = CTkEntry(
            self.framemain,
            bg_color="transparent",
            fg_color="#f1f1f1",
            border_color="#d6d6d6",
            border_width= 2,
            corner_radius= 20,
            text_color="#aaaaaa",
            placeholder_text="Insira o Nome",
            placeholder_text_color="#aaaaaa",
            justify = "center"
        )
        self.entrie_nome.place(relx = 0.12, rely = 0.32, relheight = 0.06, relwidth = 0.25)

        self.entrie_data = DateEntry(
            self.framemain,
            date_pattern="dd/mm/yyyy",
            background="#f1f1f1",
            foreground="black",
            borderwidth=2,
            justify = "center"
        )
        self.entrie_data.place(relx=0.15, rely=0.44, relheight=0.06, relwidth=0.18)



        self.combo_tamanho = CTkComboBox(

            self.framemain,
            values=["PP", "P", "M", "G", "GG", "XG", "XGG"],
            fg_color="#f1f1f1",     
            border_color="#d6d6d6",
            border_width=2,
            corner_radius=20,
            text_color="#555555",     
            button_color="#d6d6d6",
            button_hover_color="#c5c5c5",
            dropdown_fg_color="white",
            dropdown_text_color="black",
            justify = "center"
       )
        self.combo_tamanho.place(relx=0.15, rely=0.56, relheight=0.06, relwidth=0.18)


        self.entrie_quantidade = CTkEntry(
            self.framemain,
            bg_color="transparent",
            fg_color="#f1f1f1",
            border_color="#d6d6d6",
            border_width= 2,
            corner_radius= 20,
            text_color="#aaaaaa",
            placeholder_text="Insira a Quantidade",
            placeholder_text_color="#aaaaaa",
            justify = "center"
        )
        self.entrie_quantidade.place(relx = 0.12, rely = 0.67, relheight = 0.06, relwidth = 0.25)


        self.var_termo = tk.IntVar()
        self.check_assinatura = CTkCheckBox(
            self.framemain,
            fg_color="#aaaaaa",
            bg_color="transparent",
            border_color="#aaaaaa",
            border_width=2,    
            hover_color="#646464",
            text="TERMO ASSINADO",
            text_color="black",
            font=("SEGOE IU", 12, "bold"),
            variable=self.var_termo
        )
        self.check_assinatura.place(relx = 0.15, rely = 0.88)

        self.combo_tipo = CTkComboBox(

            self.framemain,
            values=["MASCULINO", "FEMININO"],
            fg_color="#f1f1f1",     
            border_color="#d6d6d6",
            border_width=2,
            corner_radius=20,
            text_color="#555555",     
            button_color="#d6d6d6",
            button_hover_color="#c5c5c5",
            dropdown_fg_color="white",
            dropdown_text_color="black",
            justify = "center"
       )
        self.combo_tipo.place(relx=0.12, rely=0.8, relheight=0.06, relwidth=0.25)

        



















if __name__ == "__main__":
    app = novopedido()
    app.mainloop()