import customtkinter
from constantes import constantes as c


class FloatSpinbox(customtkinter.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 28,
                 step_size:  int= 1,
                 command = None,
                 value=0,
                 name="",
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.step_size = step_size
        self.command = command
        self.value=value
        self.name=name
        self.configure(fg_color=("#cbd5e1","#1e293b"), corner_radius=0, height=10)
        
        self.grid_columnconfigure((1, 2), weight=0)  # buttons don't expand
        self.grid_columnconfigure(0, weight=1)  # entry expands

        
        self.entry = customtkinter.CTkEntry(self, width=width-(2*height), height=height-6, border_width=0, corner_radius=0, fg_color="transparent",  font=('yu gothic ui', 16, 'bold'), placeholder_text_color=("black","white"))
        self.entry.grid(row=0, column=0, columnspan=1, padx=1, pady=2, sticky="ew")

        self.subtract_button = customtkinter.CTkButton(self, text="-", width=height-10,height=height-10,  fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), hover=False, text_color=(c.LIGHT_TEMA,c.DARK_TEMA), font=('yu gothic ui', 16, 'bold'),
                                                       command=self.subtract_button_callback, corner_radius=5)
        self.subtract_button.grid(row=0, column=1, padx=(3, 0), sticky="ew")

        self.add_button = customtkinter.CTkButton(self, text="+", width=height-10, height=height-10,  fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), hover=False, text_color=(c.LIGHT_TEMA,c.DARK_TEMA), font=('yu gothic ui', 16, 'bold'),
                                                  command=self.add_button_callback)
        self.add_button.grid(row=0, column=2, padx=(3, 3), sticky="ew")

        # default value
        self.entry.insert(0, self.value if self.value !=0 else self.name)

    def add_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            if self.entry.get() == self.name:
                value=0
            else:
                value = int(self.entry.get()) + self.step_size

            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def subtract_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get()) - self.step_size
            self.entry.delete(0, "end")
            if value < 0:
                self.entry.insert(0, self.name)
            else:
                
                self.entry.insert(0,  value)
        except ValueError:
            return

    def get(self):
        try:
            return int(self.entry.get())
        except ValueError:
            return None

    def set(self, value: int):
        self.entry.delete(0, "end")
        self.entry.insert(0, str(int(value)))