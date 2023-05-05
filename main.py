from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=150)
window.config(pady=10,padx=10)

weight_label = Label(text="Enter Your Weight (kg)")
weight_label.config(pady=5)
weight_label.pack()

weight_entry = Entry(width=20)
weight_entry.pack()

height_label = Label(text="Enter Your Height (cm)")
height_label.config(pady=5)
height_label.pack()

height_entry = Entry(width=20)
height_entry.pack()

def bmi_calc():
    height = height_entry.get()
    weight = weight_entry.get()

    if weight == "" or height == "":
        result_label.config(text="Enter both weight and height!")
    else:
        try:
            bmi = float(weight) / ((float(height) / 100) ** 2)
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Enter a valid number!")

def write_result(bmi):
    result_string = f"Your BMI is {round(bmi, 2)}. You are "
    if bmi <= 16:
        result_string += "severely thin!"
    elif 16 < bmi <= 17:
        result_string += "moderately thin!"
    elif 17 < bmi <= 18.5:
        result_string += "mild thin!"
    elif 18.5 < bmi <= 25:
        result_string += "normal weight"
    elif 25 < bmi <= 30:
        result_string += "overweight"
    elif 30 < bmi <= 35:
        result_string += "obese class 1"
    elif 35 < bmi <= 40:
        result_string += "obese class 2"
    else:
        result_string += "obese class 3"
    return result_string

calculate_button = Button(text="Calculate",command=bmi_calc)
calculate_button.pack()
result_label = Label()
result_label.pack()

window.mainloop()