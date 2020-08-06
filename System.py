from tkinter import *
import time, os, requests, datetime
from tkinter import ttk

# Calc Funcs
def btn(number):
    global operator
    operator = operator + str(number)
    txt_input.set(operator)

def equal():
    global operator
    sumup = float(eval(operator))
    txt_input.set(sumup)
    operator = ''

def clear():
    global operator
    operator = ''
    txt_input.set('')
    Display.insert(0, 'Cleared...')


# Other Funcs
meal_dict = {'Fried Rice':5.0, 'Fried Rice & Chicken':8.5, 'Durum':3.5, 'Cheese Burger':4.0, 'Pepper Chicken':3.5}
drink_dict = {'Cola':2.0, 'Limo':1.5, 'Apfel Schorle':1.5, 'Wein':3.0, 'Bier':0.95}
room_dict = {'normal':25.0, 'vip':60.0}
dev_cost = 3.0

def total_result():
    # Meals
    meal = meal_selector.get()
    meal_qty = int(meal_qty_indicator.get())
    if meal_qty:
        meal_tot = float(meal_dict.get(meal) * meal_qty)
        cost.set(meal_tot)
    else:
        cost.set(0.0)

    # Drinks
    drink = drink_selector.get()
    drink_qty = int(drink_qty_indicator.get())
    if drink_qty:
        drink_tot = float(drink_dict.get(drink) * drink_qty)
        Drinks.set(drink_tot)
    else:
        Drinks.set(0.0)

    # Room + Delivery
    room = radio1.get()
    if room!=3:
        if room == 2:
            temp = room_dict.get('normal')
            Room_cost.set(temp)
            if chkb1.get()==1:
                temp_d = round(temp * (3.5 / 100), 2)
                Devcost.set(temp_d)
            else:
                Devcost.set(0.0)

        elif room == 1:
            temp = room_dict.get('vip')
            Room_cost.set(temp)
            if chkb1.get()==1:
                temp_d = round(temp * (3 / 100), 2)
                Devcost.set(temp_d)
            else:
                Devcost.set(0.0)

    elif chkb1.get()==1:
        Devcost.set(dev_cost)
        Room_cost.set(0.0)
    else:
        Devcost.set(0.0)
        Room_cost.set(0.0)

    # Service Charge
    temp_s = float(txtMeal1.get()) + float(txtDrink1.get()) + float(txtRoom.get()) + float(txtDev.get())
    service_cost.set(round((temp_s * 0.015), 2))

    # Total Charge
    temp_t = round(temp_s + float(txtService.get()), 2)
    total_cost.set(temp_t)

    # Main Screen
    temp_bigscreen = 'Grand Total: €'+ str(temp_t)
    Display.delete(0, END)
    Display.insert(0, temp_bigscreen)
    if temp_t == 0:
        Display.delete(0, END)
        Display.insert(0, 'Please Make an order...')

#currency coverter
def currency_coverter():
    base_url = os.environ['MY_CURRENCY_API']
    currency_dict = {'Yuan': 'CNY', 'US Dollar': 'USD', 'Cedi':'GHS', 'Naira': 'NGN', 'Canadian Dollar': 'CAD', 'British Pounds': 'GBP'}
    response = requests.get(base_url)
    data = response.json()

    # fecht currency and amount
    amt = txtAmount.get()
    curr = txtCountry.get()
    if curr == 'Choose a Currency':
        Display.delete(0, END)
        Display.insert(0, 'Please choose a Currency')

    curr_ = currency_dict.get(curr)

    if data['success'] is True:
        val = round(float(amt) * data['rates'].get(curr_), 2)
        temp = curr + ': ' + str(val)
        Display.delete(0, END)
        Display.insert(0, temp)
    else:
        Display.delete(0, END)
        Display.insert(0, 'Please connect to the Internet....')

# Resetting Button
def rest():
    clear()
    Display.delete(0, END)
    Display.insert(0, 'Hello! Welcome')
    meal_selector.set(value='Available Delicacies')
    meal_qty_indicator.delete(0, END)
    meal_qty_indicator.insert(0,0)
    drink_selector.set(value='Available Drinks')
    drink_qty_indicator.delete(0, END)
    drink_qty_indicator.insert(0, 0)
    chkb1.set(0)
    radio1.set(3)
    txtCountry.set(value='Choose a Currency')
    cost.set(0.0)
    Drinks.set(0.0)
    Devcost.set(0.0)
    Room_cost.set(0.0)
    service_cost.set(0.0)
    total_cost.set(0.0)
    txtAmount.delete(0, END)
    txtAmount.insert(0, 0)

