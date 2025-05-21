import tkinter as tk

calculation = ""



def add_calculator(symbol):
    global calculation
    calculation += str(symbol)
    result_box.delete(1.0, "end")
    result_box.insert(1.0, calculation)



def evaluate_calculator():
    global calculation
    try:
        calculation = str(eval(calculation))
        result_box.delete(1.0, "end")
        result_box.insert(1.0, calculation)
    except:
        clear_field()
        result_box.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    result_box.delete(1.0, "end")

root = tk.Tk()              # ক্যালকুলেটরের উইনডো বানানোর জন্য
root.geometry("340x285")   # ক্যালকুলেটরের সাইজ দেওয়ার জন্য
root.config(bg="black")
result_box = tk.Text(root, height=2, width= 19, font=("Arial", 25), bg="#96a89b")  # রেসাল্ট বক্স বানানোর জন্য
result_box.grid(columnspan=7)

btn_1 = tk.Button(root, text="1",command=lambda:add_calculator(1),  width=4, font="Arial", bg="#9c883b")
btn_1.grid(row=3, column=1)
btn_2 = tk.Button(root, text="2",command=lambda:add_calculator(2), width=4, font="Arial", bg="#9c883b")
btn_2.grid(row=3, column=2)
btn_3 = tk.Button(root, text="3",command=lambda:add_calculator(3), width=4, font="Arial", bg="#9c883b")
btn_3.grid(row=3, column=3)
btn_4 = tk.Button(root, text="4",command=lambda:add_calculator(4), width=4, font="Arial", bg="#9c883b")
btn_4.grid(row=4, column=1)
btn_5 = tk.Button(root, text="5",command=lambda:add_calculator(5), width=4, font="Arial", bg="#9c883b")
btn_5.grid(row=4, column=2)
btn_6 = tk.Button(root, text="6",command=lambda:add_calculator(6), width=4, font="Arial", bg="#9c883b")
btn_6.grid(row=4, column=3)
btn_7 = tk.Button(root, text="7",command=lambda:add_calculator(7), width=4, font="Arial", bg="#9c883b")
btn_7.grid(row=5, column=1)
btn_8 = tk.Button(root, text="8",command=lambda:add_calculator(8), width=4, font="Arial", bg="#9c883b")
btn_8.grid(row=5, column=2)
btn_9 = tk.Button(root, text="9",command=lambda:add_calculator(9), width=4, font="Arial", bg="#9c883b")
btn_9.grid(row=5, column=3)
btn_0 = tk.Button(root, text="0",command=lambda:add_calculator(0), width=4, font="Arial", bg="#9c883b")
btn_0.grid(row=6, column=2)

btn_eq = tk.Button(root, text="=",command= lambda:evaluate_calculator(), width=4, font="Arial", bg="#9c883b")
btn_eq.grid(row=6, column=3)

btn_p = tk.Button(root, text="+",command=lambda:add_calculator("+"), width=4, font="Arial", bg="#9c883b")
btn_p.grid(row=3, column=4)
btn_m = tk.Button(root, text="-",command=lambda:add_calculator("-"), width=4, font="Arial", bg="#9c883b")
btn_m.grid(row=4, column=4)
btn_g = tk.Button(root, text="*",command=lambda:add_calculator("*"), width=4, font="Arial", bg="#9c883b")
btn_g.grid(row=5, column=4)
btn_d = tk.Button(root, text="/",command=lambda:add_calculator("/"), width=4, font="Arial", bg="#9c883b")
btn_d.grid(row=6, column=4)
btn_mod = tk.Button(root, text="%",command=lambda:add_calculator("%"), width=4, font="Arial", bg="#9c883b")
btn_mod.grid(row=6, column=1)


btn_ac = tk.Button(root, text="AC",command=lambda:clear_field(), width=16, font="Arial", bg="#910713")
btn_ac.grid(columnspan=7)



root.mainloop()