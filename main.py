from http.server import HTTPServer
import threading
import socket
from tkinter import *
from subprocess import check_output
from tkinter.ttk import Combobox
import webbrowser
from PIL import Image, ImageTk
import pyqrcode
import os
from qrgenerator import handler

parent = Tk()
parent.title("Saral Share")
parent.geometry("800x800+100+10")
parent.iconbitmap("icon.ico")
parent.resizable(height=False, width=False)
def checkConnection():
    meta_data = check_output("ipconfig /all")
    data = meta_data.decode('utf-8', errors="backslashreplace")
    ip = None
    for i in data.splitlines():
        if("DNS Servers" in i):
            ip = i.split(":")[-1].strip()
            break
    return ip
address = None


class SaralShare:

    def __init__(self):
        

        
        
        appDataDir = os.getenv("APPDATA")
        try:
            os.mkdir(os.path.join(appDataDir, "Saral Share"))
        except OSError as error:
            print(error)
        imagePath = os.path.join(appDataDir, "Saral Share", "myqr.png")
        
        portVar = StringVar()
        gfont = ("Arial", 12)
        infoLabel = Label(text="", pady=15,font=("Times New Roman", 18))
        infoLabel.pack(side=TOP)
        
        infoLabel2 = Label(
            text="If this address doesn't match with your Phone\nThen Scan the QR code!", pady=5, font=gfont)
        infoLabel2.pack(side=TOP)
        
        PortText = Label(text="Please select PORT or Enter Manually!",
                         pady=15, font=gfont)
        PortText.pack(side=TOP)
        
        
        
        def TracePortVar(a,b,c):
            if(address is not None):
                infoLabel.configure(
                    text=f"http://{address}:{portVar.get()}")
        portVar.trace("w", TracePortVar)
        comboBox  = Combobox(font=("Arial", 12), values=[str(i) for i in range(8080, 8091)], textvariable=portVar)
        comboBox.pack()
        comboBox.current(0)
        space = Label(text="", pady=5)
        space.pack()
        
        def check():
            global address
            address = checkConnection()
            if(address is not None):
                launchButton.configure(text=f"Launch \n {address}:{portVar.get()}")
                infoLabel.configure(
                    text=f"http://{address}:{portVar.get()}", fg="#1bc43d")
                threading.Thread(
                    target=StartServer, daemon=True).start()
            else:
                qrImage.configure(image="")
                launchButton.configure(text="No connection")
                infoLabel.configure(text="Wifi not connected!", fg="red")
        
        reCheckConnection = Button(text="Refresh", borderwidth=0, border=1, padx=20,
                                   command=check, background="#1646e0", font=("Calibari", 12), fg="white")
        reCheckConnection.place(relx=0.7, rely=0.45, anchor=CENTER)
        def launchIP():
            if (address is not None):
                webbrowser.open_new(f"http://{address}:{portVar.get()}")
            else:
                launchInfo.configure(text="Please Connect WiFi")
        launchButton = Button(
            command=launchIP,
            text="Launch", borderwidth=1, background="#1bc43d", font=gfont, fg="white")
        launchButton.place(relx=0.7, rely=0.51, anchor=CENTER)
        launchInfo = Label(text="", font=("", 12),)
        launchInfo.place(relx=0.7, rely=0.6, anchor=CENTER)
        qrImage = Label(text="No Connection Available", font=gfont)
        qrImage.place(relx=0.3, rely=0.5, anchor=CENTER)       
        
        def launchWebsite():
            webbrowser.open_new("https://saralcode.com/apps/saralshare")
        developerButton = Button(
            borderwidth=1,
            highlightthickness=1,
            command=launchWebsite,
            text="Developed By Saral Code", padx=5, font=("Arial", 12), fg="#1f48cf")
        developerButton.place(relx=0.5, rely=0.8, anchor=CENTER)
        developerInfo = Label(text="This is a web browser launcher for Saral Share\nAndroid Application", font=("", 12), )
        developerInfo.place(relx=0.5, rely=0.85, anchor=CENTER)

        
        def StartServer():
            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)
            if(IPAddr == "127.0.0.1"):
                qrImage.configure(text="Please connect to Wifi")
                print("Please connect to wifi")
            else:
                with HTTPServer((IPAddr, 5595), handler) as server:
                    serverUrl = f"http://{IPAddr}:5595"
                    print(f"Serving at : http://{IPAddr}:5595")
                    # Generate QR code
                    url = pyqrcode.create(serverUrl)
                    url.png(imagePath, scale=8)
                    image1 = Image.open(imagePath)

                    myImage = ImageTk.PhotoImage(image1)

                    qrImage.configure(image=myImage)
                    server.serve_forever()
        check()
        # threading.Thread(
        #     target=StartServer, daemon=True).start()
        parent.mainloop()
    

# async def startServerWithImage():
            
            

SaralShare()
    