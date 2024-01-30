'''from xml.etree.ElementTree import tostring'''
from pickle import FALSE
import requests, bs4
import re
from bs4 import BeautifulSoup as BS
'''from telethon import TelegramClient, events'''
from fake_useragent import UserAgent

def getAnekdotRu():
    url = 'https://anekdot.ru/random/anekdot'                        
    h   = {"User-Agent":"1"}                   # сайт не пускает без header
    web = requests.get(url, headers=h).text    # Получение кода веб-сайта, где расположены случайные анекдоты

    bs      = bs4.BeautifulSoup(web, "lxml")                             
    result    = str(bs.find_all(class_="topicbox")[1].find(class_="text"))  # получаем элемент, в котором написан текст анекдота
    text = result.replace("<br/>","\n")                           # удаляем лишние теги, которые попали в наш текст. заменяем тег переноса на \n
    text = text.split(">")
    text[0] = ""
    text = ''.join(text)
    text = text.split("<")
    text[-1] = ""
    text = ''.join(text)
    #print(text)
    return (text)

def getTg(response):
    if "tgme_widget_message_text js-message_text" in response.text:
        html = (BS(response.text, 'html.parser'))
        html = html.find("div", {"class": "tgme_widget_message_text js-message_text"})
        html = str(html)
        html = html.replace("<br/>","\n")
        html = html.split(">")
        html[0] = ""
        html = ''.join(html)
        html = html.split("<")
        html[-1] = ""
        html = ''.join(html)
        html = html.replace("/b","")
        if html == '':
            html = getTg(response)
            return (html)
        if html[0] == 'b':
            html = html.replace(html[0], "", 1)
    else:
        return ("None")

    return (html)

def getTgImg(response):
    if "tgme_widget_message_photo_wrap" in response.text:
        html = (BS(response.text, 'html.parser'))
        html = html.find("div", {"class": "tgme_widget_message_bubble"})
        html = html.find("a", {"class": "tgme_widget_message_photo_wrap"})
        html = html.get("style")
        html = re.findall(r'url\((.+)\)', html)
        html = str(html)
        html = html.replace('"','')
        html = html.replace("'","")
        html = html.replace("[","")
        html = html.replace("]","")
    else:
        html = "None"
    
    return (html)

def getTgVideo(response):
    if "tgme_widget_message_video js-message_video" in response.text:
        html = (BS(response.text, 'html.parser'))
        html = html.find("video", {"class": "tgme_widget_message_video js-message_video"})
        html = html.get("src")
    else:
        html = "None"

    return (html)