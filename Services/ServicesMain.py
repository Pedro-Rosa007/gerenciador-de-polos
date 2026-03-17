

class MainServices:

    def open_new_pedidos(self, tela_atual):

        tela_atual.destroy() 
        from Interface.NovoPedido import novopedido
        app = novopedido()
        app.mainloop()

    def open_Estoque(self, tela_atual):
        tela_atual.destroy()  
        from Interface.Estoque import estoque
        app = estoque()
        app.mainloop()

    def open_Dashboard(self, tela_atual):
        tela_atual.destroy()  
        from Interface.Dashboard import dashboard
        app = dashboard()
        app.mainloop()


    def open_Pedidos(self, tela_atual):
        tela_atual.destroy()  
        from Interface.Pedidos import pedidos
        app = pedidos()
        app.mainloop()

    