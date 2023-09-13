import requests
import tkinter as tk
from tkinter import ttk, messagebox

def prayer_times(city,country):
    url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=5"
    try:
        response = requests.get(url)
        info = response.json()
        if "data" in info:
            timings = info["data"]['timings']
            return timings
        else: return None
    except Exception as e:
        print(f"error: {e}")
        
def fetch_data():
    result_screen.delete(0,tk.END)
    city = city_entry.get()
    country= country_entry.get()
    
    if city and country:
        prayer_time = prayer_times(city,country)
        for name,time in prayer_time.items():
            result_screen.insert(tk.END,f"{name} => {time}")
    else:
        messagebox.showerror("Error", "Couldnt Fetch Prayer times")


root = tk.Tk()
frame = ttk.Frame(root,padding='20')
frame.grid(row=0,column=0)
city_list = ['cairo','istanbul','london','dubai']
country_list = ['egypt','turkey','uk','united arap emirates']


city_label = ttk.Label(frame,text="City : ")
city_label.grid(row=0,column=0)
city_entry = ttk.Combobox(frame,values=city_list)
city_entry.grid(row=0,column=1)

country_label = ttk.Label(frame,text="Country : ")
country_label.grid(row=1,column=0)
country_entry = ttk.Combobox(frame,values=country_list)
country_entry.grid(row=1,column=1)

result_button = ttk.Button(frame,text='Get Prayer Time',command=fetch_data)
result_button.grid(row=3,column=1,columnspan=2,pady=10)

result_screen = tk.Listbox(frame)
result_screen.grid(row=4,column=1,columnspan=2,pady=5)

root.mainloop()