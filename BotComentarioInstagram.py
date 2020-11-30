from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(
            firefox_profile=firefoxProfile, executable_path=r"diretório geckodriver"
        )
        

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(0.5)
        user_element = driver.find_element_by_xpath(
            "//span[@class='KPnG0']")
        user_element.click()
        time.sleep(0.5)
        user_element = driver.find_element_by_xpath(
            "//input[@name='email']")
        user_element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element_by_xpath(
            "//input[@name='pass']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(10)
        self.comente_nas_fotos_sorteio()

    @staticmethod
    def type_like_a_person(sentence, single_input_field, tempmin, tempmax):
        print(sentence)
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(tempmin, tempmax) / 8)

    def comente_nas_fotos_sorteio(self):
        driver = self.driver
        pagina = self.listaSorteios()
        partida = 0
        inicio = 0
        encerramento = 1000
        tempmin = 2
        tempmax = 4
        repetir = 2
        nome1 = "1"
        nome2 = "2"
        nome3 = "3"
        localizarnome = 0
        comments = self.listaComments()
        driver.get(random.choice(pagina))   

        while(partida < encerramento):
            print("loop: ", partida)
            try: 
                repetir = 2
                
                driver.find_element_by_class_name("Ypffh").click()
                comment_input_box = driver.find_element_by_class_name("Ypffh")
                nome1 = random.choice(comments)
                nome2 = nome1
                inicio = 0
                while(nome2 == nome1):
                    nome2 = random.choice(comments)
                nome3 = nome2
                while(nome3 == nome2):
                    nome3 = random.choice(comments)
                    if(nome3 == nome1):
                        nome3 = nome2

                while(inicio < repetir):
                    
                    if (inicio == 0):
                        self.type_like_a_person(
                            nome1, comment_input_box, tempmin, tempmax)
                    elif (inicio == 1):
                        self.type_like_a_person(
                            nome2, comment_input_box, tempmin, tempmax)
                    if(inicio == 2 and repetir == 3):
                        self.type_like_a_person(
                            nome3, comment_input_box, tempmin, tempmax)

                    inicio = inicio + 1

                inicio = 0
                partida = partida + 1
                driver.find_element_by_xpath(
                    "//button[contains(text(), 'Publicar')]"
                ).click()
                time.sleep(5)
                driver.find_element_by_class_name("Ypffh").click()
                driver.get(random.choice(pagina))
                time.sleep(5)

            except Exception as e:
                partida = partida - 1
                time.sleep(5)
                driver.get(random.choice(pagina))
                time.sleep(5)

    def listaSorteios(self):
        return [ 
            "inserir a URL dos sorteios a participar"   
        ]

    def listaComments(self):
        return [
            "Inserir Nome dos ",
            "amigos a comentar ",
            "com o @ ",
            "e um espaço no final ",
            "nesse mesmo formato "
        ]



Bot = InstagramBot("email do instagram", "senha do instagram")
Bot.login()