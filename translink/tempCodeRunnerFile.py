for route in routes:
    
        numBuses = api.buses(route_number = route)
        print(numBuses)