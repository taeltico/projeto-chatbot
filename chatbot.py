from selenium import webdriver
import time

class whatsAppBot:
    def __init__(self):
     self.mensagem = "Bom dia pessoal"
     self.grupos = ["Bot Development Support"]
    Options = webdriver.chromeOptions()
    options.add_argument('lang=pt-br')
    self.driver = webdriver.Chrome(executable_path=r'chromedriver.exe')

def enviarMensagens(self):

    # <span dir="auto" title="Bot Development Support" class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr">Bot Development Support</span>

    # <div tabindex="-1" class="p3_M1">

    #<span data-testid="send" data-icon="send" class="">

    self.driver.get("https://web.whatsapp.com/")
    time.sleep(30)
    for grupo in self.grupos:    
        grupo = self.driver.find_element_by_xpath(f"/span[@title='{grupo}']")
        time.sleep(3)
        grupos.click()
        chat_box = self.driver.find_elements_by_class_name('p3_M1')
        time.sleep(3)
        chat_box.click()
        chat_box.send_keys(self.mensagem)
        self.driver.find_element_by_xpath("//span[@data-icon='send']")
        time.sleep(3)
        botao_enviar.click()
        time.sleep(5)
bot = whatsappBot()
bot.enviarmensagens()
