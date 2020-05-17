import configparser
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

options=webdriver.ChromeOptions()
options.add_argument('headless')

class linkedinbot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.base_url = 'https://www.linkedin.com'
        self.login_url = self.base_url + '/login'
        self.feed_url = self.base_url + '/feed'

        self.username = username
        self.password = password

    def _open(self,url):
        self.driver.get(url)
        sleep(2)

    def login(self,username,password):
        self._open(self.login_url)
        self.driver.find_element_by_id('username').send_keys(self.username)
        self.driver.find_element_by_id('password').send_keys(self.password)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Sign in')]").click()


    def post(self,text):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME,'share-box-feed-entry__trigger'))).click()
        #self.driver.find_element_by_class_name('share-box-feed-entry__trigger').click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div/div/div[1]/p').send_keys(post_text)
        sleep(2)
        self.driver.find_element_by_class_name("share-actions").click()
        sleep(4)

    def search(self,text,connect=False):
        self._open(self.feed_url)
        search = self.driver.find_element_by_class_name('search-global-typeahead__input')
        search.send_keys(text)
        search.send_keys(Keys.ENTER)


        if connect:
            self._search_connect()

    def _search_connect(self): # a private method and cannot be called by the object of the class itself; some other method defined inside the class has to call it
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[3]/div/div[2]"
                                                                                  "/div/div[2]/div/div/div/div/ul/li[1]"
                                                                                  "/div/div/div[3]/div"))).click()

        #self.driver.find_element_by_class_name('search-result__actions--primary').click()

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div[3]/button[1]"))).click()
        self.driver.find_element_by_class_name('send-invite__custom-message').send_keys(note)
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()

    def min_chat(self):
        sleep(10)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME,'msg-overlay-bubble-header__button'))).click()

if __name__ == '__main__':

    config = configparser.ConfigParser()
    config.read("C:/_.ini")
    username = config['CREDS']['USERNAME']
    password = config['CREDS']['PASSWORD']

    post_text = "This is an automated bot."
    search_text = ' '
    note = ' '

    bot = linkedinbot(username,password)
    bot.login(username,password)
    bot.min_chat()
    #bot.post(post_text)
    bot.search(search_text,connect=True)