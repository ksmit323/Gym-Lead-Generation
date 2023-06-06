import googlemaps
import csv
import time


def main():
    
    # API key
    api_key = "AIzaSyAlWDq9ryxbHMFMs6clR37LHzF8Ps2OIbE"

    # Write in a list of coordinates for all the locations
    with open('coordinates.csv') as f:
        reader = csv.reader(f)
        coordinates = [','.join(row) for row in reader]
    
    gym_names = []
    count = 0
    
    # Iterate over each coordinate to find gyms in that area
    for location in coordinates:

        # Define place type
        type = 'gym'

        # Retrieve gym names
        gym_names += get_gym_names(location, type, api_key)

        count += 1
        print(f'{count}/{len(coordinates)} gyms have been added')
    
    gym_names = set(gym_names)

    # Write names to CSV file
    with open('names.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for name in gym_names:
            writer.writerow([name])


def get_gym_names(location, type, api_key):

    # Define the Client
    gmaps = googlemaps.Client(key = api_key)

    # Define the search parameters
    places = gmaps.places_nearby(location=location, rank_by='distance', type=type)

    # Create a list of all gym names
    gym_names = [place['name'] for place in places['results']]

    # Retrieve additional results using the pagetoken
    while 'next_page_token' in places:

        # Wait to avoid OVER_QUERY_ LIMIT errors
        time.sleep(2)

        # Retrieve next page of results
        next_page = gmaps.places_nearby(page_token=places['next_page_token'])

        # Add gym names from the next page to the list
        gym_names += [place['name'] for place in next_page['results']]

        # Update places to be the next page
        places = next_page
    
    return gym_names



if __name__ == '__main__':
    main()





















# location = "Hanoi" # replace with your desired location
# radius = "10000" # radius in meters, change as needed
# type = "gym" # type of business to search for, change as needed

# url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={}&radius={}&type={}&key={}".format(location, radius, type, api_key)

# response = requests.get(url)
# data = json.loads(response.text)

# if data["status"] == "OK":
#     for result in data["results"]:
#         print(result["name"])
# else:
#     print("Error: {}".format(data["status"]))