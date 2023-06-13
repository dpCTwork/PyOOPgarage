class ParkingGarage:
    def __init__(self, tickets, spaces):
        self.tickets = list(range(1, tickets+1))
        self.spaces = list(range(1, spaces+1))
        self.currentTicket = {}

    def greet_driver(self):
        print("\nWelcome to The Nonsense Parking Garage!\n This is an imaginary parking garage where you can pay whatever you want to park as long as you want!\n")
    
    def showSpaces(self):
        print("\nCurrently available spaces:")
        print(len(self.spaces))

    def takeTicket(self):
        if len(self.tickets) == 0:
            print("Sorry, we're full. Please come back later.")
        else:
            ticket = self.tickets.pop(0)
            space = self.spaces.pop(0)
            self.currentTicket[ticket] = {'space': space, 'paid': False}
            print(f"\nYour ticket number is {ticket}.")
            while True:
                pay_now_later = input("Would you like to pay for parking now? (Y/N): ")
                if pay_now_later.lower() == 'y':
                    self.payForParking()
                    break
                elif pay_now_later.lower() == 'n':
                    break
                else:
                    print("Invalid input. Please try again.")
                    continue
            print("Thank you for choosing the David's Nonsense Parking Garage")
            print(f"Please park in space {space}.")
            print(f"There are now {len(self.spaces)} spaces available.\n")
        

    def payForParking(self):
        ticket = int(input("\nEnter your ticket number to pay: "))
        while  True:
            if ticket not in self.currentTicket:
                print("\nInvalid ticket number. Please enter the correct ticket number.")
                continue
            elif self.currentTicket[ticket]['paid']:
                print("\nTicket has already been paid! You have 15 minutes to exit the garage.")
                break
            else:
                print("\nPlease pay whatever you wish to pay.")
                payment = float(input("Enter payment amount: $"))
                self.currentTicket[ticket]['paid'] = True
                print(f"\nPayment amount of ${payment:.2f} has been accepted.")
                break

    def leaveGarage(self):
        while True:
            ticket = int(input("Enter your ticket number to leave: "))
            if ticket not in self.currentTicket:
                print("Invalid ticket number. Please try again.")
                continue
            elif not self.currentTicket[ticket]['paid']:
                payment_leave = float(input("You have not paid for this ticket yet. Please enter a payment amount: $"))
                print(f"\nPayment amount of ${payment_leave:.2f} has been accepted.")
                break
            else:
                print("\nYou have already paid for this ticket.") 
        space = self.currentTicket[ticket]['space']
        self.tickets.append(ticket)
        self.spaces.append(space)
        del self.currentTicket[ticket]
        print("Thank you and have a nice day!")

garage = ParkingGarage(3, 3)

garage.greet_driver()
garage.showSpaces()
while True:
    proceed = input("\nWould you like to proceed? (Y/N) ")
    if proceed.lower() == 'y':
        garage.takeTicket()
        if garage.currentTicket[ticket]['paid']:
            garage.leaveGarage()
        else:
            garage.payForParking()
            garage.leaveGarage()
        break
    elif proceed.lower() == 'n':
        break
    else:
        print("Invalid input. Please try again.")
        continue