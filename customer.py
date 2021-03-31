import pickle
from os import path


class Customer(object):

    def load_customer_data(self, seat_book):
        """
            This function is used to load customer data in pickle file.
        :param seat_book: Input parameter to load booked seat details
        :return: Nothing
        """
        with open('customer_data', 'wb') as book:
            pickle.dump(seat_book, book)

    def book_seat(self, seat_book, booking_id):
        """
        This function is used to book seat
        :param seat_book: Input parameter having booked seat details
        :param booking_id: Booking Id of seat booked by customer
        :return: Nothing
        """
        if path.exists('customer_data'):
            with open('customer_data', 'rb') as res_seat:
                reserve_seat = pickle.load(res_seat)
            if booking_id not in reserve_seat:
                reserve_seat.update(seat_book)
            self.load_customer_data(reserve_seat)
        else:
            self.load_customer_data(seat_book)

    def get_ticket(self, bkg_id):
        """
        This function returns ticket details based on booking id
        :param bkg_id: Input parameter to get the booking id
        :return: Ticket details
        """
        customer = dict()
        if path.exists('customer_data'):
            with open('customer_data', 'rb') as user_seat:
                customer = pickle.load(user_seat)
        if bkg_id in customer:
            return customer[bkg_id]
        else:
            print("Invalid Booking Id..!!")
            return {}
