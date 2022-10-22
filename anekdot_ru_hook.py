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
    return text

def getTg(url):
    request = requests.get(url, headers={'User-Agent': UserAgent().chrome})
    html = (BS(request.text, 'html.parser'))
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
        html = getTg(url)
        return (html)
    if html[0] == 'b':
        html = html.replace(html[0], "", 1)

    return (html)

def getTgImg(url):
    request = requests.get(url, headers={'User-Agent': UserAgent().chrome})
    html = (BS(request.text, 'html.parser'))
    html = html.find("div", {"class": "tgme_widget_message_bubble"})
    html = html.find("a", {"class": "tgme_widget_message_photo_wrap"})
    try:
        html = html.get("style")
        html = re.findall(r'url\((.+)\)', html)
        html = str(html)
        html = html.replace('"','')
        html = html.replace("'","")
        html = html.replace("[","")
        html = html.replace("]","")
    except:
        html = "None"

    return (html)