#VENTANA CON CUADRO CON RELOJ O VENTANA DE WELCOME


from tkinter import Tk, Label
#from datetime import datetime

window = Tk()
window.title("Digital Clock")
window.geometry("600x300")
window.configure(bg="red")

label = Label(window, text="Welcome!",font=("Arial Black",78,"bold"), bg="red", fg="white")
label.pack(pady=100)

#def clock():
    #time=datetime.now().strftime("%H:%M:%S")
    #label.configure(text=time)
    #label.after(500,clock)

#clock()
window.mainloop()

