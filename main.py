import SeatEnum
import uuid
from customer import Customer
from flight import Flight

if __name__ == '__main__':
    booked_seat = dict()
    cont = 'Y'
    fl = Flight()
    cus = Customer()
    fl.load_seats()
    user_pref = 0
    user_seat = 0
    pref = 0
    seat_pref = 0
    while cont.lower() != 'n':
        user_choice = int(input("1. Book Ticket\n2. View Ticket\nEnter your choice:"))
        if user_choice == 1:
            name = input("Enter your full name: ")
            while user_pref != 1:
                pref = int(input("Enter your class preference from below \n1. Business\t2. Economy\n"))
                # Check if preferred travel class is available or not
                user_pref = fl.check_class(pref)
                if user_pref == 0:
                    print("Sorry {} class seats are booked..!!".format(SeatEnum.AirClass(pref).name))
                elif user_pref == 2:
                    print("Sorry all the seats are booked..!!")
                    exit()
            while user_seat != 1:
                seat_pref = int(input("Enter your seat preference from below\n1. Window\t2. Aisle\t3. Middle\n"))
                # Check if preferred seat is available or not
                user_seat = fl.check_seat_pref(pref, seat_pref)
                if user_seat == 0:
                    print("Sorry {} seats are booked..!!".format(SeatEnum.SeatSelection(seat_pref).name))
                elif user_seat == 2:
                    print("Sorry all the seats are booked..!!")
                    exit()
            # Generate unique booking id
            booking_id = uuid.uuid4()
            print("Congratulations..!! Your seat is booked\nBooking id: {}\n"
                  "Please note down booking id to view ticket.".format(booking_id.node))
            # Get random seat based on travel preference and seat preference
            seat_no = fl.get_random_seat(pref, seat_pref)
            if booking_id not in booked_seat.values():
                booked_seat[booking_id.node] = {'name': name, 'pref': SeatEnum.AirClass(pref).name,
                                                'seat_pref': SeatEnum.SeatSelection(seat_pref).name,
                                                'seat_no': seat_no}
            # Reserve seat into "reserved_seats" pickle file
            fl.reserve_seat(pref, seat_pref, seat_no)
            # Book the seat and load into customer pickle file.
            cus.book_seat(booked_seat, booking_id.node)
        elif user_choice == 2:
            try:
                book_id = int(input("Enter your booking id: "))
                # Get ticket details
                customer = cus.get_ticket(book_id)
                if len(customer) > 0:
                    print('*' * 30)
                    print("Traveller Name:  {}\nTravel Class:    {}\nSeat Preference:  {}\nSeat Number:  {}"
                          .format(customer['name'], customer['pref'], customer['seat_pref'], customer['seat_no']))
                    print('*' * 30)
            except ValueError as ve:
                print("Invalid Booking Id..!!")
        cont = input("Do you want to continue?(Y/N):")
        if cont.lower() == 'y':
            user_pref = 0
            user_seat = 0
