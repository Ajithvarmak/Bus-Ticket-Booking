#Login Requirement 
def login():
    print("Welcome to the Ticket Booking System!")
    print("Cumbum To Coimbatore Route Bus Here")
    while True:
        user=input("Enter your username: ")
        password=input("Enter your password: ")
        if user!="" and password!="":
            print("Login successful!")
            search_bus()
        else: 
            print("login failed!")
            break

#Search Requirement
def search_bus():
    print("Search for Available Buses in Cumbum To Coimbatore Route")
    place=["cumbum","theni","dindigal","palladam","sulur","coimbatore"]
    print("Available Stops: ",place)
    while True:
        From=input("Enter the starting point: ").lower()
        To=input("Enter a Destination:").lower()

        print("Available Date")
        print("1: 12/07/2027")
        date=input("Choose the date:")
        if date=="1":
            date="12/07/2027"
        else:
            print("invaild date")
            break
        
        if (From in place) and (To in place):
            print("Bus Available From ",From,"To",To)
            bus_time(From,To,date)
        else:
            print("Bus Not Available")
            break
        break

# bus time in requirement 2
def bus_time(From,To,date):
    time_schedule={
        ("cumbum","theni"):["12.00","12.45"],
        ("cumbum","dindigal"):["12.00","2.30"],
        ("cumbum","palladam"):["12.00","4.00"],
        ("cumbum","sulur"):["12.00","4.30"],
        ("cumbum","coimbatore"):["12.00","5.00"],
        ("theni","dindigal"):["12.45","2.30"],
        ("theni","palladam"):["12.45","4.00"],
        ("theni","sulur"):["12.45","4.30"],
        ("theni","coimbatore"):["12.45","5.00"],
        ("dindigal","palladam"):["2.30","4.00"],
        ("dindigal","sulur"):["2.30","4.30"],
        ("dindigal","coimbatore"):["2.30","5.00"],
        ("palladam","sulur"):["4.00","4.30"],
        ("palladam","coimbatore"):["4.00","5.00"],
        ("sulur","coimbatore"):["4.30","5.00"],
    }
    if (From,To) in time_schedule:
        times=time_schedule[(From,To)]
        departure=str(times[0])
        arrived=str(times[1])
        print("Departure:",departure,"From",From)
        print("Arrived Time:",arrived,"To", To) 
        bus_details(date,departure,arrived,From,To)    
    else:
        print("time not available")

# bus details requirement 
def bus_details(date,departure,arrived,From,To):
    print("Bus Details",From.capitalize(),"to",To.capitalize())
    print(" Ambal Travels ", "|", "Date:",date, "|", "Departure:",departure,"|","Arriver:",arrived)
    price=route_price(From,To)
    seats=create_seats(price)
    show_seats(seats,From,To)
    seat_booking(seats,From,To)

# route price requirement 
def route_price(From,To):
    route={
        ("cumbum","theni"):100,
        ("cumbum","dindigal"):150,
        ("cumbum","palladam"):200,
        ("cumbum","sulur"):350,
        ("cumbum","coimbatore"):500,
        ("theni","dindigal"):80,
        ("theni","palladam"):120,
        ("theni","sulur"):250,
        ("theni","coimbatore"):400,
        ("dindigal","palladam"):80,
        ("dindigal","sulur"):180,
        ("dindigal","coimbatore"):220,
        ("palladam","sulur"):100,
        ("palladam","coimbatore"):120,
        ("sulur","coimbatore"):70,
    }

    if (From,To) in route:
        price = route[(From,To)]
        return price
    else:
        print("price not available")

# seat class
class Seat:
    def __init__(self,number,price):
        self.number = number
        self.available = True
        self.gender=None

        if self.number <=14:
            self.price=price
        else:
            self.price= price // 2+20

    def show(self):
        if self.available:
            status="available"
        elif self.gender =="female only":
            status="female only"
        else:
            status="booked"+str(self.gender)
        print("Seat",self.number,"|",status,"|","Price",self.price)

# create seat 1 - 20
def create_seats(price):
    seats =[]
    for i in range (1,21):
        seats.append(Seat(i,price))
    return seats

def show_seats(seats,From,To):
    print("Seat Details")
    print("Route:",From,"to",To)
    for s in seats:
        s.show()

def find(seats,n):
    for s in seats:
        if s.number ==n:
            return s
    return None  

#seat choosing requirement
def seat_booking(seats,From,To):
    show_seats(seats,From,To)

    seat_no=int(input("Enter Seat No:"))
    chosen =find(seats, seat_no)

    if chosen==None:
        print("Invaild Seat")
        return None
    if not chosen.available and chosen.gender !="female_only":
        print("Seat",seat_no," is Already Booked ")
        return None
    return seat_no,chosen

login()