# from datetime import date

from tests import *
from cakedoctor.event import *
from tests.unit.cakedoctor_client import WhoAsk, WhoAsk2
# from tests.helpers import *


class TestExample(unittest.TestCase):

    def test_helper(self):

        # Create an instance of WhoAsk class and two instance of WhoRespond class
        who_ask = WhoAsk()

        # Start the operation to monitor
        who_ask.monitor_touch()
        # who_ask.monitor_payment_cube()


        who_ask2 = WhoAsk2()
        # who_ask2.monitor_touch()
        who_ask2.monitor_payment_cube()
        self.assertFalse(True)








