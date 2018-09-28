import threading

from monitor.event import EventDispatcher, DeviceMonitorEvent
from monitor.orchestration_registry.chief_specialist import ChiefSpecialist

def device_monitor():
    return DeviceMonitorImpl(EventDispatcher())

class DeviceMonitorImpl(object):
    def __init__(self, dispatcher):
        self.event_dispatcher = dispatcher

    def add_event_listener(self, monitor_listener):
        self.event_dispatcher.add_event_listener( 
            monitor_listener, monitor_listener.on_answer_event 
        )

    def dispatch_operation(self, monitor_listener, operation = None):
        """
        Dispatch the ask event
        """
        print(">>> I'm instance {0}. Who are listening to me ?".format( self ))

        exicutor_thread = threading.Thread(target=self._exicute_dispatcher_operation, args=(monitor_listener, operation,))
        exicutor_thread.start()
        
        print("Starting new thread :{}, sepcialist: {}, for: {}".format(exicutor_thread.getName(), operation.specialist, "INFO"))

    def _exicute_dispatcher_operation(self, monitor_listener, operation):

        self.event_dispatcher.dispatch_event( 
            DeviceMonitorEvent ( monitor_listener, ChiefSpecialist().start_operation(operation)) 
        )
        

if __name__ == "__main__":
    pass
    





