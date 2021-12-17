import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class Instagem():
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
            self.driver.close()

    def Postagem(self,LINK):
        try:
            WebDriverWait(self.driver.get(f'{LINK}'),5)
            print('acesso a postagem')
            time.sleep(5)

        except Exception as e:
            print(e)
            self.driver.close()

    def Comenta(self,quantidade_comentario,tempo_de_descanco_em_segundos):
        try:
            i = 0
            Arquivo = open("Comentarios.txt",encoding='utf-8')
            comentarios = Arquivo.readlines()
            while i < quantidade_comentario:
                comentario = random.choice(comentarios)
                print('Comentando')
                self.driver.find_element(By.CLASS_NAME,'Ypffh').click()
                self.driver.find_element(By.CLASS_NAME,'Ypffh').send_keys(comentario,Keys.ENTER)
                i += 1
                print(f'foi comentado {i}')
                time.sleep(tempo_de_descanco_em_segundos)



        except Exception as e:
            print(e)
            self.driver.close()

        finally:
            print(f'O script terminou comentando {i}')
            self.driver.close()


    def Marca_Amigo(self,quantidade_comentario,tempo_de_descanco_em_segundos):
        try:
            a = 0
            Arquivo = open("Amigos.txt",encoding='utf-8')
            Amigo = Arquivo.readlines()
            while a < quantidade_comentario:
                comentarioamigo = random.choice(Amigo)
                print('Marcando')
                self.driver.find_element(By.CLASS_NAME,'Ypffh').click()
                time.sleep(2.3)
                self.driver.find_element(By.CLASS_NAME,'Ypffh').send_keys(comentarioamigo,Keys.TAB)
                time.sleep(2.3)
                self.driver.find_element(By.CLASS_NAME, 'Ypffh').send_keys(Keys.ENTER)
                a += 1
                print(f'o amigo {comentarioamigo} Marcado total {a}')
                time.sleep(tempo_de_descanco_em_segundos)



        except Exception as e:
            print(e)
            self.driver.close()

        finally:
            print(f'O script terminou comentando {a}')
            self.driver.close()
