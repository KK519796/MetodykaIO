import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Formularz rejestracyjny dla wolontariusza")
label_title = tk.Label(root, text="Imię:")
label_title.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_title = tk.Entry(root, width=40)
entry_title.grid(row=0, column=1, padx=10, pady=5)
label_author = tk.Label(root, text="Nazwisko:")
label_author.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_author = tk.Entry(root, width=40)
entry_author.grid(row=1, column=1, padx=10, pady=5)
label_genre = tk.Label(root, text="Adres e-mail:")
label_genre.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_genre = tk.Entry(root, width=40)
entry_genre.grid(row=2, column=1, padx=10, pady=5)
label_year = tk.Label(root, text="Numer telefonu:")
label_year.grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_year = tk.Entry(root, width=40)
entry_year.grid(row=3, column=1, padx=10, pady=5)
label_year = tk.Label(root, text="Miasto:")
label_year.grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_year = tk.Entry(root, width=40)
entry_year.grid(row=4, column=1, padx=10, pady=5)
label_year = tk.Label(root, text="Kraj:")
label_year.grid(row=5, column=0, padx=10, pady=5, sticky="w")
entry_year = tk.Entry(root, width=40)
entry_year.grid(row=5, column=1, padx=10, pady=5)
label_year = tk.Label(root, text="Data urodzenia:")
label_year.grid(row=6, column=0, padx=10, pady=5, sticky="w")
entry_year = tk.Entry(root, width=40)
entry_year.grid(row=6, column=1, padx=10, pady=5)
label_year = tk.Label(root, text="PESEL:")
label_year.grid(row=7, column=0, padx=10, pady=5, sticky="w")
entry_year = tk.Entry(root, width=40)
entry_year.grid(row=7, column=1, padx=10, pady=5)
label_year = tk.Label(root, text="Wykształcenie:")
label_year.grid(row=8, column=0, padx=10, pady=5, sticky="w")
entry_year = tk.Entry(root, width=40)
entry_year.grid(row=8, column=1, padx=10, pady=5)
label_year = tk.Label(root, text="Doświadczenie wolontariackie")
label_year.grid(row=9, column=0, padx=10, pady=5, sticky="w")
entry_year = tk.Entry(root, width=40)
entry_year.grid(row=9, column=1, padx=10, pady=5)
label_year = tk.Label(root, text="Języki obce:")
label_year.grid(row=10, column=0, padx=10, pady=5, sticky="w")
entry_year = tk.Entry(root, width=40)
entry_year.grid(row=10, column=1, padx=10, pady=5)
label_year = tk.Label(root, text="Czy posiadasz prawo jazdy?")
label_year.grid(row=11, column=0, padx=10, pady=5, sticky="w")
entry_year = tk.Entry(root, width=40)
entry_year.grid(row=11, column=1, padx=10, pady=5)
label_year = tk.Label(root, text="Dostępność czaswa:")
label_year.grid(row=12, column=0, padx=10, pady=5, sticky="w")
entry_year = tk.Entry(root, width=40)
entry_year.grid(row=12, column=1, padx=10, pady=5)
label_year = tk.Label(root, text="Czy potrzebujesz zakwaterowania?")
label_year.grid(row=13, column=0, padx=10, pady=5, sticky="w")
entry_year = tk.Entry(root, width=40)
entry_year.grid(row=13, column=1, padx=10, pady=5)
label_year = tk.Label(root, text="Rozmiar koszulki:")
label_year.grid(row=14, column=0, padx=10, pady=5, sticky="w")
entry_year = tk.Entry(root, width=40)
entry_year.grid(row=14, column=1, padx=10, pady=5)
label_year = tk.Label(root, text="Uwagi dodatkowe")
label_year.grid(row=15, column=0, padx=10, pady=5, sticky="w")
entry_year = tk.Entry(root, width=40)
entry_year.grid(row=15, column=1, padx=10, pady=5)
# Przycisk zapisu
button_save = tk.Button(root, text="Zapisz", command=lambda x:x)
button_save.grid(row=16, column=0, columnspan=2, pady=10)
# Uruchomienie pętli głównej
root.mainloop()