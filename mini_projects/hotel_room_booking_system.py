class Room:
    def __init__(self, room_no):
        self.room_no = room_no
        self.is_booked = False

class Hotel:
    def __init__(self):
        self.rooms = [Room(i) for i in range(1, 6)]

    def book_room(self):
        for room in self.rooms:
            if not room.is_booked:
                room.is_booked = True
                print(f"Room {room.room_no} booked")
                return
        print("No rooms available")

    def show_rooms(self):
        for room in self.rooms:
            status = "Booked" if room.is_booked else "Available"
            print(room.room_no, status)

hotel = Hotel()

hotel.show_rooms()
hotel.book_room()
hotel.book_room()
hotel.show_rooms()