from tkinter import *
from Project.main import Instagem
from threading import *

main = Tk()
var = IntVar()



class Logar():
    def logar(self):
        selection = var.get()
        self.bot = Instagem()
        self.bot.login(self.login.get(),self.password.get())
        self.linkfoto()
        if selection == 1:
            self.marcarAmigos()
        else:
            #self.comenta()
            a = Instagem()
            a.obterUsuarios()


    def linkfoto(self):
        self.bot.Postagem(self.LinkInstagram.get())

    def comenta(self):
        qTd=int(self.QtdComentarios.get())
        iVcS=int(self.IntervaloComentariosSeg.get())
        self.bot.Comenta(qTd,iVcS)

    def marcarAmigos(self):
        AqTd=int(self.QtdComentarios.get())
        AiVcS=int(self.IntervaloComentariosSeg.get())

        self.bot.Marca_Amigo(AqTd,AiVcS)

    def threading(self):
        t1 = Thread(target=self.logar)
        t1.start()




class Aplicacao(Logar):
    def __init__(self):

        self.main=main
        self.Principal()
        self.Frame()
        self.Label()
        main.mainloop()

    def Principal(self):
        self.main.title('Boot comentario instagram')
        self.main.geometry('800x500')
        self.main.resizable(False, False)

    def Frame(self):
        self.FramePrincipal = Frame(self.main, bg='#F8F8FF', highlightbackground='black')
        self.FramePrincipal.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

    def Label(self):
        Label(self.FramePrincipal, text='Login', bg='white',fg='#B22222').place(relx=0.08, rely=0.01)
        self.login = Entry(self.FramePrincipal)
        self.login.place(relx=0.15, rely=0.01,width=300)

        Label(self.FramePrincipal, text='Senha', bg='white' ,fg='#B22222').place(relx=0.08, rely=0.10)
        self.password = Entry(self.FramePrincipal,show="*")
        self.password.place(relx=0.15, rely=0.10)

        Label(self.FramePrincipal,text='Link do instagram' ,bg='white',fg='#B22222').place(relx=0.08,rely=0.20)
        self.LinkInstagram=Entry(self.FramePrincipal)
        self.LinkInstagram.place(relx=0.30, rely=0.20,width=500)

        Label(self.FramePrincipal,text='Quantidade de comentarios' ,bg='white',fg='#B22222').place(relx=0.08,rely=0.30)
        self.QtdComentarios=Entry(self.FramePrincipal)
        self.QtdComentarios.place(relx=0.35,rely=0.30 ,width=50)

        Label(self.FramePrincipal,text='Marcar amigo ?',bg='white',fg='#B22222').place(relx=0.08,rely=0.35)

        Radiobutton(self.FramePrincipal,text='Sim' ,bg='white',fg='#B22222',variable=var,value=1).place(relx=0.30,rely=0.35)
        Radiobutton(self.FramePrincipal, text='Nao', bg='white', fg='#B22222',variable=var,value=2).place(relx=0.40, rely=0.35)

        Label(self.FramePrincipal, text='Intervalo entre comentarios em Segundos', bg='white',fg='#B22222').place(relx=0.08, rely=0.40)
        self.IntervaloComentariosSeg=Entry(self.FramePrincipal)
        self.IntervaloComentariosSeg.place(relx=0.45, rely=0.40,width=50)

        self.BtnLogareComentar = Button(self.main, text='Iniciar', command=self.threading)
        self.BtnLogareComentar.place(relx=0.2, rely=0.60,width=100,height=30)

        self.BtnSair = Button(self.main, text='Sair', command=self.main.destroy)
        self.BtnSair.place(relx=0.5, rely=0.60, width=100,height=30)




