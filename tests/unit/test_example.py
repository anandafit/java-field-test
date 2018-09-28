# from datetime import date

from tests import *
from monitor.event import *
from tests.unit.devicemonitor_client import WhoAsk, WhoAsk2
# from tests.helpers import *


class TestExample(unittest.TestCase):

    def test_helper(self):

        # Create an instance of WhoAsk class and two instance of WhoRespond class
        who_ask = WhoAsk()

        # Start the operation to monitor
        who_ask.monitor_deviceone()
        who_ask.monitor_devicetwo()


        who_ask2 = WhoAsk2()
        who_ask2.monitor_deviceone()
        who_ask2.monitor_devicetwo()








