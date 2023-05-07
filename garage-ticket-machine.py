
class ParkingGarage():
    def __init__(self) -> None:
        self.ticket = []
        self.parking_space = []
        self.current_ticket ={}

    def take_ticket():
        ParkingGarage.ticket -= 1
        ParkingGarage.parking_space -=1
    #- This should decrease the amount of tickets available by 1
  #This should decrease the amount of parkingSpaces available by 1

    def pay_for_parking():
        payment =input()
        if payment == 0:
            print("Their Ticket has been paid and they have 15 min to leave")
            ParkingGarage.current_ticket #needs to show paid
        else:
            print("Your ticket value is", ParkingGarage.current_ticket)

    # Display an input that waits for an amount from the user and store it in a variable
 #If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
 #This should update the "currentTicket" dictionary key "paid" to True

    def leave_garage():
        pass
    #- If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)