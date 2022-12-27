from PIL import ImageTk, Image
import tkinter as tk
import json

list=[]

def createWindow():
    window = tk.Tk()
    window.geometry('1920x1080')
    window.configure(background="grey")
    with open('sample.json', 'r') as openfile:
        json_object = json.load(openfile)

    for x in json_object:
            if json_object[x]["have"] != json_object[x]["need"]:
                img = ImageTk.PhotoImage(Image.open("C:/Users/Tobis-RGP-GamingPC/Desktop/Tarkov/Bilder/"+x+".png"))
                hight = img.height()
                if hight not in list:
                    list.append(hight)
 
    def test(itemName):
        if json_object[itemName]["have"] != json_object[itemName]["need"]:
            json_object[itemName]["have"] += 1
            window.destroy()  
            json_object2 = json.dumps(json_object, indent=4)

            with open("sample.json", "w") as outfile:
                outfile.write(json_object2)
            createWindow()

    row = 0
    column = 0
    for h in list:
        for x in json_object:
            if json_object[x]["have"] != json_object[x]["need"]:
                img = ImageTk.PhotoImage(Image.open("C:/Users/Tobis-RGP-GamingPC/Desktop/Tarkov/Bilder/"+x+".png"))
                if img.height() == h:
                    column = column+2
                    l = tk.Label(window,background='grey', text=x).grid(row=row, column=column)
                    def action(y = x): 
                        return test(y)
                    b = tk.Button(l, text = x, image = img, command=action)
                    b.image = img
                    b.grid(row=row+1, column=column)
                    tk.Label(l,background='grey',text=str(json_object[x]["have"])+"/"+str(json_object[x]["need"])).grid(row=row+1, column=column , sticky='s')
                    if column == 18:
                        row = row +2
                        column = 0
        
    window.mainloop()

    json_object2 = json.dumps(json_object, indent=4)

    with open("sample.json", "w") as outfile:
        outfile.write(json_object2)

createWindow()