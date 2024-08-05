import tkinter as tk
import pyperclip
from PIL import Image, ImageGrab
from pynput import mouse

class Window:
    def __init__(self, root):
        self.root = root
        self.root.title('Color Picker')
        self.root.geometry('300x400')
        self.root.resizable(False, False)
        
        # TITLE WIDGET
        self.title = tk.Label(root, text='Color Picker', font=("Arial", 16, "bold"))
        self.title.place(x=90, y=20)
        
        # HEX Color -- text -- Esto muestra el valor HEX del pixel
        self.hex_color = tk.Label(root, text='#a1a1a1', font=("Arial", 20, "bold"))
        self.hex_color.place(x=95, y=120)
        
        # HEX COLOR -- canvas -- Esto sirve para mostrar el color del pixel
        self.ColorCanvas = tk.Canvas(root, width=50, height=50, bd=4, relief='flat', highlightbackground="black")
        self.ColorCanvas.config(background='#a1a1a1')
        self.ColorCanvas.place(x=125, y=190)
        
        # CopyButton -- Esto lo usamos para copiar el color (hex_color)
        self.CopyButton = tk.Button(root, width=10, height=2, text='Copy color', cursor='hand2', background='#bababa', command=self.CopyTheColor)
        self.CopyButton.place(x=97, y=280)  
        
        self.CopyButton.bind("<Enter>", lambda event: self.CopyButton.config(background='#949494'))
        self.CopyButton.bind("<Leave>", lambda event: self.CopyButton.config(background='#bababa')) 
        
        # Configura el evento para detectar la tecla F1
        self.root.bind('<F8>', lambda event: self.GetColor())
        
        # Configura el listener del ratón para obtener la posición
        self.mouse_listener = mouse.Listener(on_move=self.on_move)
        self.mouse_listener.start()
        
    def on_move(self, x, y):
        self.mouse_x = x
        self.mouse_y = y
        
    def CopyTheColor(self):
        hexcolorvalue = self.hex_color.cget('text')
        try:
            pyperclip.copy(hexcolorvalue)
            #print(f'Se ha copiado el color correctamente: {hexcolorvalue}')
        except Exception as error:
            #print(f'Ha ocurrido un error: {error}')
            # Mostrar un mensaje de error en la interfaz de usuario (opcional)
            tk.messagebox.showerror("Error", f"Ha ocurrido un error: {error}")
            
    def ChangeColor(self, hex_value):
        self.hex_color.config(text=hex_value)
        self.ColorCanvas.config(background=hex_value)
        
    def GetColor(self):
        try:
            # Usa la posición del ratón capturada por pynput
            x, y = getattr(self, 'mouse_x', 0), getattr(self, 'mouse_y', 0)

            # Define la región de captura (un solo pixel)
            bbox = (x, y, x + 1, y + 1)
        
            # Captura la región de un solo pixel usando Pillow
            image = ImageGrab.grab(bbox)
            
            # Obtén el color del pixel en la posición (0, 0) de la imagen capturada
            pixel_color = image.getpixel((0, 0))
        
            # Convierte el color RGB a HEX
            hex_color = '#{:02x}{:02x}{:02x}'.format(*pixel_color)

            #print(f'Posición del ratón: x={x}, y={y}')
            #print(f'El color es: {hex_color}')
            
            self.ChangeColor(hex_value=hex_color)            
            
        except Exception as e:
            #print(f'Ha ocurrido un error: {e}')
            tk.messagebox.showerror("Error", f"Ha ocurrido un error: {e}")


if __name__ == '__main__':
    root = tk.Tk()
    app = Window(root)
    root.mainloop()
