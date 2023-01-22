# this file is to test out the api integration of the project
from tilapya import *
import folium
api = RTTI('Ik7TSY2bkJRQzeQeH5LT')
routes = ['R4', '2', '3', '4', '5', '6', '7', '8', '9', '10', '14', '15', '16', '17', '19', '20', '22', '23', '25', '26', '27', '28', '29', '31', '33', '41', '49', '50', '68', '84', '99', '100', 'R3', '101', '103', '104', '105', '106', '110', '112', '116', '119', '123', '128', '129', '130', '131', '133', '134', '136', '144', '145', '146', '147', '148', '155', 'R3', '151', '152', '153', '156', '157', '159', '160', '169', '170', '171', '172', '173', '174', '180', '181', '182', '183', '185', '186', '187', '188', '189', '191', 'R2', '210', '211', '212', '214', '215', '227', '228', '229', '230', '232', '236', '240', '241', '245', '246', '247', '249', '250', '251', '252', '253', '254', '255', '256', '257', '258', '262', '280', '281', '282', 'R1', '301', '310', '311', '312', '314', '316', '319', '320', '321', '322', '323', '324', '325', '326', '329', '335', '337', '340', '341', '342', '345', '350', '351', '352', '354', '360', '361', '362', '363', '364', '370', '371', '372', '373', '375', '388', '391', '393', '394', '395', '401', '402', '403', '404', '405', '406', '407', '408', '410', '412', '413', '414', '416', '418', '430', '480', '501', '503', '502', '509', '531', '555', '560', '561', '562', '563', '564', '595', '601', '602', '603', '604', '606', '608', '609', '614', '616', '618', '619', '620', '640', '701', '719', '722', '733', '741', '743', '744', '745', '746', '748', '749', '791', 'N8', 'N9', 'N10', 'N15', 'N17', 'N19', 'N20', 'N22', 'N24', 'N35']

# buses = api.buses(route_number = 109)
# print(buses)


## Maybe a function that accepts a stop number and returns a list of the current coordinates of the buses that service that stop for a specific route (only if that route has available buses)


def stopCoords(stop_num):
    stop = api.stop(stop_num)
    return (stop.Latitude, stop.Longitude) #TODO wheelchair access??

def busCoords(route_num):
    busesCoords = []
    try:
        buses = api.buses(route_number = route_num)
        for bus in buses:
            if eval(bus.VehicleNo)//1000<=9:
                busesCoords.append((bus.Latitude, bus.Longitude))
                print(busesCoords + "for bus" + route_num)
    except TransLinkAPIError:
        print("sorry your buses for route " + route +  " cannot be found")
    
    finally
        return busesCoords


#stop = api.stop('53095')
#print("LAT" + str(stop.Latitude))
#print("LONG" + str(stop.Longitude))


# vehicles = api.vehicles_by_route(25)
# vehicle_ids = [vehicle.VehicleNo for vehicle in buses]
# latlongs = []
# for vehicle_id in vehicle_ids:
#      if (eval(vehicle_id)//1000<=9):
#          bus = api.bus(vehicle_id)
#          print(bus.Latitude, bus.Longitude)

#     print(vehicle_id)
#     lat = bus.Latitude
#     long = bus.Longitude
#     latlongs.append((lat,long))


# stops = [stop.Name for stop in api.stops(route_number = '25')]
#     print(vehicle_id)


