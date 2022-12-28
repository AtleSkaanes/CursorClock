import tkinter as tk

window = tk.Tk()
window.rowconfigure(0, minsize=100, weight=1)
window.columnconfigure(1, minsize=100, weight=1)
window.config(bg="#444")


def get_entry(e):
    message = e.widget.get()
    e.widget.delete(0,tk.END)
    tk.Label(text=f"You typed: "+message+"\n").pack()

def exit_app():
    window.destroy()
    exit()

def allow_clicks():
    print("you allowed clicks")

def start_clock():
    print("started")

print("a")
window.title('Cursor Clock')
window.geometry("300x100+10+20")

exit_btn = tk.Button(text="exit (i)",command=exit_app)
exit_btn.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

click_btn = tk.Button(text="Allow clicks (u)", command=allow_clicks)
click_btn.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

toggle_btn = tk.Button(text="toggle (y)", command=start_clock)
toggle_btn.grid(row=0, column=2, sticky="ew", padx=5, pady=5)


tk.mainloop()
exit()