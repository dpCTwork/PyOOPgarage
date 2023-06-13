# Your assignment for today is to create a parking garage class to get more familiar with Object Oriented Programming(OOP)

Your parking garage class should have the following methods:

## **takeTicket**

- This should decrease the amount of tickets available by 1
- This should decrease the amount of parkingSpaces available by 1

## **payForParking**

- Display an input that waits for an amount from the user and store it in a variable
- If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
- This should update the "currentTicket" dictionary key "paid" to True

## **leaveGarage**

- If the ticket has been paid, display a message of "Thank You, have a nice day"
- If the ticket has not been paid, display an input prompt for payment
- Once paid, display message "Thank you, have a nice day!"
- Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
- Update tickets list to increase by 1 (meaning add to the tickets list)

You will need a few attributes as well:

- tickets -> list
- parkingSpaces -> list
- currentTicket -> dictionary

By the end of this project each student should be able to:

- Explain and/or demonstrate creating classes
- Explain and/or demonstrate creating class methods
- Explain and/or demonstrate class instantiation

When the project is completed, commit the final changes and submit your GitHub link.
