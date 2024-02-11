from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import userinfo as ui

class Browser2:
    def __init__(self,link):
        self.link = link
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        Browser2.goInstagram(self)

    def goInstagram(self):
        self.browser.get(self.link)
        time.sleep(2)
        Browser2.Login(self)
        Browser2.getFollowers(self)

    def getFollowers(self):
        consttakipciler = []
        consttakipettiklerim = []
        self.browser.find_element_by_css_selector("#react-root > div > div > section > main > div > header > section > ul > li:nth-child(2) > a > div").click()
        time.sleep(2)

        Browser2.scrollDown(self)

        takipciler = self.browser.find_elements_by_class_name("notranslate")

        for takipci in takipciler:
            consttakipciler.append(takipci.text)

        self.browser.get(self.link+"/" + ui.userName)

        self.browser.find_element_by_css_selector("#react-root > div > div > section > main > div > header > section > ul > li:nth-child(3) > a > div").click()
        time.sleep(2)

        Browser2.scrollDown(self)

        takipettiklerim = self.browser.find_elements_by_class_name("notranslate")

        for takipedilen in takipettiklerim:
            consttakipettiklerim.append(takipedilen.text)
        time.sleep(2)
        for takipedilen2 in consttakipettiklerim:
            check = False
            for takipci2 in consttakipciler:
                if(takipci2 == takipedilen2):
                    check = True
            if(check == False):
                print(takipedilen2 + " seni geri takip etmiyor")
        time.sleep(2)

    def scrollDown(self):
        jsKomut= """
		sayfa = document.querySelector(".isgrP");
		sayfa.scrollTo(0,sayfa.scrollHeight);
		var sayfaSonu = sayfa.scrollHeight;
		return sayfaSonu;
		"""
        sayfaSonu = self.browser.execute_script(jsKomut)
        while True:
            son = sayfaSonu
            time.sleep(1)
            sayfaSonu = self.browser.execute_script(jsKomut)
            if son == sayfaSonu:
                break

    def Login(self):
        username = self.browser.find_element_by_name("username")
        password = self.browser.find_element_by_name("password")

        username.send_keys(ui.userName)
        password.send_keys(ui.password)

        loginBtn = self.browser.find_element_by_css_selector("#loginForm > div > div:nth-child(3)")
        loginBtn.click()
        time.sleep(4)

        self.browser.get(self.link+"/" + ui.userName)
        time.sleep(2)
