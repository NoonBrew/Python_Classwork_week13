import requests
import pprint

''' Function pulls the API from the website then stores the info
into a list '''
def bus_info(url):
    # Holds the dictionary and stores it in a list from the API.
    bus_dict = requests.get(url).json()
    # Calls a function with our original list and keyword that returns a list and stores it in the variables
    bus_route = bus_info_grabber(bus_dict, 'Route')
    bus_departure = bus_info_grabber(bus_dict, 'DepartureText')
    bus_description = bus_info_grabber(bus_dict, 'Description')
    # Calls the bus printer function
    bus_schedule_printer(bus_route, bus_description, bus_departure)


def bus_info_grabber(list, dict_key):
    ''' This function takes a dict Key and runs it through a list loop'''
    # Initiates a new list to store the information we want from the dictionary
    new_bus_list = []
    # Loops over the original list accessing the dictionary stored at each number value
    for bus in list:
        # Takes the key that we passed to append the value to the new list for each item in the orginal list.
        new_bus_list.append(bus[dict_key])
    # Returns the list to be stored and printed later.
    return new_bus_list

''' Function takes the three lists and prints them in a formated mannar
to make the values more understandable '''
def bus_schedule_printer(list1, list2, list3):
    # Centers the title of the info
    print('MCTC Bus Info'.center(66, '*'))
    # uses left and right justifications to crate spacing between headers
    print('Bus Number'.ljust(24) + 'Route' + 'Departure Time'.rjust(37))
    # loops through only one list to make sure that each bus as a number before printing any other value.
    for item in range(len(list1)):
        # compensates for the varying length of the route description by subtracting the length of the description
        # from the justification to keep ever thing orderly.
        endWidth = 50 - len(list2[item])
        print(f'{list1[item]}'.ljust(14), f'{list2[item]}', f'{list3[item]}'.rjust(endWidth, '.'))
    print()

''' main function calls the bus_info function '''
def main():
    # Stores the diffrent APIs in variables so they can be passed to the info function
    north_bus_line_url = 'http://svc.metrotransit.org/NexTrip/17940?format=json'
    south_bus_line_url = 'http://svc.metrotransit.org/NexTrip/17928?format=json'
    # prints a notification of what line each bus_info function is grabbing for.
    print('North Bus Line'.center(66, '+'))
    bus_info(north_bus_line_url)
    print('South Bus LIne'.center(66, '+'))
    bus_info(south_bus_line_url)

# Trys to run the main function but if it detects no internet it will print a warning.
try:
    main()

except ConnectionError:
    print('It appears you are not connected to the Internet. Please try again later.')