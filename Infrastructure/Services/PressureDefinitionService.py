class PressureDefinitionService:
    @staticmethod
    def get_pressure_definition(pressure):
        if pressure < 1005:
            return 'Low'
        elif pressure <= 1018:
            return 'Normal'
        else:
            return 'Very High'
