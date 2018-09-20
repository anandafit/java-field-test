from cakedoctor.specialists.touch import executor as touch_specialist
from cakedoctor.specialists.payment_cube import executor as payment_cube_specialist

class ChiefSpecialist(object):
    def __init__(self):
        pass

    def start_operation(self, operation):
        if operation.specialist == 'touch':
            # Start monitoring touch here
            result = touch_specialist.start(operation)

        elif operation.specialist == 'payment_cube':
            # Start monitoring payment cube here
            result = payment_cube_specialist.start(operation)
               
        else :
            return "Specialist not found"  

        return result   
            