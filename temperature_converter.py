import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox

class TemperatureConverterApp(tb.Window):
    def __init__(self):
        super().__init__(themename="cyborg")  # Dark modern theme
        self.title("🌡️ Temperature Converter")
        self.geometry("400x400")
        self.create_widgets()

    def create_widgets(self):
        tb.Label(self, text="Temperature Converter", font=("Helvetica", 18), bootstyle="info").pack(pady=20)

        self.temp_entry = tb.Entry(self, font=("Helvetica", 12), bootstyle="primary")
        self.temp_entry.pack(pady=10, ipadx=10, ipady=5)

        self.from_unit = tb.Combobox(self, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly", bootstyle="info")
        self.from_unit.set("Celsius")
        self.from_unit.pack(pady=5)

        self.to_unit = tb.Combobox(self, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly", bootstyle="info")
        self.to_unit.set("Fahrenheit")
        self.to_unit.pack(pady=5)

        tb.Button(self, text="Convert", command=self.convert_temp, bootstyle="success-outline").pack(pady=15)

        self.result_label = tb.Label(self, text="", font=("Helvetica", 14), bootstyle="warning")
        self.result_label.pack(pady=20)

    def convert_temp(self):
        try:
            value = float(self.temp_entry.get())
            from_u = self.from_unit.get()
            to_u = self.to_unit.get()

            # Convert to Celsius
            if from_u == "Celsius":
                celsius = value
            elif from_u == "Fahrenheit":
                celsius = (value - 32) * 5 / 9
            elif from_u == "Kelvin":
                celsius = value - 273.15

            # Convert from Celsius to target
            if to_u == "Celsius":
                result = celsius
            elif to_u == "Fahrenheit":
                result = celsius * 9 / 5 + 32
            elif to_u == "Kelvin":
                result = celsius + 273.15

            self.result_label.config(text=f"{round(result, 2)} {to_u}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

if __name__ == "__main__":
    app = TemperatureConverterApp()
    app.mainloop()