def hotel():
    Display.delete(0, END)
    Display.insert(0, 'Hotel Management System')

def powered():
    Display.delete(0, END)
    Display.insert(0, 'Powered by PYthon...')

def reset():
    Display.delete(0, END)
    Display.insert(0, 'System Resetting....')
    Display.after(2000, hotel)
    Display.after(4000, powered)
    Display.after(4000, rest)


# Clear Button
def clear_screen():
    Display.delete(0, END)
    cost.set('')
    Drinks.set('')
    Devcost.set('')
    Room_cost.set('')
    service_cost.set('')
    total_cost.set('')

# Exit Button
def stop():
    root.destroy()

def close_app():
    Display.delete(0, END)
    Display.insert(0, 'Clearing Memory...')
    Display.after(3000, stop)

# Time
def digital_clock():
    d = datetime.datetime.now()
    today = d.strftime('%B %d, %Y')
    current_time = time.strftime('%H:%M:%S') + ' ' +today
    lblInfo.config(text=current_time)
    lblInfo.after(200, digital_clock)

root = Tk(className='Hotel Management System')
root.geometry('1200x700+0+0')

# Windows partition - Crating spaces for different part of the gui
Tops = Frame(root, width=1200, height=100, bg='blue', relief=SUNKEN)
Tops.pack(side=TOP)  # add frame to gui window

f1_ = Frame(root, width=10, height=600, relief=SUNKEN)
f1_.pack(side=LEFT)

f1 = Frame(root, width=800, height=600, relief=SUNKEN)
f1.pack(side=LEFT)

f2_ = Frame(root, width=10, height=600, relief=SUNKEN)
f2_.pack(side=RIGHT)

f2 = Frame(root, width=300, height=600, relief=SUNKEN)
f2.pack(side=RIGHT)

f3 = Frame(root, width=35, height=600, relief=SUNKEN)
f3.pack(side=LEFT)

f4 = Frame(root, width=100, height=600, relief=SUNKEN)
f4.pack(side=LEFT)

# Main Screen
txt_input = StringVar(value='Master Python Today................')
Display = Entry(Tops, font=('arial', 97), fg='white', bd=10, bg='#1a4b66', justify='right', textvariable=txt_input)
Display.grid(columnspan=4)

# Date and Time
localtime = time.asctime(time.localtime(time.time()))
lblInfo = Label(f2, font=('arial', 20, 'bold'), fg='dark blue', bd=10, anchor=W)
lblInfo.grid(row=0, column=0, columnspan=4)
digital_clock()

# Calculator
operator = ''
button7 = Button(f2, padx=20, pady=15, bd=8, font=('arial', 30, 'bold'), text='7', command=lambda: btn(7)).grid(row=1, column=0)
button8 = Button(f2, padx=20, pady=15, bd=8, font=('arial', 30, 'bold'), text='8', command=lambda: btn(8)).grid(row=1, column=1)
button9 = Button(f2, padx=20, pady=15, bd=8, font=('arial', 30, 'bold'), text='9', command=lambda: btn(9)).grid(row=1, column=2)
button_c = Button(f2, padx=16, pady=15, bd=8, font=('arial', 30, 'bold'), text='C', command=clear ).grid(row=1, column=3)
button4 = Button(f2, padx=20, pady=15, bd=8, font=('arial', 30, 'bold'), text='4', command=lambda: btn(4)).grid(row=2, column=0)
button5 = Button(f2, padx=20, pady=15, bd=8, font=('arial', 30, 'bold'), text='5', command=lambda: btn(5)).grid(row=2, column=1)
button6 = Button(f2, padx=20, pady=15, bd=8, font=('arial', 30, 'bold'), text='6', command=lambda: btn(6)).grid(row=2, column=2)
button_plus = Button(f2, padx=18, pady=15, bg='#e37b2b', bd=8, font=('arial', 30, 'bold'), text='+', command=lambda: btn('+')).grid(row=2, column=3)
button1 = Button(f2, padx=20, pady=15, bd=8, font=('arial', 30, 'bold'), text='1', command=lambda: btn(1)).grid(row=3, column=0)
button2 = Button(f2, padx=20, pady=15, bd=8, font=('arial', 30, 'bold'), text='2', command=lambda: btn(2)).grid(row=3, column=1)
button3 = Button(f2, padx=20, pady=15, bd=8, font=('arial', 30, 'bold'), text='3', command=lambda: btn(3)).grid(row=3, column=2)
button_minus = Button(f2, padx=22, pady=15, bg='#e37b2b', bd=8, font=('arial', 30, 'bold'), text='-', command=lambda: btn('-')).grid(row=3, column=3)
button0 = Button(f2, padx=20, pady=15, bd=8, font=('arial', 30, 'bold'), text='0', command=lambda: btn(0)).grid(row=4, column=0)
button_dot = Button(f2, padx=24, pady=15, bd=8, font=('arial', 30, 'bold'), text='.', command=lambda: btn('.')).grid(row=4, column=1)
button_div = Button(f2, padx=24, pady=15, bg='#e37b2b', bd=8, font=('arial', 30, 'bold'), text='/', command=lambda: btn('/')).grid(row=4, column=2)
button_mul = Button(f2, padx=18.5, pady=15, bg='#e37b2b', bd=8, font=('arial', 30, 'bold'), text='x', command=lambda: btn('*')).grid(row=4, column=3)
button_eq = Button(f2, padx=52.3, pady=15, bd=8, font=('arial', 30, 'bold'), text='=', command=equal).grid(row=5, column=0,columnspan=2)
button_openbrac = Button(f2, padx=23, pady=15, bd=8, font=('arial', 30, 'bold'), text='(', command=lambda: btn('(')).grid(row=5, column=2)
button_closebrac = Button(f2, padx=22.5, pady=15, bd=8, font=('arial', 30, 'bold'), text=')', command=lambda: btn(')')).grid(row=5, column=3)

