# IMPORTANDO LAS LIBRERIAS QUE VAMOS A NECESITAR
import tkinter as tk
from mss import mss
from PIL import Image
import pynput


class MainApp():
    def __init__(self, root):
        self.root = root
        self.root.title('Color Picker')
        self.root.geometry('300x400')
        self.root.resizable(False, False)
        
        #TITLE WIDGET
        self.title = tk.Label(root, text='Color Picker', font=("Arial", 16, "bold"))
        self.title.place(x=90, y=20)
        #HEX Color -- text -- Esto muestra el valor HEX del pixel
        self.hex_color = tk.Label(root, text='HEX Color', font=("Arial", 20, "bold"))
        self.hex_color.place(x=90, y=120)
        
        #HEX COLOR -- canvas -- Esto sivve para mostrar el color del pixel
        self.ColorCanvas = tk.Canvas(root, width=50, height=50, bd=4, relief='flat', highlightbackground="black")
        self.ColorCanvas.config(background='#a1a1a1')
        self.ColorCanvas.place(x=125, y=190)
        
        
        
        
        
        


   
   
if __name__ == '__main__':
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()