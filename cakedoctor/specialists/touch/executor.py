import time
from cakedoctor.response_event import CAKEDoctorResponseEvent

def start(operation):
    timeout = time.time() + 60*1   # 1 minutes from now
    while True:
        test = 0
        print("Monitoring touch is running... ... ... ...")
        time.sleep(1) # wait 3 second during the loop
        if test == 5 or time.time() > timeout:
            break
        test = test - 1
    return CAKEDoctorResponseEvent(operation.specialist, operation.operation_name,
     CAKEDoctorResponseEvent.INFO, "Touch is good")
    


