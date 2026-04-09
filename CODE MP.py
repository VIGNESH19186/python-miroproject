movies=[
    "MOVIE 1",
    "MOVIE 2",
    "MOVIE 3",
    "MOVIE 4",
    "MOVIE 5"
]

a={
    "IMAX",
    "PVR",
    "THEATER"
}

b={
    "IMAX":("DIAMOND","GOLD","SILVER"),
    "PVR":("DIAMOND","GOLD","SILVER"),
    "THEATER":("DIAMOND","GOLD")
}

c_price = {                
    "DIAMOND": 250,
    "GOLD": 200,
    "SILVER":150
}

seats = [
    [0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],
    [0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],
    [0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]
]

print("available movies")
for i, movie in enumerate(movies, start=1):   
    print(i, movie)

k=int(input("total number of seats: "))


v = movies[k-1]

places = tuple(a)   
print("\nAvailable Places:")
for i, place in enumerate(places, start=1):
    print(i, place)

place_choice = int(input("Select place number: ")) - 1
place_selected = places[place_choice]

def price(choice):          
    if choice == 1:
        return (k*250)+10
    elif choice == 2:
        return (k*200)+10
    else:
        return (k*150)+10

seat_choice = int(input("Enter seat type (1/2/3): "))
print("Total price =", price(seat_choice))

while True:
    print("\nseats selected = 1 , seats available = 0")
    for row in seats:
        print(row)

    r=int(input("enter row (0-8): "))
    c=int(input("enter col (0-3): "))

    if seats[r][c] == 0:
        seats[r][c] = 1
        print("seat booked successfully")
    else:
        print("seat has already been booked")

    more = input("Book another seat? (yes/no): ")
    if more.lower() != "yes":
        break
movie_selected = v
place_selected = place_selected
seat_types = ["DIAMOND", "GOLD", "SILVER"]
seat_selected = seat_types[seat_choice - 1]
total_amount = price(seat_choice)
print("---------------------------------------------")
print("        MOVIE BILL")
print("---------------------------------------------")
print("Movie Name   :", movie_selected)
print("Theater      :", place_selected)
print("Seat Type    :", seat_selected)
print("No. of Seats :", k)
print("Service Fee  : Rs. 10")
print("Total Amount : Rs.", total_amount)
print("   THANK YOU! VISIT AGAIN")
print("---------------------------------------------")
