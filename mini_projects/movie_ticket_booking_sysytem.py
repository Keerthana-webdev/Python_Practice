class Movie:
    def __init__(self, seats):
        self.seats = ["Free"] * seats

    def book_seat(self, index):
        if self.seats[index] == "Free":
            self.seats[index] = "Booked"
            print("Seat booked")
        else:
            print("Already booked")

    def show_seats(self):
        print(self.seats)

movie = Movie(5)

movie.show_seats()
movie.book_seat(2)
movie.book_seat(2)
movie.show_seats()