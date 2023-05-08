
class ParkingGarage():
    def __init__(self) -> None:
        self.ticket = 50
        self.parking_space = 50
        self.current_ticket ={}

    def take_ticket(self):
        self.ticket -= 1
        self.parking_space -=1
        self.current_ticket['paid'] = False
# This should decrease the amount of tickets available by 1
#  This should decrease the amount of parkingSpaces available by 1

    def pay_for_parking(self):
        payment =input("Enter the payment amount")
        if payment == int(0):
            print("Their Ticket has been paid and they have 15 min to leave")
            self.current_ticket['paid'] = True
        else:
            print("Your ticket value is", self.current_ticket)

# Display an input that waits for an amount from the user and store it in a variable
# If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# This should update the "currentTicket" dictionary key "paid" to True



# GABE: "LEAVE GARAGE" START HERE BELOW------------------------------------


    def leave_garage(self):
#####GABE LINE BREAK TO HELP READ######
        if self.current_ticket['paid'] == True:     # Check *IF* the ticket has been paid
            print("Thank You, have a nice day!")    # DISPLAY message
            self.parking_space += 1                 # INCREASE the parking space by 1
            self.ticket += 1                        # INCREASE the ticket by 1
#####GABE LINE BREAK TO HELP READ######
        else: 
            payment = input("Please pay for your ticket: ")     #ASK for payment
            if payment == "0":
                print("Thank You, have a nice day!")    # DISPLAY message
                self.parking_space += 1                 # INCREASE the parking space by 1
                self.ticket += 1                        # INCREASE the ticket by 1
                self.current_ticket['paid'] = True      # UPDATE the current ticket to PAID
#####GABE LINE BREAK TO HELP READ######
        else:
        print("Payment not accepted. Please try again.")


#- If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)



        ParkingGarage()