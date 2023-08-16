
# importing library
import requests
from bs4 import BeautifulSoup
import tkinter
from tkinter import LEFT

#window creation
window = tkinter.Tk()
window.title("Weather")
window.minsize(width=300,height=300)
    
#button function
def funaction_button():
    input = entry.get()
    try:
        if input == "":
            label2.config(text="Please don't leave it empty")
        else:
            # creating url and requests instance
            url = f"https://www.google.com/search?q=weather{input}"
            html = requests.get(url).content
    
            # getting raw data
            soup = BeautifulSoup(html, 'html.parser')
            temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
            str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
            # formatting data
            data = str.split('\n')
            time = data[0]
            sky = data[1]
                    
            # getting all div tag
            listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
            strd = listdiv[5].text
                    
            # getting other required data
            pos = strd.find('Wind')
            other_data = strd[pos:]
                    
            # printing all data
            label2.config(text=f"Temperature is {temp} \n Time: {time} \n Sky Description: {sky} \n {other_data}")
    except:
        label2.config(text="Please enter a city name")

# photo
photo = tkinter.PhotoImage(file="image_64.png")
photo_label = tkinter.Label(image=photo)
photo_label.pack()

        
label1 = tkinter.Label(text="Please enter your city")
label1.pack()

entry = tkinter.Entry(width=30)
entry.pack()

photo1 = tkinter.PhotoImage(file="icons8-click-64.png")
button = tkinter.Button(text="Click",command=funaction_button,image=photo1,width=185,height=50,compound = LEFT)
button.pack()

label2 = tkinter.Label(text="")
label2.pack()

window.mainloop()