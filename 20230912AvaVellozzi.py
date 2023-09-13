from geopy.geocoders import Nominatim

def get_coordinates(address):
    geolocator = Nominatim(user_agent="20230912AvaVellozzi")
    location = geolocator.geocode(address)

    if location is not None:
        latitude = location.latitude
        longitude = location.longitude
        return latitude, longitude
    else:
        return None

address = "1702 W University Ave, Gainesville, FL"
coordinates = get_coordinates(address)

if coordinates:
    latitude, longitude = coordinates
    print(f"Latitude: {latitude}, Longitude: {longitude}")
else:
    print("Address not found or invalid.")


