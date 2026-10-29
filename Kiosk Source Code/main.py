import tkinter as tk # GUI library for creating the application window and widgets
import winsound # Library for playing sound on Windows, used to play a beep sound on button clicks

from homescreen import Home_Screen 
from parkingscreen import Parking
from mapscreen import Map

class KioskApp:
    def __init__(self, root,):
        self.root = root
        self.root.title('Trafford centre Kiosk')
        self.root.geometry('1920x1080')
        self.current_screen = None
        self.font_size = 15
        self.show_home()

    def show_home(self):
        self.switch_to(Home_Screen)

    def show_parking(self):
        self.switch_to(Parking)


    def show_map(self):
        self.switch_to(Map)

    def switch_to(self, ScreenClass):
        if self.current_screen is not None:
            self.current_screen.frame.destroy()
        self.current_screen = ScreenClass(self.root, self)
        self.apply_font_to_screen()


    def update_font_sizes(self, delta): 
        self.font_size = max(5, min(60, self.font_size + delta))
        self.apply_font_to_screen()

    def apply_font_to_screen(self):

        def update_widgets(parent):
            for widget in parent.winfo_children():
                if isinstance(widget, tk.Button):
                    widget.config(font=("Arial", self.font_size))
                update_widgets(widget)

        update_widgets(self.root)

    
    def on_click(self):
        winsound.Beep(800, 80) # Play a beep sound on click


    

if __name__ == '__main__':
    root = tk.Tk()
    app = KioskApp(root)
    root.mainloop()
