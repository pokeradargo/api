from Infrastructure.Services.HourLocalTimeService import HourLocalTimeService
from Domain.Services.AppearedTimeDayDefinitionService import AppearedTimeDayDefinitionService


class AppearedTimeDayPreProcessingAction:
    _HourLocalTimeService = None
    _AppearedTimeDayDefinitionService = None

    def __init__(self):
        self._HourLocalTimeService = HourLocalTimeService()
        self._AppearedTimeDayDefinitionService = AppearedTimeDayDefinitionService()

    def run(self, lat, lng):
        hour = self._HourLocalTimeService.get_local_hour_from_lat_and_lng(lat, lng)
        return self._AppearedTimeDayDefinitionService.get_appeared_time_day_definition(hour)
