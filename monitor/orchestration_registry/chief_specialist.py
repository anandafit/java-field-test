from monitor.specialists.specialist_one import executor as specialist_one
from monitor.specialists.specialist_two import executor as specialist_two

class ChiefSpecialist(object):
    def __init__(self):
        pass

    def start_operation(self, operation):
        if operation.specialist == 'specialist_one':
            # Start monitoring device one
            result = specialist_one.start(operation)

        elif operation.specialist == 'specialist_one':
            # Start monitoring device two
            result = specialist_two.start(operation)
               
        else :
            return "Specialist not found"  

        return result   
            