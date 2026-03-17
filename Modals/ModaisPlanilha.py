import customtkinter as ctk
from customtkinter import CTkButton, CTkLabel, CTkFrame

class modals(ctk.CTk):
    def __init__(self, master=None):
        super().__init__(master)

        self.master = master 
        self.builder_modal()

    def builder_modal(self):

        self.tela_modal()
        self.modern_frame()
        self.botao_sair()
        self.texto_label()

    def tela_modal(self):

        height = 150
        width = 300
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.configure(fg_color = "#ff00bf")
        self.attributes("-transparentcolor", "#ff00bf")
        self.overrideredirect(True) 

    def modern_frame(self):

        self.framemain = CTkFrame(
            self,
            fg_color="white",
            bg_color="transparent",
            corner_radius= 15,
            border_color="#ececec",
            border_width= 4
        )
        self.framemain.place(relx = 0.05, rely = 0.05, relwidth = 0.9, relheight = 0.9)

    def botao_sair(self):

        self.sair = CTkButton(
            self.framemain,
            text="FECHAR",
            text_color="white",
            fg_color="#00e6e6",
            bg_color="transparent",
            corner_radius=27,
            font=("SEGOE UI", 12, "bold"),
            command=self.destroy
        )
        self.sair.place(relx=0.1, rely=0.7, relwidth=0.8, relheight=0.2)


    def texto_label(self):

        self.label = CTkLabel(
            self.framemain,
            text= """ERRO! 
PLANILHA NÃO ENCONTRADO!""",
            text_color="black",
            bg_color="transparent",
            font=("SEGOE UI", 12, "bold"),
            wraplength=280
        )
        self.label.place(relx=0.18, rely=0.34)

if __name__ == "__main__":
    app = modals()
    app.mainloop()