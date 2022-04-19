import tkinter as tk
import requests
import time
from datetime import date

def getweather(*arg):
    # f = ("poppins", 15, "bold")
    # t = ("poppins", 35, "bold")
    # canvas = tkinter.Tk()
    # canvas.geometry("600x600")
    # canvas.title("Weather app")
    # textfield = tkinter.Entry(canvas, font = t)
    # textfield.pack(pady = 20)
    # textfield.focus()
    # textfield.bind('<Return>', getweather)
    # lbl = tkinter.Label(canvas, text = "")
    # lbl.pack()
    # inputtxt = tkinter.Text(canvas,
    #                height = 5,
    #                width = 20)
    # inputtxt.pack()
    # def printInput():
    #     inp = textfield.get(1.0, "end-1c")
    #     lbl.config(text = "Provided Input: "+inp)
    # printInput()
    # city = textfield.get()
    # print('textfield --',city)
    # canvas.mainloop()
    # api = "https://api.openweathermap.org/data/2.5/weather?q=" + city +"&appid=4a29da6b90cdaebca75efdd596c95d5d"
    # json_data = requests.get(api).json()
    # print(json_data)
    # condition = json_data['weather'][0]['main']
    # temp = int(json_data['main']['temp']- 273.15)
    #min_temp = int(json_data['main']['temp_min']-273.15)
    #max_temp = int(json_data['main']['temp_max']-273.15)
    #pressure = json_data['main']['pressure']
    #humidity = json_data['main']['humadity']
    # wind = json_data['wind']['speed']
    #sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise']-21600))
    #sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset']-21600))
    #final_info = condition + "\n" + str(temp) + "c"
    #final_data = "\n" + "max temp: " + str(max_temp) + "\n" + "min_temp: " + str(min_temp) + "\n" + "pressure: " + str(pressure) + "\n " + "humidity: " +str(humidity) + "\n" +"wind speed: " + str(wind)
    # label1.config(text = final_info)
    #label2.config(text = final_data)
    #city=input('enter the city')
    # label1 = tkinter.Label(canvas, font = t)
    # label1.pack()
    # label2 = tkinter.label(canvas, font = f)
    # label2.pack()
    frame = tk.Tk()
    frame.title("WEATHER")
    frame.geometry('600x600')
    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        lbl.config(text = "weather of - "+inp)
        api = "https://api.openweathermap.org/data/2.5/weather?q=" + inp +"&appid=4a29da6b90cdaebca75efdd596c95d5d"
        json_data = requests.get(api).json()
        # print(json_data)
        lb2.config(text = "weather is "+ json_data['weather'][0]['main'])
        lb3.config(text = "discription "+ json_data['weather'][0]['description'])
        sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise']-21600))
        sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset']-21600))
        sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise']-21600))
        sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset']-21600))
        max_temp = str(int(json_data['main']['temp_max']-273.15))
        min_temp = str(int(json_data['main']['temp_max']-273.15))
        
        lb4.config(text = "sun rise at   "+ sunrise + ",   sun set at  " + sunset)
        lb4.config(text = "min temp is   "+ min_temp + ",  max temp is  "+ max_temp)


    inputtxt = tk.Text(frame,height = 5,width = 20)
    inputtxt.pack()
    printButton = tk.Button(frame,text = "Print", command = printInput)
    printButton.pack()
    lbl = tk.Label(frame, text = "")
    lbl.pack()
    lb2 = tk.Label(frame,text="")
    lb2.pack()
    lb3 = tk.Label(frame,text="")
    lb3.pack()
    lb4 = tk.Label(frame,text="")
    lb4.pack()
    frame.mainloop()
    
getweather()