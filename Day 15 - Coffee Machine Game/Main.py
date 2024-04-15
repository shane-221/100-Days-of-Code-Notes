from turtle import clear
from Menu import MENU
from Menu import resource
import time

coffee_machine = True
while coffee_machine:
    clear()
    # TODO 1 What would you like?
    Coffee_Type = input("What would you like? Expresso, Latte, Or Cappuccino?\n")
    Coffee_Type = str(Coffee_Type.lower())

    # TODO 4: Deduct from the resource. If too low, tell them insufficient resource.
    Total_Water = resource["water"] - MENU[Coffee_Type]["ingredients"]["water"]
    Total_Milk = resource["milk"] - MENU[Coffee_Type]["ingredients"]["milk"]
    Total_coffee = resource["coffee"] - MENU[Coffee_Type]["ingredients"]["coffee"]


    def report():
        print(f'''
                Water: {Total_Water}
                Milk: {Total_Milk}
                Coffee{Total_coffee} ''')


    if Total_Water and Total_Milk and Total_coffee > 0:

        # TODO 2: Tell them how much it is
        Coffee_Cost = int(MENU[Coffee_Type]["cost"])
        print(f"The {Coffee_Type} will cost: £{Coffee_Cost}")

        #    TODO 3: How many of each set of coins? Look through all the payment options
        #    TODO 5: Run this as a loop to keep asking again
        payment_loop = True
        while payment_loop:
            def payment_process():
                print("Please insert coins:")
                Quarters = int(input("How many quarters?:"))
                Dimes = int(input('How many dimes?:'))
                Nickles = int(input("How many nickles?:"))
                Pennies = int(input("How many pennies?:"))

                global To_Be_Paid
                To_Be_Paid = Coffee_Cost - (Quarters * 0.25) - (Dimes * 0.1) - (Nickles * 0.05) - (Pennies * 0.01)
                To_Be_Paid = round(To_Be_Paid, 2)


            #   Running the payment process and their options
            payment_process()
            global To_Be_Paid

            if To_Be_Paid > 0:
                print("Need to insert more cash!")
                print(f"${To_Be_Paid} is outstanding. Try Again!")
                time.sleep(2)
                clear()

            elif To_Be_Paid == 0:
                print("Thanks for payment. Here is your latte!")
                clear()
                payment_loop = False
            elif To_Be_Paid < 0:
                print("Thanks for your payment. You change will be released shortly!")
                clear()
                time.sleep(2)
                print(f'''
                Thanks for your payment!
                $ {To_Be_Paid * -1} has been refunded to you!''')
                payment_loop = False
    else:
        print("Not enough resources. Please choose another option !")
        clear()
    # TODO 6: Run the report of what is left over
    report_Query = input("Would you like to print the report? Yes or No?")
    if report_Query == "Yes":
        report()

    switch_off_machine = input("Would you like to switch the coffee machine off?")
    if switch_off_machine == "Yes":
        coffee_machine = False
        clear()
    else:
        clear()
