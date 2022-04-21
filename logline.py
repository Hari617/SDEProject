

class LogLine( object ):
    def __init__( self, a, d, b ):
        self.a = a
        self.d = d
        self.b = b

    def __str__( self ):
        return "%s %s %s" % ( self.a, self.d, self.b )

    def __eq__( self, other ):
        return (
            self.a == other.a
            and self.d == other.d
            and self.b == other.b
        )