# Meals
meal_qty_int = IntVar()
meal_desc = StringVar(value='Available Delicacies')

meal_label = Label(f1, font=('arial', 16, 'bold'), text='Choose Meal', bd=10, anchor=W).grid(row=0, column=0)
meal_selector = ttk.Combobox(f1, font=('arial', 16, 'bold'), textvariable=meal_desc)
meal_selector['values'] = ('Fried Rice', 'Fried Rice & Chicken', 'Durum', 'Cheese Burger', 'Pepper Chicken')
meal_selector.grid(row=0, column=1)

meal_qty_label = Label(f1, font=('arial', 16, 'bold'), text='Qty of Meal', bd=10, anchor=W).grid(row=1, column=0)
meal_qty_indicator = Entry(f1, font=('arial', 16, 'bold'), textvariable=meal_qty_int, bg='white', bd=5, justify='right')
meal_qty_indicator.grid(row=1, column=1)

# Drinks
drink_qty_int = IntVar()
drink_desc = StringVar(value='Available Drinks')

drink_label = Label(f1, font=('arial', 16, 'bold'), text='Choose Drink', bd=10, anchor=W).grid(row=2, column=0)
drink_selector = ttk.Combobox(f1, font=('arial', 16, 'bold'), textvariable=drink_desc)
drink_selector['values'] = ('Cola', 'Limo', 'Apfel Schorle', 'Wein', 'Bier')
drink_selector.grid(row=2, column=1)

drink_qty_label = Label(f1, font=('arial', 16, 'bold'), text='Qty of Drink', bd=10, anchor=W).grid(row=3, column=0)
drink_qty_indicator = Entry(f1, font=('arial', 16, 'bold'), textvariable=drink_qty_int, bg='white', bd=5,
                            justify='right')
drink_qty_indicator.grid(row=3, column=1)

# Order Delivery
chkb1 = IntVar()
lblHomeDev = Label(f1, font=('arial', 16, 'bold'), text='Order Delivery', bd=10, anchor=W).grid(row=4, column=0)
chkHomeDev = Checkbutton(f1, font=('arial', 16, 'bold'), text='Yes', variable=chkb1).grid(row=4, column=1)

# Book a Room
radio1 = IntVar()
radio1.set(3)
lblRoom = Label(f1, font=('arial', 16, 'bold'), text='Book a Room', bd=10, anchor=W).grid(row=5, column=0)
vip_rad = Radiobutton(f1, font=('arial', 16, 'bold'), text='VIP', variable=radio1, value=1).grid(row=5, column=1,
                                                                                                 sticky=W)
norm_rad = Radiobutton(f1, font=('arial', 16, 'bold'), text='Normal', variable=radio1, value=2).grid(row=5,
                                                                                                     column=1)
no_rad = Radiobutton(f1, font=('arial', 16, 'bold'), text='No', variable=radio1, value=3).grid(row=5, column=1,
                                                                                               sticky=E)

