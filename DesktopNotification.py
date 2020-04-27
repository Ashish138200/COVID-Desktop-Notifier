from tkinter import *

import requests
from win10toast import ToastNotifier
import datetime
try:
    data = requests.get("https://api.covid19india.org/data.json")   # covid19india database
except:
    print("Check your internet connection")
    data = None

if data is not None:
    getData = data.json()
    covid_India = getData["cases_time_series"]                      # national level data
    title = """Ashish's COVID-19 India Live  {}""".format(datetime.date.today())
    n = len(covid_India)
    a = covid_India[n-1]                                            # current date data
    l = list(a.values())
    dconf = l[0]                                                    # daily confirmed
    ddec = l[1]                                                     # daily deaths
    drecov = l[2]                                                   # daily recovered
    date = l[3]
    tc = l[4]                                                       # total confirmed
    td = l[5]                                                       # total deaths
    tr = l[6]                                                       # total recovered
    m1 = "Total cases is: %s " %tc +"\n"
    m2 = "Total Deaths: %s " %td  + "\n"
    m3 = "Total Recovered: %s " %tr + "\n"
    m4=  "Today's confirmed cases: %s"%dconf + "\n"
    message = m1+m2+m3+m4
    toaster = ToastNotifier()
    toaster.show_toast(title, message, icon_path="Corona.ico", duration=100)
