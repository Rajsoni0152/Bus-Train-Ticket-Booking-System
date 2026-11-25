
seats = {}
bookings = {}

for i in range(1, 11):
    seats[i] = "Available"

while True:

    print("\n==== BUS/TRAIN BOOKING SYSTEM ====")
    print("1. View Seats")
    print("2. Book Ticket")
    print("3. View Bookings")
    print("4. Cancel Ticket")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":

        for seat, status in seats.items():
            print("Seat", seat, ":", status)

    
    elif choice == "2":

        seat_input = input("Enter seat number (1-10): ")

        if seat_input.isdigit():

            seat_no = int(seat_input)

            if seat_no in seats:

                if seats[seat_no] == "Available":

                    name = input("Enter passenger name: ")

                    seats[seat_no] = "Booked"

                    bookings[seat_no] = {
                        "name": name,
                        "price": 500
                    }

                    print("\nBooking successful!")
                    print("Passenger Name:", name)
                    print("Seat Number:", seat_no)
                    print("Ticket Price: Rs. 500")

                else:
                    print("Seat is already booked.")

            else:
                print("Invalid seat number! Please enter 1-10.")

        else:
            print("Please enter a valid number!")

    elif choice == "3":

        print("\n===== BOOKING DETAILS =====")

        if len(bookings) == 0:
            print("No bookings available.")

        else:
            for seat, details in bookings.items():
                print("Passenger:", details["name"])
                print("Seat:", seat)
                print("Price: Rs.", details["price"])
                print("----------------------")

    elif choice == "4":

        seat_input = input("Enter seat number to cancel: ")

        if seat_input.isdigit():

            seat_no = int(seat_input)

            if seat_no in bookings:

                name = bookings[seat_no]["name"]

                refund = 500 * 80 / 100

                del bookings[seat_no]
                seats[seat_no] = "Available"

                print("\nCancellation successful!")
                print("Passenger:", name)
                print("Refund Amount: Rs.", refund)

            else:
                print("No booking found for this seat.")

        else:
            print("Please enter a valid number!")

    elif choice == "5":
        print("Thank you for using our system!")
        break

    else:
        print("Invalid choice!")