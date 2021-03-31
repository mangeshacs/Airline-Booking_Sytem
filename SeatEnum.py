import enum

class SeatSelection(enum.Enum):
    Window = 1
    Aisle = 2
    Middle = 3

class AirClass(enum.Enum):
    Business = 1
    Economy = 2

# print(AirClass(2).name)