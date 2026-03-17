import customtkinter as ctk
from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkCheckBox, END
from Services.ServicesMain import MainServices
from Services.ServicesEstoque import ServicesEstoque
from Services.ServicesDashboard import ServicesDashboard

from Services.ServicesPedidos import ServicesPedidos


class Application(ctk.CTk):

    

    def __init__(self):
        super().__init__()
        
        self.iconbitmap("Arts/icon.ico")

        self.service = MainServices()
        self.service_estoque = ServicesEstoque()
        self.service_dashboarde = ServicesDashboard()
        self.service_pedidos = ServicesPedidos()

        self.title("Gerenciamento de Pedidos")
        ctk.set_appearance_mode("light") 
        self.buildapp()



    def buildapp(self):

        self.tela_inicial_start()
        self.frame_principal()
        self.labels()
        self.bottons()


        
    def center_window(self, width, height):
      
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        self.geometry(f"{width}x{height}+{x}+{y}")
        


    def tela_inicial_start(self):

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
            text ="GERENCIAMENTO DE POLOS",
            font=("SEGOE IU", 45, "bold"),
            bg_color="#f0f0f0",
            text_color="black"
        )
        self.title.place(relx=0.22,rely=0.1)




    def bottons(self):
        

        self.botao_add_pedido = CTkButton(
            self.framemain,
            text= "NOVO PEDIDO",
            text_color="White",
            corner_radius= 20,
            border_width=2,
            fg_color="#dedede",
            border_color="#e0e0e0",
            bg_color="transparent",
            hover_color="#b6b6b6",
            font=("SEGOE IU", 20, "bold"),
            command= lambda: self.service.open_new_pedidos(self)
        )
        self.botao_add_pedido.place(relx=0.35, rely = 0.3, relheight = 0.1, relwidth = 0.3)


        self.botao_ver_estoque = CTkButton(
            self.framemain,
            text= "ESTOQUE",
            text_color="White",
            corner_radius= 20,
            border_width=2,
            fg_color="#dedede",
            border_color="#e0e0e0",
            bg_color="transparent",
            hover_color="#b6b6b6",
            font=("SEGOE IU", 20, "bold"),
            command= lambda: self.service.open_Estoque(self)
        )
        self.botao_ver_estoque.place(relx=0.35, rely = 0.42, relheight = 0.1, relwidth = 0.3)


        self.botao_dashboard = CTkButton(
            self.framemain,
            text= "DASHBOARD",
            text_color="White",
            corner_radius= 20,
            border_width=2,
            fg_color="#dedede",
            border_color="#e0e0e0",
            bg_color="transparent",
            hover_color="#b6b6b6",
            font=("SEGOE IU", 20, "bold"),
            command= lambda: self.service.open_Dashboard(self)
        )
        self.botao_dashboard.place(relx=0.35, rely = 0.54, relheight = 0.1, relwidth = 0.3)



        self.botao_ver_pedidos = CTkButton(
            self.framemain,
            text= "PEDIDOS",
            text_color="White",
            corner_radius= 20,
            border_width=2,
            fg_color="#dedede",
            border_color="#e0e0e0",
            bg_color="transparent",
            hover_color="#b6b6b6",
            font=("SEGOE IU", 20, "bold"),
            command= lambda: self.service.open_Pedidos(self)
        )
        self.botao_ver_pedidos.place(relx=0.35, rely = 0.66, relheight = 0.1, relwidth = 0.3)

       





    










