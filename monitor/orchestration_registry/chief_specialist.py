from monitor.specialists.deviceone import executor as deviceone_specialist
from monitor.specialists.devicetwo import executor as devicetwo_cube_specialist

class ChiefSpecialist(object):
    def __init__(self):
        pass

    def start_operation(self, operation):
        if operation.specialist == 'deviceone':
            # Start monitoring device one
            result = deviceone_specialist.start(operation)

        elif operation.specialist == 'devicetwo':
            # Start monitoring device two
            result = devicetwo_cube_specialist.start(operation)
               
        else :
            return "Specialist not found"  

        return result   
            