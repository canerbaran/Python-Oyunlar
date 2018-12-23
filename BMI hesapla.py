#my first program with sublime text\

import tkinter as tk

window = tk.Tk()

window.title("Vucut Kitle Indeksi Hesaplama Programi")

window.geometry("600x200")


def bmi_generator():
	kilo = int(entry1.get())
	boy = int(entry2.get())
	vki = (kilo /((boy/100)**2))
	return vki

def bmi_display():
	 kitle = bmi_generator()
	 kitle_display = tk.Text(master=window, height=10, width=20)
	 kitle_display.grid(column=1, row=4)
	 kitle_display.insert(tk.END, round(kitle,2))




label1 = tk.Label(text= "Bu program ile \nVucut Kitle Indeksinizi Hesaplayabilirsiniz ")
label1.grid(column=0, row=0)

label2 = tk.Label(text= "Kilonuzu kg olarak giriniz")
label2.grid(column=0, row=1)

label3= tk.Label(text= " Boyunuzu cm olarak giriniz")
label3.grid(column=0, row=2)


entry1 = tk.Entry()
entry1.grid(column=1, row=1)

entry2 = tk.Entry()
entry2.grid(column=1, row=2)

button1 = tk.Button(text="HESAPLA", command=bmi_display)
button1.grid(column=1, row=3)


window.mainloop()