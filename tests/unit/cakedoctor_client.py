from cakedoctor.event import CakedoctorEvent
from cakedoctor.cakedoctor_listener import CakedoctorListener

from cakedoctor.operation import CAKEDoctorOperation

from cakedoctor.cakedoctor import cakedoctor
my_cakedoctor = cakedoctor()
'''
WhoAsk need would be Pulse client
'''
class WhoAsk( CakedoctorListener ):
    """
    First class which ask who is listening to it
    """
    def __init__(self):
        self._cakedoctor = my_cakedoctor
        self._cakedoctor.add_event_listener(self)
        
    def monitor_touch(self):
        my_operation = CAKEDoctorOperation("touch", "monitor_touch_issues")
        self._cakedoctor.dispatch_operation(self, my_operation)

    def monitor_payment_cube(self):
        my_operation = CAKEDoctorOperation("payment_cube", "monitor_payment_cube")
        self._cakedoctor.dispatch_operation(self, my_operation)    
   
    def on_answer_event(self, event):
        """
        Event handler for the RESPOND event type
        """
        operation = event.data
        print("<<< Thank you instance {0}".format( operation.data ))


class WhoAsk2( CakedoctorListener ):
    """
    First class which ask who is listening to it
    """
    def __init__(self):
        self._cakedoctor = my_cakedoctor
        self._cakedoctor.add_event_listener(self)

    def monitor_touch(self):
        my_operation = CAKEDoctorOperation("touch", "monitor_touch_issues")
        self._cakedoctor.dispatch_operation(self, my_operation)

    def monitor_payment_cube(self):
        my_operation = CAKEDoctorOperation("payment_cube", "monitor_payment_cube")
        self._cakedoctor.dispatch_operation(self, my_operation)    
           
   
    def on_answer_event(self, event):
        """
        Event handler for the RESPOND event type
        """
        operation = event.data
        print("<<< Thank you instance 2 {0}".format( operation.data ))        
      