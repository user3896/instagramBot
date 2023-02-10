from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chrome_driver = "C:\drivers\chromedriver"

driver = webdriver.Chrome(chrome_driver)


class insta:
    def __init__(self, username, gmail, password):
        self.username = username
        self.gmail = gmail
        self.password = password
        self.url = "https://www.instagram.com/accounts/login/"

    def login(self):
        driver.get(self.url)
        sleep(3)
        username = driver.find_element_by_name("username")
        password = driver.find_element_by_name("password")
        print("bulundu")
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)
        sleep(5)
        print("yüklendi")
        driver.close

    def follower(self):
        driver.get(self.url)
        sleep(3)
        username = driver.find_element_by_name("username")
        password = driver.find_element_by_name("password")
        print("bulundu")
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)
        sleep(10)
        next = driver.find_element_by_class_name("EforU")
        next.click()
        sleep(5)
        pro = driver.find_element_by_link_text("Profil")
        pro.click()
        sleep(10)
        folower = driver.find_element_by_partial_link_text(" takipçi")
        folower.click()
        sleep(5)
        # followers = driver.find_element_by_class_name("_aacl._aaco._aacu._aacx._aada").find_element_by_tag_name("span").find_element_by_tag_name("span").find_element_by_tag_name("div") sadece bi tanesi
        followers = driver.find_elements_by_class_name(
            "_ab8w ._ab94._ab99._ab9h._ab9m._ab9o._abcm")  # buda oluyo
        for i in followers:
            print(i.find_element_by_class_name(
                "_aacl._aaco._aacu._aacy._aada"))

        # foto = driver.find_elements_by_class_name("_aap6._aap7._aapa")

        # for i in foto:
        #     print(i.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div[1]/div/div/a/img'))
    def message(self):
        driver.get(self.url)
        sleep(3)
        username = driver.find_element_by_name("username")
        password = driver.find_element_by_name("password")
        print("bulundu")
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)
        sleep(10)
        a = driver.get(
            "https://www.instagram.com/direct/t/340282366841710300949128227709915881731")  # your message box link
        sleep(5)
        a = driver.find_element_by_class_name("_a9--._a9_1")
        a.click()
        # a.find_elements_by_tag_name("button")[1].click()
        sleep(5)
        a0 = driver.find_element_by_tag_name("textarea")
        while 1:
            a0.send_keys("instagram botu")
            a0.send_keys(Keys.ENTER)


a0 = insta("your instagram username", "your gmail", "instagram_password")
# class="._ab8y.._ab94._ab97._ab9f._ab9k._ab9p._abcm"
a0.follower()
# a0.message()
