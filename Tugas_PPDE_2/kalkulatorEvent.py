import tkinter as tk
from tkinter import messagebox

class kalkulatorEvent:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Kalkulator Event Driven")
        self.window.geometry("300x400")
        self.window.config(bg="lightblue")
        
        self.current_input = ""
        self.operator = ""
        self.first_number = 0
        
        self.buat_interface()
    
    def buat_interface(self):
        # display untuk menampilkan angka
        self.display = tk.Entry(
            self.window,
            font=("Courier New", 16),
            justify="right",
            state="readonly",
            bg="white"
        )
        self.display.pack(fill=tk.X, padx=10, pady= 10)
        
        # frame tombol
        button_frame = tk.Frame(self.window, bg="lightgray")
        button_frame.pack(fill=tk.BOTH)
        
        # Tombol angka 0 - 9
        for i in range(3):
            for j in range(3):
                angka = i * 3 + j + 1
                btn = tk.Button(
                    button_frame,
                    text=str(angka),
                    font=("Courier New", 14),
                    width=5,
                    height=2,
                    command=lambda n=angka: self.input_angka(n)
                )
                btn.grid(row=i, column=j, padx=2, pady=2)

        # Tombol 0
        btn_0 = tk.Button(
            button_frame,
            text="0",
            font=("Courier New", 14),
            width=5,
            height=2,
            command=lambda: self.input_angka(0)
        )
        btn_0.grid(row=3, column=1, padx=2, pady=2)
        
        # Tombol operator
        operators = ['+', '-', '*', '/']
        for i, op in enumerate(operators):
            btn_op = tk.Button(
                button_frame,
                text=op,
                font=("Courier New", 14),
                width=5,
                height=2,
                bg="green",
                command=lambda o=op: self.input_operator(o)
            )
            btn_op.grid(row=i, column=3, padx=2, pady=2)
        
        # tombol sama dengan
        btn_equals = tk.Button(
            button_frame,
            text="=",
            font=("Courier New", 14),
            width=5,
            height=2,
            command=self.hitung_hasil
        )
        btn_equals.grid(row=3, column=2, padx=2, pady=2)
        
        # tombol clear
        btn_clear = tk.Button(
            button_frame,
            text="C",
            font=("Courier New", 14),
            width=5,
            height=2,
            bg="red",
            fg="white",
            command=self.clear_all
        )
        btn_clear.grid(row=3, column=0, padx=2, pady=2)
        
    def input_operator(self, op):
        # Event handler Input operator
        if self.current_input:
            self.first_number = float(self.current_input)
            self.operator = op
            self.current_input = ""
            self.update_display()
    
    def hitung_hasil(self):
        # Event handler menghitung hasil
        if self.current_input and self.operator:
            try:
                second_number = float(self.current_input)
                
                if self.operator == '+':
                    result = self.first_number + second_number
                elif self.operator == '-':
                    result = self.first_number - second_number
                elif self.operator == '*':
                    result = self.first_number * second_number
                elif self.operator == '/':
                    if second_number != 0:
                        result = self.first_number / second_number
                    else:
                        messagebox.showerror("Error", "Pembagian dengan nol!")
                        return
                
                self.current_input = str(result)
                self.operator = ""
                self.first_number = 0
                self.update_display()
            except ValueError:
                messagebox.showerror("Error", "Input tidak valid")
    
    def clear_all(self):
        # event handler untuk clear layar
        self.current_input = ""
        self.operator = ""
        self.first_number = 0
        self.update_display()
        
    def input_angka(self, angka):
        # Event handler input angka
        self.current_input += str(angka)
        self.update_display()
        
    def update_display(self):
        # Method update layar display
        self.display.config(state="normal")
        self.display.delete(0, tk.END)
        self.display.insert(0, self.current_input)
        self.display.config(state="readonly")
    
    def jalankan(self):
        self.window.mainloop()
        
if __name__ == "__main__":
    # instance init from appBio class
    kalkulator = kalkulatorEvent()
    kalkulator.jalankan()