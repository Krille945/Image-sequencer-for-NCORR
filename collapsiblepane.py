

import tkinter as tk
from tkinter import ttk
class CollapsiblePane(ttk.Frame):


    def __init__(self,parent, expanded_text="Collapse<<", collapsed_text="Expand>>"):

        ttk.Frame.__init__(self, parent)

        self.style = ttk.Style()
        #root.style.theme_use("clam")
        self.style.configure('TButton', foreground='#ffffff')
        self.style.configure('TButton', background='#010101')
        self.style.configure('TFrame', background='#272727')
    
        self.parent = parent 
        self._expanded_text = expanded_text 
        self._collapsed_text = collapsed_text 
        self.columnconfigure(1, weight = 1)
        self._variable = tk.IntVar()
        self._button = tk.Checkbutton(self, variable = self._variable, command = self._activate, bg='#272727', fg='#ffffff')
        self._button.grid(row = 0, column = 0)  
        self._button.configure(text = self._collapsed_text)
        #self._separator = ttk.Separator(self, orient ="horizontal") 
        #self._separator.grid(row = 0, column = 1, sticky ="we")  
        self.frame = ttk.Frame(self) 
    

    def _activate(self): 
        if not self._variable.get(): 
         
            self.frame.grid_forget() 
  
            self._button.configure(text = self._collapsed_text)

        elif self._variable.get(): 
            # increasing the frame area so new widgets 
            # could reside in this container 
            self.frame.grid(row = 1, column = 0, columnspan = 5) 
            self._button.configure(text = self._expanded_text) 

    def toggle(self): 
        """Switches the label frame to the opposite state."""
        self._variable.set(not self._variable.get()) 
        self._activate() 
