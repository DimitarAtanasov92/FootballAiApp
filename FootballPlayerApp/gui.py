import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from model import PlayerValuePredictor


class PlayerValueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Футболист Ценов Прогнозатор")

        self.predictor = PlayerValuePredictor('fifa_players.csv')
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Заплата (евро):").grid(row=0, column=0)
        self.wage_entry = tk.Entry(self.root)
        self.wage_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Общ рейтинг:").grid(row=1, column=0)
        self.overall_entry = tk.Entry(self.root)
        self.overall_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Потенциал:").grid(row=2, column=0)
        self.potential_entry = tk.Entry(self.root)
        self.potential_entry.grid(row=2, column=1)

        tk.Label(self.root, text="Международна репутация (1-5):").grid(row=3, column=0)
        self.reputation_combobox = ttk.Combobox(self.root, values=["1", "2", "3", "4", "5"])
        self.reputation_combobox.grid(row=3, column=1)

        tk.Label(self.root, text="Реакции:").grid(row=4, column=0)
        self.reactions_entry = tk.Entry(self.root)
        self.reactions_entry.grid(row=4, column=1)

        tk.Label(self.root, text="Композиция:").grid(row=5, column=0)
        self.composure_entry = tk.Entry(self.root)
        self.composure_entry.grid(row=5, column=1)

        tk.Label(self.root, text="Визия:").grid(row=6, column=0)
        self.vision_entry = tk.Entry(self.root)
        self.vision_entry.grid(row=6, column=1)

        self.predict_button = tk.Button(self.root, text="Прогнозирай", command=self.predict_value)
        self.predict_button.grid(row=7, columnspan=2)

    def predict_value(self):
        try:
            wage = int(self.wage_entry.get())
            overall = int(self.overall_entry.get())
            potential = int(self.potential_entry.get())
            reputation = self.reputation_combobox.get()
            reactions = int(self.reactions_entry.get())
            composure = int(self.composure_entry.get())
            vision = int(self.vision_entry.get())

            predicted_value = self.predictor.predict(wage, overall, potential, reputation, reactions, composure, vision)
            messagebox.showinfo("Резултат", f"Прогнозна стойност на футболиста: {predicted_value:.2f} евро")
        except Exception as e:
            messagebox.showerror("Грешка", str(e))
