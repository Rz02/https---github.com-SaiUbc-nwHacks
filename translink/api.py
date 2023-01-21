# this file is to test out the api integration of the project
from tilapya import RTTI
api = RTTI('Ik7TSY2bkJRQzeQeH5LT')
stop = api.stop('53095')
print(stop.Name)

