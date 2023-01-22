stop = api.stop('53095')
print("LAT" + str(stop.Latitude))
print("LONG" + str(stop.Longitude))


vehicles = api.vehicles_by_route(25)
vehicle_ids = [vehicle.VehicleNo for vehicle in buses]
latlongs = []
for vehicle_id in vehicle_ids:
     if (eval(vehicle_id)//1000<=9):
         bus = api.bus(vehicle_id)
         print(bus.Latitude, bus.Longitude)

    print(vehicle_id)
    lat = bus.Latitude
    long = bus.Longitude
    latlongs.append((lat,long))


stops = [stop.Name for stop in api.stops(route_number = '25')]
print(vehicle_id)