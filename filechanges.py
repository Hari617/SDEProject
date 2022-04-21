

class FileChanges( object ):
    def __init__( self, p, r, nn ):
        self.nn = nn
        self.r = r
        self.p = p
        

    def __str__( self ):
        return "+%d -%d %s" % ( self.p, self.r, self.nn )

    def __eq__( self, rte ):
        return (
            self.p == rte.p
            and self.r == rte.r
            and self.nn == rte.nn
        )
