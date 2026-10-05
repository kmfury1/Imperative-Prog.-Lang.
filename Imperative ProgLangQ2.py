flight_route = [
    ("New Orleans", "Atlanta"),
    ("Atlanta", "London"),
    ("London", "Dubai"),
    ("Dubai", "Singapore")
]

def print_itinerary(route_list):
    print("--- FLIGHT ITINERARY ---")
    for departure, arrival in route_list:   # tuple unpacking
        print(f"Depart: {departure}  ->  Arrive: {arrival}")

# Main program
print_itinerary(flight_route)