import requests
import os
import tkinter
from fake_useragent import UserAgent



def get_html(url, e_site):
    ua = UserAgent()
    headers = {'user-agent': f'{ua.opera}'}
    r = requests.get(url, headers=headers)
    r.encoding = e_site
    return r.text


def save_file(url, name):
    r = requests.get(url, stream=True)
    if os.path.exists('download'):
        with open(name, 'bw') as f:
            f.write(r.content)
    else:
        os.mkdir('download')
        with open(name, 'bw') as f:
            f.write(r.content)


def get_window_size():
    r = tkinter.Tk()
    return r.winfo_screenwidth(), r.winfo_screenheight()