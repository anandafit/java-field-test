import time

from monitor.response_event import MonitorResponseEvent

def start(operation):
    timeout = time.time() + 60*1   # 1 minutes from now
    while True:
        test = 0
        print("Continue monitoring by specialist one ... ... ... ...")
        time.sleep(1) # wait 3 second during the loop
        if test == 5 or time.time() > timeout:
            break
        test = test - 1
    return MonitorResponseEvent(operation.specialist, operation.operation_name,
     MonitorResponseEvent.INFO, "Specialist one monitoring is done")