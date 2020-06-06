arquivo = open("Dados.txt", "a")

from selenium import webdriver
import time
from tkinter import *
import os

lista = []
mens = []
transformador = ""
janela = Tk()
c = ""

def click1():
    ed2.get()
    lista.append(ed2.get())
    arquivo.write("\n" + ed2.get()+ "\n")
    contador = len(lista)
    lb3["text"] = contador


def click2():
    ed1.get()
    lista.remove(ed1.get())

    contador = len(lista)
    lb3["text"] = contador


def click3():
    ed3.get()
    mens.append(ed3.get())
    ###############################
    janela.quit()  # ao clicar no botão enviar a janela é fechada e o fluxo do código continua

###########################


bt1 = Button(janela, width=20, text="adicionar", command=click1)
bt1.place(x=30, y=140)

bt2 = Button(janela, width=20, text="remover", command=click2)
bt2.place(x=30, y=180)

bt3 = Button(janela, width=20, text="enviar", command=click3)
bt3.place(x=290, y=130)

ed1 = Entry(janela)
ed1.place(x=40, y=100)

ed2 = Entry(janela)
ed2.place(x=40, y=50)

ed3 = Entry(janela)
ed3.place(height=40, x=300, y=80)

lb1 = Label(text="nome de quem adicionar")
lb1.place(x=35, y=20)

lb2 = Label(text="nome de quem remover")
lb2.place(x=35, y=75)

lb3 = Label(text="0")
lb3.place(x=175, y=47)

lb4 = Label(text="mensagem que você quer enviar")
lb4.place(x=280, y=50)

janela.title("ver0.001 beta")
janela.geometry('500x350')
janela.mainloop()
print(lista)

for i in (mens):
    transformador = i
print(transformador)


class WhatsappBot:
    def __init__(self):
        # Parte 1 - A mensagem que você quer enviar
        self.mensagem = transformador
        # Parte 2 - Nome dos grupos ou pessoas a quem você deseja enviar a mensagem
        self.grupos_ou_pessoas = lista
        options = webdriver.ChromeOptions()  # Linha desnecessarias
        options.add_argument('lang=pt-br')  # Linha desnecessarias
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', chrome_options=options)

    def EnviarMensagens(self):
        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)
        for grupo_ou_pessoa in self.grupos_ou_pessoas:
            campo_grupo = self.driver.find_element_by_xpath(
                f"//span[@title='{grupo_ou_pessoa}']")
            time.sleep(3)
            campo_grupo.click()
            chat_box = self.driver.find_element_by_class_name('_1Plpp')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)


bot = WhatsappBot()
bot.EnviarMensagens()
