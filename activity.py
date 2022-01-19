import requests
import pprint
def get_activity():
    url = 'https://www.boredapi.com/api/activity'

    response = requests.get(url).json()
    activity = response['activity']
    return activity
def main():
    while True:
        activity = get_activity()
        print(f'Your suggested activity is: {activity}')
        another_activity = input('Another activity? Press "Y" for another: ')
        if another_activity.lower() != 'y':
            break

main()