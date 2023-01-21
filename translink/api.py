# this file is to test out the api integration of the project
import requests


response = requests.get('https://api.translink.ca/rttiapi/v1/buses/7196?apikey=[Ik7TSY2bkJRQzeQeH5LT]')


print(response.json())
