import tkinter as tk
from tkinter import *
from search_engine_for_chrome_and_bing import *
from search_engine_for_chrome_and_startpage import *

def Bing():
    
    search_term = search_term_string.get()
    get_results_Bing("{}".format(search_term))
    
def StartPage():
    
    search_term = search_term_string.get()
    get_results_Start_Page("{}".format(search_term))
    
def radio_Control():
    radio_control = radioVariable.get()
    search_term_button = search_term_string.get() 
    
    if search_term_button != "":
        
        if radio_control != 1 and radio_control !=2:
            
            print("Radio Buttons Not Choose")
                
        else:
            
            if radio_control == 1:
                Bing()
                
                
            elif radio_control == 2:
                StartPage()
                
            
    else:
        print("TextBox Cannot Be Empty")
    
        

root = tk.Tk()

width = 300
height = 200

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_coordinate = (screen_width/2) - (width/2)
y_coordinate = (screen_height/2) - (height/2)

root.geometry("%dx%d+%d+%d" % (width,height,x_coordinate,y_coordinate))
root.title("MSI FORM")


head = Label(text = "FIND LINKS", bg = "#003399", fg = "black", width = "250", height = "2")
head.pack()


radioVariable = IntVar()



radioBing = Radiobutton(root, text="Bing", padx = 50, variable = radioVariable, value=1)
radioBing.pack(anchor=tk.W,pady=10)

radioStartPage = Radiobutton(root, text="Start Page", padx = 50, variable = radioVariable, value=2)
radioStartPage.pack(anchor=tk.W)

search_term_string = StringVar()
search_term_textbox = Entry(textvariable = search_term_string, width = "30").pack(anchor=tk.W,padx=50,pady=10)


find = Button(text = "Find Links", width = "25", height = "10", command = radio_Control, bg = "grey").pack(anchor=tk.W,padx=50,pady=10)

root.mainloop()