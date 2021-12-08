import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class Instagem:
    def __init__(self):
        self.driver = webdriver.Chrome()

    @staticmethod
    def digitar_igual_humano(frase):
        for letra in frase:
            frase.send_keys(letra)
            time.sleep(random.randint(1,5)/30)

    def login(self,username,password):
        self.username = username
        self.password = password
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)
        try:
            user_element = driver.find_element(By.XPATH,
                                               "//input[@name='username']")
            user_element.clear()
            time.sleep(random.randint(5, 10))
            user_element.send_keys(self.username)
            time.sleep(random.randint(5, 10))
            password_element = driver.find_element(By.XPATH,
                                                   "//input[@name='password']")
            password_element.clear()
            password_element.send_keys(self.password)
            time.sleep(random.randint(5, 10))
            password_element.send_keys(Keys.RETURN)
            time.sleep(random.randint(5, 10))
            self.driver.get('https://www.instagram.com')
            print('Logado no instagram')

        except Exception as e:
            print(e)

    def Postagem(self,LINK):
        try:
            WebDriverWait(self.driver.get(f'{LINK}'),5)
            print('acesso a postagem')
            time.sleep(5)

        except Exception as e:
            print(e)

    def Comenta(self,quantidade_comentario,tempo_de_descanco_em_segundos):
        try:
            i = 0
            Arquivo = open("Comentarios.txt",encoding='utf-8')
            comentarios = Arquivo.readlines()
            while i < quantidade_comentario:
                print('Comentando')
                time.sleep(tempo_de_descanco_em_segundos)
                self.driver.find_element(By.CLASS_NAME,'Ypffh').click()
                self.driver.find_element(By.CLASS_NAME,'Ypffh').send_keys(random.choice(comentarios),Keys.ENTER)
                i += 1



        except Exception as e:
            print(e)

