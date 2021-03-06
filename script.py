from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from threading import Thread
import threading

driver = []
wait = []

def waitX(wait, path):
    e = wait.until(EC.presence_of_element_located((By.XPATH, path)))
    return e
def waitY(wait, path):
    e = wait.until(EC.presence_of_element_located((By.CLASS_NAME, path)))
    return e
class process(Thread):
    def __init__(self, count, account):
        Thread.__init__(self)
        self.count = count
        self.account = account
        driver.append(webdriver.Chrome())
        wait.append(WebDriverWait(driver[self.count], 10))
    def run(self):
        user = self.account.split(":")[0]
        passw = self.account.split(":")[1]
        driver[self.count].get("https://hot14.vn/")
        btnLogin = waitX(wait[self.count], """//*[@id="sticky-wrapper"]/div/div/div[4]/a""").click()
        btnFbLogin = waitX(wait[self.count], """//*[@id="popUp-login"]/div/a[2]""").click()
        logConfirm = waitX(wait[self.count], """//*[@id="email"]""")
        driver[self.count].find_element_by_xpath("""//*[@id="email"]""").send_keys(user)
        inpPass = driver[self.count].find_element_by_xpath("""//*[@id="pass"]""")
        inpPass.send_keys(passw)
        inpPass.send_keys(Keys.RETURN)
        e = threading.Event()
        try:
            confirm = waitX(wait[self.count], """//*[@id="live-daily-chart"]/li[2]/div""")
        except:
            driver[self.count].get("https://hot14.vn/")
            btnLogin = waitX(wait[self.count], """//*[@id="sticky-wrapper"]/div/div/div[4]/a""").click()
            btnFbLogin = waitX(wait[self.count], """//*[@id="popUp-login"]/div/a[2]""").click()
        chart = waitX(wait[self.count], """//*[@id="form1"]/div[3]/div[3]/div/div[2]/div[1]/div""")
        songtotal = chart.find_elements_by_class_name("song_total")
        for i in songtotal:
            child = i.find_element_by_class_name("name").get_attribute("innerHTML") 
            if child == "Hoa Hải Đường":
                voteH = i.find_element_by_class_name("vote-btn").click()
            if child == "Sóng Gió":
                voteS = i.find_element_by_class_name("vote-btn").click()
            if child == "Em Gì Ơi":
                voteE = i.find_element_by_class_name("vote-btn").click()
        while not e.wait(5):
            driver[self.count].get("https://hot14.vn/")
            confirm = waitX(wait[self.count], """//*[@id="live-daily-chart"]/li[2]/div""")
            chart = waitX(wait[self.count], """//*[@id="form1"]/div[3]/div[3]/div/div[2]/div[1]/div""")
            songtotal = chart.find_elements_by_class_name("song_total")
            for i in songtotal:
                child = i.find_element_by_class_name("name").get_attribute('innerHTML')
                if child == "Hoa Hải Đường":
                    try:
                        voteH = i.find_element_by_class_name("vote-btn").click()
                    except:
                        pass 
                if child == "Sóng Gió":
                    try:
                        voteS = i.find_element_by_class_name("vote-btn").click()
                    except:
                        pass 
                if child == "Em Gì Ơi":
                    try:
                        voteE = i.find_element_by_class_name("vote-btn").click()
                    except:
                        pass 
            

acc1 = process(0, "minh7cpht@gmail.com:tonyandtony2k32k3")
acc2 = process(1, "tony_yeon_parker@protonmail.com:tonyandtony2k32k3")
acc3 = process(2, "seonparkertony@gmail.com:tonyandtony2k32k3")
acc4 = process(3, "+84865524321:BrightlightxLight2003")
acc5 = process(4, "bright.sen.light@gmail.com:minh123456789")
acc1.start()
cc2.start()
acc3.start()
acc4.start()
acc5.start()