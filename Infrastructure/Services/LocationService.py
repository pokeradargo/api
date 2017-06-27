from geopy.geocoders import Nominatim


class LocationService:

    def get_location_data(self, lat, lng):
        country_code = None
        geolocator = Nominatim()
        location = geolocator.reverse(lat + ',' + lng)
        if location is not None:
            country_code = location.raw['address']['country_code']

        return {
            'country_code': country_code
        }
