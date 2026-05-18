#Login Requirement 
def login():
    print("Welcome to the Ticket Booking System!")
    print("Cumbum To Coimbatore Route Bus Here")
    while True:
        user=input("Enter your username: ")
        password=input("Enter your password: ")
        if user!="" and password!="":
            print("Login successful!")
            return True
        else: 
            print("login failed!")
            break
login()
