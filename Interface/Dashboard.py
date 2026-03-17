import customtkinter as ctk
from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkCheckBox, END
from Services.ServicesDashboard import ServicesDashboard


class dashboard(ctk.CTk):

    def __init__(self):
        super().__init__()
        
        self.iconbitmap("Arts/icon.ico")

        self.service = ServicesDashboard()

        self.title("Dashboard")
        ctk.set_appearance_mode("light")
        self.buildapp_dashboard()

    def buildapp_dashboard(self):
        self.tela_inicial_start_dashboard()
        self.frame_principal()
        self.labels()
        self.bottons()


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
            self.framemain,
            text ="DASHBOARD DE VENDAS",
            font=("SEGOE IU", 45, "bold"),
            bg_color="#f0f0f0",
            text_color="black"
        )
        self.title.place(relx=0.25,rely=0.1)




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