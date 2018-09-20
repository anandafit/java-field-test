class CakedoctorListener(object):
    def on_answer_event( self ):
        raise NotImplementedError( "Should have implemented this" )

    def on_cakedoctro_error_event(self):
        raise NotImplementedError("Should have implimented this")