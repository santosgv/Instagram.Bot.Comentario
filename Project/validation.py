from Project.interface import Aplicacao
import urllib.request as urllib2
from tkinter import messagebox


def connection_check():
    try:
        urllib2.urlopen('https://www.google.com', timeout=1)
        serial()
        return True

    except SystemExit:
        messagebox.showinfo("Atenção", "Sem acesso a Internet")
        return False


def serial():
    with open('serial.mde', 'r+') as f:
        data = f.readline()
        try:
            if 30 >= int(data) > 0:
                f.seek(0)
                f.write(str(int(data) - 1))
                messagebox.showinfo("Atenção", "Voce esta usando a versao Trial")
                Aplicacao()
            else:
                messagebox.showerror("Erro", "A versao Trial foi expirada")

        except ValueError:
            messagebox.showerror("Erro", 'Nao foi encontrado uma serial valida')