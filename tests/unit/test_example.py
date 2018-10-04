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
        who_ask.monitor_via_specialist_one()
        who_ask.monitor_via_specialist_two()


        who_ask2 = WhoAsk2()
        who_ask2.monitor_via_specialist_one()
        who_ask2.monitor_via_specialist_two()








