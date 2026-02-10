import connection as con
import tkinter as tk
import os


def build_tkinter():
    root = tk.Tk()
    root.title("Nat lang queries")
    root.geometry(f"350x150+{(root.winfo_screenwidth() - 350) // 2}+{(root.winfo_screenheight() - 150) // 2}")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    main_frame = tk.Frame(root, bg="#F7E26B")
    main_frame.pack(expand=True, fill='both')

    input_str = tk.StringVar()

    tk.Label(main_frame, text="User inputs", bg=main_frame.__getitem__("bg"), fg="#000000",
                 font=("Segoe UI", 12, "bold")).pack(pady=10)
    tk.Entry(main_frame, width=40, textvariable=input_str).pack(pady=5)
    
    tk.Button(main_frame, text="query it", fg="#000000", bg=main_frame.__getitem__("bg"),
              font=("Segoe UI", 10, "bold")).pack(pady=5)

    root.mainloop()


def main():
    build_tkinter()


if __name__ == "__main__":
    main()