# Cost Display
cost = StringVar()
lblMeal1 = Label(f1, font=('arial', 16, 'bold'), text='Cost of Meal (€)', bd=16).grid(row=0, column=2)
txtMeal1 = Entry(f1, font=('arial', 16, 'bold'), textvariable=cost, bd=5, fg='white', bg='blue', insertwidth=4,
                 justify='right')
txtMeal1.grid(row=0, column=3)

Drinks = StringVar()
lblDrink1 = Label(f1, font=('arial', 16, 'bold'), text='Cost of Drink (€)', bd=16).grid(row=1, column=2)
txtDrink1 = Entry(f1, font=('arial', 16, 'bold'), textvariable=Drinks, bd=5, fg='white', bg='blue', insertwidth=4,
                  justify='right')
txtDrink1.grid(row=1, column=3)

Devcost = StringVar()
lblDev = Label(f1, font=('arial', 16, 'bold'), text='Delivery Cost (€)', bd=16).grid(row=2, column=2)
txtDev = Entry(f1, font=('arial', 16, 'bold'), textvariable=Devcost, bd=5, fg='white', bg='blue', insertwidth=4,
               justify='right')
txtDev.grid(row=2, column=3)

Room_cost = StringVar()
lblRoom = Label(f1, font=('arial', 16, 'bold'), text='Cost of Room (€)', bd=16).grid(row=3, column=2)
txtRoom = Entry(f1, font=('arial', 16, 'bold'), textvariable=Room_cost, bd=5, fg='white', bg='blue', insertwidth=4,
                justify='right')
txtRoom.grid(row=3, column=3)

service_cost = StringVar()
lblService = Label(f1, font=('arial', 16, 'bold'), text='Service Fee (€)', bd=16).grid(row=4, column=2)
txtService = Entry(f1, font=('arial', 16, 'bold'), textvariable=service_cost, bd=5, fg='white', bg='blue',
                   insertwidth=4, justify='right')
txtService.grid(row=4, column=3)

total_cost = StringVar()
lblTotal = Label(f1, font=('arial', 16, 'bold'), text='Total Cost (€)', bd=16).grid(row=5, column=2)
txtTotal = Entry(f1, font=('arial', 16, 'bold'), textvariable=total_cost, bd=5, fg='white', bg='blue',
                 insertwidth=4, justify='right')
txtTotal.grid(row=5, column=3)

# Currency Converter
var1 = IntVar()
indicator = StringVar(value='Choose a Currency')

lblCunCo = Label(f1, font=('arial', 16, 'bold italic'),
                 text='---------------------------------------Currency Converter--------------------------------------',
                 bd=16)
lblCunCo.grid(row=6, column=0, columnspan=4)

lblCountry = Label(f1, font=('arial', 16, 'bold'), text='Currency', bd=16, anchor=W).grid(row=7, column=0)
txtCountry = ttk.Combobox(f1, font=('arial', 16, 'bold'), textvariable=indicator)
txtCountry['value'] = ('Yuan', 'US Dollar', 'Cedi', 'Naira', 'Canadian Dollar', 'British Pounds')
txtCountry.grid(row=7, column=1)

lblAmount = Label(f1, font=('arial', 16, 'bold'), text='Amount (€)', bd=16, anchor=W).grid(row=7, column=2)
txtAmount = Entry(f1, font=('arial', 16, 'bold'), textvariable=var1, bd=5, bg='white', insertwidth=4, justify='right')
txtAmount.grid(row=7, column=3)

# Control Buttons
btConvert = Button(f1, padx=52.3, pady=15, bd=8, font=('arial', 16, 'bold'), text='Convert', command=currency_coverter).grid(row=8, column=2)

btTotal = Button(f4, padx=53, pady=15, bd=8, font=('arial', 16, 'bold'), text='Total', command=total_result).grid(row=0, column=0)
btScreen = Button(f4, padx=51, pady=15, bd=8, font=('arial', 16, 'bold'), text='Clear', command=clear_screen).grid(row=1, column=0)
btReset = Button(f4, padx=49, pady=15, bd=8, font=('arial', 16, 'bold'), text='Reset', command=reset).grid(row=2, column=0)
btExit = Button(f4, padx=56, pady=15, bd=8, font=('arial', 16, 'bold'), text='Exit', command=close_app).grid(row=3, column=0)

# Logo
photo = PhotoImage(file='python.jpg')
smaller_image = photo.subsample(10, 10)
myphoto = Label(f1, image=smaller_image).grid(row=8, column=0)

root.mainloop()
