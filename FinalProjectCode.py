import randfacts
def get_fact():
    t1.config(state='normal')
    t1.delete('1.0', tk.END)
    f = randfacts.getFact(False)
    t1.insert(tk.END,f)
    t1.config(state='disabled')
     
def exit():
    window.destroy()
 
import tkinter as tk
window = tk.Tk()
window.geometry("700x250")
window.config(bg="#FF1493")
window.resizable(width=False,height=False)
window.title('FACT MACHINE')
 
l1 = tk.Label(window,text="Welcome to the Fact Machine!",font=("Comix Sans MS", 25),fg="White",bg="lightpink")
l2= tk.Label(window,text="Click on the 'Get new Fact!' button to get a fact!",font=("Comix Sans MS", 15,"bold"),fg="white",bg="#FF1493")
btn1 = tk.Button(window,text="Get new Fact!",font=("Comix Sans MS", 15),command=get_fact)
btn2 = tk.Button(window,text="Exit application",font=("Comix Sans MS", 15),command=exit)
t1 = tk.Text(window,width=60,height=2,font=("Comix Sans MS",15),state='disabled',bg="lightpink")

l1.pack()
l2.pack()
btn1.pack()
t1.pack()
btn2.pack()
 
window.mainloop()