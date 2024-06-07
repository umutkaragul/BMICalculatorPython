from tkinter import *

#screen
window = Tk()
window.title("BMI")
window.geometry("300x200")
window.config(padx=20, pady=30)


def bmiCalculator():
    try:
        weight_input = weight_entry.get()
        height_input = height_entry.get()

        if not weight_input or not height_input:
            raise ValueError("Please fill in the blanks!")

        if not weight_input.isdigit() or not height_input.isdigit():
            raise ValueError("Please enter only numbers!")

        weight = int(weight_input)
        height = int(height_input)

        if weight <= 0 or height <= 0:
            raise ValueError("Please enter a positive number!")

        height = height / 100
        bmi = round(weight / (height ** 2), 1)

        if bmi < 18.5:
            message.config(text=f"Your BMI: {bmi}. Underweight")
        elif bmi < 25:
            message.config(text=f"Your BMI: {bmi}. Normal Weight")
        elif bmi < 30:
            message.config(text=f"Your BMI: {bmi}. Overweight")
        elif bmi < 35:
            message.config(text=f"Your BMI: {bmi}. Obesity I")
        elif bmi < 40:
            message.config(text=f"Your BMI: {bmi}. Obesity II")
        else:
            message.config(text=f"Your BMI: {bmi}. Morbid Obesity")
    except ValueError as e:
        message.config(text=str(e))


#weight input
weight_label = Label(text="Enter Your Weight(kg)")
weight_label.pack()

weight_entry = Entry()
weight_entry.pack()

#height input
height_label = Label(text="Enter Your Height(cm)")
height_label.pack()

height_entry = Entry()
height_entry.pack()

#button
calculate_button = Button(text="Calculate", command=bmiCalculator)
calculate_button.pack()

#message
message = Label(text="")
message.pack()

window.mainloop()
