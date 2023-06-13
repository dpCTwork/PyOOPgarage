class ParkingGarage:
    def __init__(self, tickets, spaces):
        self.tickets = list(range(1, tickets+1))
        self.spaces = list(range(1, spaces+1))
        self.currentTicket = {}

    def greet_driver(self):
        print("\nWelcome to The PyOOP Garage!\n This is an imaginary parking garage where you can pay whatever you want to park as long as you want!\n")
    
    def showSpaces(self):
        print(f"\nCurrently available spaces: {len(self.spaces)}")

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
            print(f"\nPlease take ticket #{ticket} and park in space #{space}. Thank you.")
        

    def payForParking(self):
        while  True:
            ticket = int(input("What is your ticket number? ")) 
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
        ticket = int(input("Enter your ticket number to verify payment and leave: "))
        if not self.currentTicket[ticket]['paid']:
            payment_leave = float(input("You have not paid for this ticket yet. Please enter a payment amount: $"))
            print(f"\nPayment amount of ${payment_leave:.2f} has been accepted.")
        else:
            print(f"\nThis ticket has been paid.")
        space = self.currentTicket[ticket]['space']
        self.tickets.append(ticket)
        self.spaces.append(space)
        del self.currentTicket[ticket]
        print("Thank you for choosing The PyOOP Garage. Have a nice day!")

garage = ParkingGarage(3, 3)

garage.greet_driver()
garage.showSpaces()
while True:
    proceed = input("\nWould you like to proceed? (Y/N) ")
    if proceed.lower() == 'y':
        garage.takeTicket()
        print("\n .... 2 hours later, time to leave ....")
        garage.payForParking()
        print(f"\n......... driving to the exit .........")
        print(".........")
        print(".........")
        garage.leaveGarage()
        break
    elif proceed.lower() == 'n':
        break
    else:
        print("Invalid input. Please try again.")
        continue