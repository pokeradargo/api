import datetime
import pytz
from timezonefinder import TimezoneFinder


class HourLocalTimeService:

    def get_local_hour_from_lat_and_lng(self, lat, lng):
        tf = TimezoneFinder()
        timezone_str = tf.timezone_at(lng=float(lng), lat=float(lat))

        timezone = pytz.timezone(timezone_str)
        dt = datetime.datetime.now()
        localtime = dt.astimezone(timezone)

        return localtime.hour

