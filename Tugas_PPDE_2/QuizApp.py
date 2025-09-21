import tkinter as tk
from tkinter import messagebox, ttk
import random

class QuizApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quiz Interaktif - Tugas Akhir")
        self.window.geometry("800x600")
        self.window.resizable(False, False)

        # Data quiz (10 soal)
        self.questions = [
            {
                "question": "Apa itu event-driven programming?",
                "options": ["Program yang berjalan berurutan", 
                            "Program yang merespons kejadian", 
                            "Program tanpa GUI", 
                            "Program berbasis web"],
                "correct": 1
            },
            {
                "question": "Apa fungsi utama dari Tkinter di Python?",
                "options": ["Mengakses database", 
                            "Membuat GUI", 
                            "Mengolah data numerik", 
                            "Membuat API"],
                "correct": 1
            },
            {
                "question": "Widget mana yang digunakan untuk menampilkan teks di Tkinter?",
                "options": ["Label", "Button", "Entry", "Frame"],
                "correct": 0
            },
            {
                "question": "Apa kepanjangan dari GUI?",
                "options": ["General User Input", 
                            "Graphical User Interface", 
                            "Global Utility Integration", 
                            "Generate Unified Interaction"],
                "correct": 1
            },
            {
                "question": "Fungsi method mainloop() di Tkinter?",
                "options": ["Menjalankan event loop aplikasi", 
                            "Menggambar tombol", 
                            "Menghentikan program", 
                            "Mengatur ukuran window"],
                "correct": 0
            },
            {
                "question": "Widget apa yang digunakan untuk input teks satu baris?",
                "options": ["Label", "Entry", "Button", "Text"],
                "correct": 1
            },
            {
                "question": "Widget apa yang digunakan untuk menampilkan pilihan ganda?",
                "options": ["Radiobutton", "Entry", "Label", "Text"],
                "correct": 0
            },
            {
                "question": "Fungsi dari pack(), grid(), place() di Tkinter?",
                "options": ["Mengatur tata letak widget", 
                            "Menambahkan warna", 
                            "Mengatur ukuran font", 
                            "Membuat event handler"],
                "correct": 0
            },
            {
                "question": "Tkinter termasuk library bawaan Python?",
                "options": ["Ya", "Tidak"],
                "correct": 0
            },
            {
                "question": "Bahasa apa yang dipakai untuk membuat Tkinter?",
                "options": ["C", "C++", "Python", "Java"],
                "correct": 2
            }
        ]

        random.shuffle(self.questions)

        # State management
        self.current_question = 0
        self.score = 0
        self.time_left = 30
        self.selected_answer = tk.IntVar()
        self.answers = []  # simpan jawaban user untuk review

        self.buat_interface()
        self.load_question()
        self.start_timer()

    def buat_interface(self):
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(fill="both", expand=True)

        # Label pertanyaan
        self.question_label = tk.Label(self.main_frame, text="", wraplength=700, font=("Arial", 14))
        self.question_label.pack(pady=20)

        # Frame untuk opsi jawaban
        self.options_frame = tk.Frame(self.main_frame)
        self.options_frame.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self.options_frame, text="", variable=self.selected_answer, value=i, font=("Arial", 12))
            rb.pack(anchor="w")
            self.option_buttons.append(rb)

        # Timer
        self.timer_label = tk.Label(self.main_frame, text="Waktu tersisa: 30", font=("Arial", 12), fg="red")
        self.timer_label.pack(pady=10)

        # Tombol submit
        self.submit_button = tk.Button(self.main_frame, text="Submit", command=self.submit_answer, font=("Arial", 12), bg="lightblue")
        self.submit_button.pack(pady=20)

    def load_question(self):
        self.selected_answer.set(-1)
        q = self.questions[self.current_question]
        self.question_label.config(text=f"Soal {self.current_question + 1}: {q['question']}")

        for i, option in enumerate(q["options"]):
            if i < len(self.option_buttons):
                self.option_buttons[i].config(text=option, state="normal")
                self.option_buttons[i].pack(anchor="w")
            else:
                self.option_buttons[i].pack_forget()

        # Reset timer
        self.time_left = 30
        self.timer_label.config(text=f"Waktu tersisa: {self.time_left}")

    def start_timer(self):
        if self.current_question < len(self.questions):
            if self.time_left > 0:
                self.timer_label.config(text=f"Waktu tersisa: {self.time_left}")
                self.time_left -= 1
                self.window.after(1000, self.start_timer)
            else:
                self.submit_answer()  # otomatis submit kalau waktu habis

    def submit_answer(self):
        q = self.questions[self.current_question]
        answer = self.selected_answer.get()

        # Simpan jawaban user
        self.answers.append(answer)

        if answer == q["correct"]:
            self.score += 1

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.load_question()
        else:
            self.show_result()

    def show_result(self):
        # Hapus frame utama
        self.main_frame.destroy()

        # Frame hasil & review
        review_frame = tk.Frame(self.window)
        review_frame.pack(fill="both", expand=True, padx=20, pady=20)

        result_label = tk.Label(review_frame, text=f"Hasil Akhir: {self.score} dari {len(self.questions)}", font=("Arial", 16, "bold"))
        result_label.pack(pady=10)

        canvas = tk.Canvas(review_frame)
        scrollbar = ttk.Scrollbar(review_frame, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas)

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Tampilkan review per soal
        for i, q in enumerate(self.questions):
            q_frame = tk.Frame(scroll_frame, pady=5)
            q_frame.pack(fill="x", anchor="w")

            q_label = tk.Label(q_frame, text=f"Soal {i+1}: {q['question']}", font=("Arial", 12, "bold"), anchor="w", justify="left", wraplength=700)
            q_label.pack(anchor="w")

            for j, option in enumerate(q["options"]):
                # default warna hitam
                color = "black"
                prefix = "•"

                if j == q["correct"]:
                    color = "green"
                    prefix = "✅"
                if self.answers[i] == j and j != q["correct"]:
                    color = "red"
                    prefix = "❌"

                opt_label = tk.Label(q_frame, text=f"{prefix} {option}", fg=color, font=("Arial", 11), anchor="w", justify="left", wraplength=700)
                opt_label.pack(anchor="w")

    def jalankan(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = QuizApp()
    app.jalankan()
