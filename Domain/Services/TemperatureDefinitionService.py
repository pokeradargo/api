class TemperatureDefinitionService:
    @staticmethod
    def get_temperature_definition(temperature):
        if temperature < 0:
            return 'Very Cold'
        elif temperature <= 10:
            return 'Cold'
        elif temperature <= 20:
            return 'Tempered'
        elif temperature <= 30:
            return 'Warm'
        else:
            return 'Very Warm'
