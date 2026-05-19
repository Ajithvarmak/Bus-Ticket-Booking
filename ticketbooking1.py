# Login Requirement
def login():
    print("Welcome to the Ticket Booking System!")
    print("Cumbum To Coimbatore Route Bus Here")
    while True:
        user = input("Enter your username: ")
        password = input("Enter your password: ")
        if user != "" and password != "":
            print("Login successful!")
            search_bus()
            break
        else:
            print("Login failed!")
            break

# Search Requirement
def search_bus():
    print("Search for Available Buses in Cumbum To Coimbatore Route")
    place = ["cumbum", "theni", "dindigal", "palladam", "sulur", "coimbatore"]
    print("Available Stops:", place)
    From = input("Enter the starting point: ").lower()
    To = input("Enter a Destination: ").lower()
    print("Available Date")
    print("1: 12/07/2027")
    date = input("Choose the date: ")
    if date == "1":
        date = "12/07/2027"
    else:
        print("Invalid date")
        return
    if From in place and To in place and From != To:
        print("Bus Available From", From, "To", To)
        bus_time(From, To, date)
    else:
        print("Bus Not Available")

# Bus time requirement
def bus_time(From, To, date):
    time_schedule = {
        ("cumbum", "theni"): ["12.00", "12.45"],
        ("cumbum", "dindigal"): ["12.00", "2.30"],
        ("cumbum", "palladam"): ["12.00", "4.00"],
        ("cumbum", "sulur"): ["12.00", "4.30"],
        ("cumbum", "coimbatore"): ["12.00", "5.00"],
        ("theni", "dindigal"): ["12.45", "2.30"],
        ("theni", "palladam"): ["12.45", "4.00"],
        ("theni", "sulur"): ["12.45", "4.30"],
        ("theni", "coimbatore"): ["12.45", "5.00"],
        ("dindigal", "palladam"): ["2.30", "4.00"],
        ("dindigal", "sulur"): ["2.30", "4.30"],
        ("dindigal", "coimbatore"): ["2.30", "5.00"],
        ("palladam", "sulur"): ["4.00", "4.30"],
        ("palladam", "coimbatore"): ["4.00", "5.00"],
        ("sulur", "coimbatore"): ["4.30", "5.00"],
    }

    if (From, To) in time_schedule:
        times = time_schedule[(From, To)]
        departure = times[0]
        arrived = times[1]
        print("Departure:", departure, "From", From)
        print("Arrived Time:", arrived, "To", To)
        bus_details(date, departure, arrived, From, To)
    else:
        print("Time not available")

# Bus details requirement
def bus_details(date, departure, arrived, From, To):
    print("Bus Details", From.capitalize(), "to", To.capitalize())
    print("Ambal Travels", "|", "Date:", date, "|", "Departure:", departure, "|", "Arriver:", arrived)

    price = route_price(From, To)
    seats = create_seats(price)
    booking = seat_booking(seats, From, To)
    if booking is not None:
        seat_no, chosen = booking
        name, age, gender, mobileno, emailid = passenger_details()
        confirmed = confirm_seat(seat_no, gender, chosen, seats)
        if confirmed:
            print("\nUpdated Seat List")
            show_seats(seats, From, To)

# Route price requirement
def route_price(From, To):
    route = {
        ("cumbum", "theni"): 100,
        ("cumbum", "dindigal"): 150,
        ("cumbum", "palladam"): 200,
        ("cumbum", "sulur"): 350,
        ("cumbum", "coimbatore"): 500,
        ("theni", "dindigal"): 80,
        ("theni", "palladam"): 120,
        ("theni", "sulur"): 250,
        ("theni", "coimbatore"): 400,
        ("dindigal", "palladam"): 80,
        ("dindigal", "sulur"): 180,
        ("dindigal", "coimbatore"): 220,
        ("palladam", "sulur"): 100,
        ("palladam", "coimbatore"): 120,
        ("sulur", "coimbatore"): 70,
    }
    if (From, To) in route:
        return route[(From, To)]
    else:
        print("Price not available")
        return 0

# Seat class
class Seat:
    def __init__(self, number, price):
        self.number = number
        self.available = True
        self.gender = None
        if self.number <= 14:
            self.price = price
        else:
            self.price = price // 2 + 20

    def show(self):
        if self.available:
            status = "available"
        elif self.gender == "female_only":
            status = "female only"
        else:
            status = "booked " + str(self.gender)
        print("Seat", self.number, "|", status, "|", "Price", self.price)

# Create seats 1 - 20
def create_seats(price):
    seats = []
    for i in range(1, 21):
        seats.append(Seat(i, price))
    return seats

def show_seats(seats, From, To):
    print("Seat Details")
    print("Route:", From, "to", To)
    for s in seats:
        s.show()

def find(seats, n):
    for s in seats:
        if s.number == n:
            return s
    return None

# Seat choosing requirement
def seat_booking(seats, From, To):
    show_seats(seats, From, To)
    try:
        seat_no = int(input("Enter Seat No: "))
    except ValueError:
        print("Invalid Seat")
        return None

    chosen = find(seats, seat_no)
    if chosen is None:
        print("Invalid Seat")
        return None
    if not chosen.available and chosen.gender != "female_only":
        print("Seat", seat_no, "is Already Booked")
        return None
    return seat_no, chosen

# Passenger details
def passenger_details():
    print("Enter the Details")
    name = input("Name: ")
    age = input("Age: ")
    gender = input("Gender: ").lower()
    mobileno = input("Mobile Number: ")
    emailid = input("Email Id: ")
    return name, age, gender, mobileno, emailid

def confirm_seat(seat_no, gender, chosen, seats):
    if chosen.gender == "female_only" and gender != "female":
        print("Seat", seat_no, "is reserved for female only")
        return False

    ticket = ticket_create(seat_no)
    if ticket is None:
        print("Seat not confirmed because payment failed")
        return False
    
    chosen.available = False
    chosen.gender = gender
    if gender == "female":
        if seat_no % 2 == 1:
            pair = seat_no + 1
        else:
            pair = seat_no - 1
        next_seat = find(seats, pair)
        if next_seat is not None and next_seat.available:
            next_seat.available = False
            next_seat.gender = "female_only"
            print("Seat", next_seat.number, "reserved female only")
    print("Confirmed")
    return True

# ticket requirement
def ticket_create(seat_no):
    print("Your Seat Number is", seat_no)
    pnr = "TN2026" + str(seat_no)
    ticket_no = str(seat_no) + "625531"
    paid = payment()
    if paid == False:
        return None
    print("PNR Number:", pnr)
    print("Ticket Number:", ticket_no)
    return pnr, ticket_no

# payment requirement
def payment():
    print("Payment Method")
    print("1:UPI  2:Net Banking  3:card")
    try:
        paymenttype = int(input("Choose: "))
    except ValueError:
        print("invalid payment")
        return False

    if paymenttype == 1:
        pay_type = "UPI"
    elif paymenttype == 2:
        pay_type = "Net Bank"
    elif paymenttype == 3:
        pay_type = "card"
    else:
        print("invalid payment")
        return False

    print("Payment type:", pay_type)

    if input("confirm (yes/no): ") == "yes":
        print("payment success")
        return True
    else:
        return False

login()