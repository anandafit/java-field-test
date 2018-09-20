class CAKEDoctorOperation( object ):
    """
    Generic operation to use with OperationDispatcher.
    """
    
    def __init__(self, specialist, operation_name, other_params = None):
        """
        The constructor accepts an operation
        """
        self._specialist = specialist
        self._operation_name = operation_name
        self._other_params = other_params
        
    @property 
    def specialist(self):
        """
        Returns the specialist associated to the operation
        """
        return self._specialist
        
    @property
    def operation_name(self):
        """
        Returns the operation_name associated to the operation
        """
        return self._operation_name

    @property
    def other_params(self):
        """
        Returns the other_params associated to the operation
        """
        return self._other_params


if __name__ == "__main__":
    pass 
