#Login Requirement 
def login():
    print("Welcome to the Ticket Booking System!")
    print("Cumbum To Coimbatore Route Bus Here")
    while True:
        user=input("Enter your username: ")
        password=input("Enter your password: ")
        if user!="" and password!="":
            print("Login successful!")
            search_bus() # if the login sucess then only go to search 
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
        else:
            print("Bus Not Available")
        break

login()

