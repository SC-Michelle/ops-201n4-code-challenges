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
window.config(bg="#E67E22")
window.resizable(width=False,height=False)
window.title('FACT MACHINE')
 
l1 = tk.Label(window,text="Welcome to the Fact Machine!",font=("Arial", 25),fg="Black",bg="White")
l2= tk.Label(window,text="Click on the 'Get new Fact!' button to get a fact!",font=("Arial", 15,"bold"),fg="darkgreen",bg="#E67E22")
btn1 = tk.Button(window,text="Get new Fact!",font=("Arial", 15),command=get_fact)
btn2 = tk.Button(window,text="Exit application",font=("Arial", 15),command=exit)
t1 = tk.Text(window,width=60,height=2,font=("Arial",15),state='disabled',bg="lightgreen")
 
l1.pack()
l2.pack()
btn1.pack()
t1.pack()
btn2.pack()
 
window.mainloop()