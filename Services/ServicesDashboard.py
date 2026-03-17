class ServicesDashboard:

    def open_Frontend(self, tela_atual):
        tela_atual.destroy()  
        from Interface.Frontend import Application
        app = Application()
        app.mainloop()