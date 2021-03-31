import pickle
import random
from os import path


class Flight(object):

    def load_seats(self):
        """
            This function is used to load the seats for booking.
        :return: nothing
        """
        seats_alloc = {
            'business': {1: {'1A', '1B', '1C', '1D'}, 2: {'2A', '2B', '2C', '2D'},
                         3: {'3A', '3B', '3C', '3D'}, 4: {'4A', '4B', '4C', '4D'}},
            'economy': {1: {'1A', '1B', '1C', '1D', '1E', '1F'}, 2: {'2A', '2B', '2C', '2D', '2E', '2F'},
                        3: {'3A', '3B', '3C', '3D', '3E', '3F'}, 4: {'4A', '4B', '4C', '4D', '4E', '4F'},
                        5: {'5A', '5B', '5C', '5D', '5E', '5F'}, 6: {'6A', '6B', '6C', '6D', '6E', '6F'},
                        7: {'7A', '7B', '7C', '7D', '7E', '7F'}, 8: {'8A', '8B', '8C', '8D', '8E', '8F'},
                        9: {'9A', '9B', '9C', '9D', '9E', '9F'}, 10: {'10A', '10B', '10C', '10D', '10E', '10F'},
                        11: {'11A', '11B', '11C', '11D', '11E', '11F'}, 12: {'12A', '12B', '12C', '12D', '12E', '12F'},
                        13: {'13A', '13B', '13C', '13D', '13E', '13F'}, 14: {'14A', '14B', '14C', '14D', '14E', '14F'},
                        15: {'15A', '15B', '15C', '15D', '15E', '15F'}, 16: {'16A', '16B', '16C', '16D', '16E', '16F'},
                        17: {'17A', '17B', '17C', '17D', '17E', '17F'}, 18: {'18A', '18B', '18C', '18D', '18E', '18F'},
                        19: {'19A', '19B', '19C', '19D', '19E', '19F'}, 20: {'20A', '20B', '20C', '20D', '20E', '20F'}
                        }

        }
        if not path.exists('flight_seats'):
            self.load_pickle('flight_seats', seats_alloc)

    def load_pickle(self, file_name, objects):
        """
            This function is used to load pickle file.
        :param file_name: pickle file name
        :param objects: data to be stored in pickle file
        :return: nothing
        """
        with open(file_name, 'wb') as open_file:
            pickle.dump(objects, open_file)

    def open_pickle(self):
        """
        This function used to open pickle file
        :return: pickle file data
        """
        if path.exists('flight_seats'):
            with open('flight_seats', 'rb') as seats:
                return pickle.load(seats)
        else:
            return {}

    def check_class(self, class_pref):
        """
        This function is used to check if Travel class is present or not
        :param class_pref: takes input parameter of travel class as
            1 for Business and 2 for Economy
        :return: 1 if Travel Class is available
                0 if travel class is not available
                2 if all the seats are booked.
        """

        all_seats = self.open_pickle()
        if len(all_seats) > 0:
            if class_pref == 1 and len(all_seats['business']) == 0:
                return 0
            elif class_pref == 2 and len(all_seats['economy']) == 0:
                return 0
            else:
                return 1
        else:
            return 2

    def check_seat_pref(self, class_pref, seat_pref):
        """
        This function is used to check if preferred seat is available or not
        :param class_pref: Input parameter for travel class preference as
            1 for Business and 2 for Economy
        :param seat_pref: Input parameter for seat preference as
            1 for Window, 2 for Aisle and 3 for Middle Seats
        :return:1 if preferred seat is available
                0 if preferred seat is not available
                2 if all the seats are booked.
        """
        seats_for_pref = self.open_pickle()
        seat_list = list()
        dict_seat_pref = dict()
        if len(seats_for_pref) > 0:
            if class_pref == 1 and len(seats_for_pref['business']) > 0:
                for i in seats_for_pref['business']:
                    seat_list.append(sorted(seats_for_pref['business'][i]))
                if class_pref not in dict_seat_pref:
                    dict_seat_pref[class_pref] = seat_list
                for i in dict_seat_pref[class_pref]:
                    if seat_pref == 1:
                        if i[0].endswith('A') or i[0].endswith('D'):
                            return 1
                    elif seat_pref == 2:
                        if len([1 for j in i if j.endswith('B') or j.endswith('C')]) > 0:
                            return 1
                    else:
                        return 0

            if class_pref == 2 and len(seats_for_pref['economy']) > 0:
                for i in seats_for_pref['economy']:
                    seat_list.append(sorted(seats_for_pref['economy'][i]))
                if class_pref not in dict_seat_pref:
                    dict_seat_pref[class_pref] = seat_list
                for i in dict_seat_pref[class_pref]:
                    if seat_pref == 1:
                        if i[0].endswith('A') or i[0].endswith('F'):
                            return 1
                    elif seat_pref == 2:
                        if len([j for j in i if j.endswith('C') or j.endswith('D')]) > 0:
                            return 1
                    elif seat_pref == 3:
                        if len([1 for j in i if j.endswith('B') or j.endswith('E')]) > 0:
                            return 1
                    else:
                        return 0
        else:
            return 2

    def get_random_seat(self, pref, seat_pref):
        """
        This function is used to get random seats for booking based on users' Travel Preference
        and Seat Preference

        :param pref: Input parameter for travel class preference as
            1 for Business and 2 for Economy
        :param seat_pref: Input parameter for seat preference as
            1 for Window, 2 for Aisle and 3 for Middle Seats
        :return: Random seat number is returned
        """
        with open('flight_seats', 'rb') as seats:
            all_seats = pickle.load(seats)
        if pref == 1:
            n = random. randint(1, 4)
            if seat_pref == 1:
                return "".join([i for i in all_seats['business'][n] if i.endswith('A') or i.endswith('D')][0])
            if seat_pref == 2 or seat_pref == 3:
                return "".join([i for i in all_seats['business'][n] if i.endswith('B') or i.endswith('C')][0])
        if pref == 2:
            n = random. randint(1, 20)
            if seat_pref == 1:
                return "".join([i for i in all_seats['economy'][n] if i.endswith('A') or i.endswith('F')][0])
            if seat_pref == 2:
                return "".join([i for i in all_seats['economy'][n] if i.endswith('C') or i.endswith('D')][0])
            if seat_pref == 3:
                return "".join([i for i in all_seats['economy'][n] if i.endswith('B') or i.endswith('E')][0])
        # def reserve_seat(self):

    def reserve_seat(self, pref, seat_pref, seat):
        """
        This function is used to reserve seat and load booked seat in another pickle file
        :param pref: Input parameter for travel class preference as
            1 for Business and 2 for Economy
        :param seat_pref: Input parameter for seat preference as
            1 for Window, 2 for Aisle and 3 for Middle Seats
        :param seat: Allocated seat number to user
        :return: Nothing
        """
        reserved_sets = dict()
        if path.exists('reserved_seats'):
            with open('reserved_seats', 'rb') as res_seats:
                reserved_sets = pickle.load(res_seats)

        with open('flight_seats', 'rb') as seats:
            all_seats = pickle.load(seats)
            if pref == 1:
                if seat not in reserved_sets.values() and pref not in reserved_sets.keys():
                    reserved_sets[pref] = [seat]
                else:
                    reserved_sets[pref].append(seat)
                if seat_pref == 1:
                    if seat in all_seats['business'][int(seat[0])]:
                        all_seats['business'][int(seat[0])].discard(seat)
                elif seat_pref == 2 or seat_pref == 3:
                    if seat in all_seats['business'][int(seat[0])]:
                        all_seats['business'][int(seat[0])].discard(seat)
            if pref == 2:
                if seat not in reserved_sets.values() and pref not in reserved_sets.keys():
                    reserved_sets[pref] = [seat]
                else:
                    reserved_sets[pref].append(seat)
                if seat_pref == 1:
                    if seat in all_seats['economy'][int(seat[0])]:
                        all_seats['economy'][int(seat[0])].discard(seat)
                elif seat_pref == 2:
                    if seat in all_seats['economy'][int(seat[0])]:
                        all_seats['economy'][int(seat[0])].discard(seat)

        with open('flight_seats', 'wb') as seats:
            pickle.dump(all_seats, seats)

        if not path.exists('reserved_seats'):
            self.load_pickle('reserved_seats', reserved_sets)
        elif path.exists('reserved_seats'):
            self.load_pickle('reserved_seats', reserved_sets)
