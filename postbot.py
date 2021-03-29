import webbrowser
from time import sleep
import keyboard

from selenium import webdriver

# the url we want to open
url = 'https://www.facebook.com'

# read the credentials
file = open("credentials.txt", "r")
email = file.readline()
password = file.readline()
# close the file
file.close()

window = webdriver.Chrome("chromedriver.exe")
window.get(url)

# accept cookies
window.find_element_by_xpath('.//*[@title="Accept All"]').click()

window.find_element_by_xpath('.//*[@id="email"]').send_keys(email)

sleep(3)

window.find_element_by_xpath('.//*[@id="pass"]').send_keys(password)

window.find_element_by_xpath('.//*[@id="loginbutton"]').click()

sleep(10)

window.find_element_by_class_name('m9osqain.a5q79mjw.jm1wdb64.k4urcfbm').click()

sleep(2)

# read the caption
file = open("captions.txt", "r")
caption = file.readline()
file.close()

# read the song link
file = open("links.txt", "r")
link = file.readline()
file.close()

# hashtags
hashtags = '#python #pythonbot #automate'

# merge the read data
post_caption = 'DAY ' + caption + ' ' + hashtags + ' ' + link

# write the post
keyboard.write(post_caption)

# give facebook time to load the song card
sleep(5)

# publish button
publish_btn = 'rq0escxv.l9j0dhe7.du4w35lb' \
              '.j83agx80.pfnyh3mw.taijpn5t' \
              '.bp9cbjyn.owycx6da.btwxx1t3' \
              '.kt9q3ron.ak7q8e6j.isp2s0ed' \
              '.ri5dt5u2.rt8b4zig.n8ej3o3l' \
              '.agehan2d.sk4xxmp2.ni8dbmo4' \
              '.stjgntxs.d1544ag0.tw6a2znq' \
              '.s1i5eluu.tv7at329'
window.find_element_by_class_name(publish_btn).click()

# re-write the captions file skipping the first line
file = open("captions.txt", "r")
lines = file.readlines()
file.close()

file = open("captions.txt", "w")
i = 0
for line in lines:
    if i != 0:
        file.write(line)
    i += 1

file.close()


# re-write the links file skipping the first line
file = open("links.txt", "r")
lines = file.readlines()
file.close()

file = open("links.txt", "w")
i = 0
for line in lines:
    if i != 0:
        file.write(line)
    i += 1

file.close()

