class AppearedTimeDayDefinitionService:
    # see http://www.myenglishlanguage.com/essential-vocabulary/telling-time-english/
    @staticmethod
    def get_appeared_time_day_definition(hour):
        if hour is not None and 6 > hour >= 0:
            return 'night'
        elif hour is not None and 12 > hour >= 6:
            return 'morning'
        elif hour is not None and 18 > hour >= 12:
            return 'afternoon'
        elif hour is not None and 24 > hour >= 18:
            return 'evening'

