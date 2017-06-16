class WindSpeedDefinitionService:
    @staticmethod
    def get_wind_speed_definition(wind_speed):
        if wind_speed < 5:
            return 'Calm'
        elif wind_speed <= 6:
            return 'Light Air'
        elif wind_speed <= 12:
            return 'Light breeze'
        elif wind_speed <= 19:
            return 'Gentle breeze'
        elif wind_speed <= 28:
            return 'Moderate breeze'
        elif wind_speed <= 38:
            return 'Fresh breeze'
        elif wind_speed <= 50:
            return 'Strong breeze'
        else:
            return 'High wind'
