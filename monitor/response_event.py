class ResponseEvent(object):
    """
    Generic operation response even to use with OperationDispatcher.
    """
    
    def __init__(self, specialist, operation_name, operation_type, data = None):
        self._specialist = specialist
        self._operation_name = operation_name
        self._operation_type = operation_type
        self._data = data
        
    @property 
    def specialist(self):
        """
        Returns the specialist associated to the ResponseEvent
        """
        return self._specialist

    @property 
    def operation_name(self):
        """
        Returns the operation_name associated to the ResponseEvent
        """
        return self._operation_name


    @property 
    def operation_type(self):
        """
        Returns the operation_type associated to the ResponseEvent
        """
        return self._operation_type

    @property 
    def data(self):
        """
        Returns the data associated to the ResponseEvent
        """
        return self._data


class MonitorResponseEvent( ResponseEvent ):
    INFO     = "INFO"
    DEBUG = "DEBUG" 
    REPORT = "REPORT"        