# burakgultekin.com.tr 
# ticimax commenter 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

#your browser path
driver_path = r"path"

browser = webdriver.Chrome(executable_path=driver_path)

#write your url
def siteyiac(url="default url"):
    browser.get(url)
siteyiac()


uyegiris = browser.find_element_by_xpath('//*[@id="divMemberWelcomeContent"]/ul/li[1]/a')
uyegiris.click()
    
eposta = browser.find_element_by_id('txtUyeGirisEmail')
#login e-mail
eposta.send_keys("email")
sifre = browser.find_element_by_id('txtUyeGirisPassword')
#Login password
sifre.send_keys("password")
girisyap = browser.find_element_by_xpath('//*[@id="divUyeGirisContent"]/div/div[1]/div/div/button')
girisyap.click()
time.sleep(5)
siteyiac()
linkler = []

def urunubul():
    urun = browser.find_element_by_xpath('//*[@id="ProductPageProductList"]/div[2]/div/div[1]/a')
    urun.click()
    
    if browser.current_url in linkler:
        time.sleep(5)
        siteyiac()
        urunubul()
    else:
        linkler.append(browser.current_url)
        
def ac(dosya):
    #your files path
    with open('path'+str(dosya),encoding="utf8") as x:
        dizi = x.readlines()
    return [x.strip() for x in dizi]

yorum = ac("yorum.txt") #comments
ad= ac("ad.txt") # names
sozluk = []
for x in ad:
    for y in yorum:
        sozluk.append([x,y])        

        
while True:
    urunubul()
    yorumtab = browser.find_element_by_xpath('//*[@id="ProductDetailMain"]/div/div[3]/div[1]/ul/li[2]/a')
    yorumtab.click()
    
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="txtbxYorumIsim"]').clear()
    metin = browser.find_element_by_xpath('//*[@id="txtbxYorumMesaj"]')
    time.sleep(3)
        
    adsoyad=browser.find_element_by_xpath('//*[@id="txtbxYorumIsim"]')
        
    adsoyad.send_keys(sozluk[0][0])
    metin.send_keys(sozluk[0][1])
    del sozluk[0]
    yorumgonder = browser.find_element_by_xpath('//*[@id="btnYorumKaydet"]')
    yorumgonder.click()
    time.sleep(3)
    yorumatildi = browser.find_element_by_xpath('//*[@id="divYorumYazildi"]/span').text
    if yorumatildi == "Yorumunuz kaydedilmiştir. Teşekkür ederiz":
        siteyiac()