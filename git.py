
import re
import dutil.parser

from githistorydata.commitdetail import CommitDetail
from githistorydata.filechanges import FileChanges
from githistorydata.logline import LogLine


class Git(object):

    def __init__( self, g_r ):
        self.g_r = g_r
    def show( self, a, d, b ):
        sl = self.g_r.git_show_numstat( a )
        return CommitDetail(
            a,
            d,
            b,
            list( self._showline( l ) for l in sl[1:] if l != "")
        )
    def log( self ):
        return list(
            self._logline( ln.strip() )
            for ln in self.g_r.git_log_pretty_tformat_H_ai_an()
            if ln.strip() != ""
        )


    rle = re.compile(
        r"([0-9a-f]{40}) (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} [-+]\d{4}) (.+)"
    )

    def _logline( self, ln ):
        x= Git.rle.match( ln )
        if not x:
            raise Exception(
                "Line from git log '%s' did not match expected format"
                % ln
            )
        return LogLine(
            x.group( 1 ),dutil.parser.parse( x.group( 2 ) ),x.group( 3 ))

    slr = re.compile(
        r"(-|\d+)\s+(-|\d+)\s+(.*)"
    )

    @staticmethod
    def lines_changed( num ):
        if num != "-":
            return int( num )
        else:
            return 0
            

    def _showline( self, ln ):
        x = Git.slr.match( ln )
        if not x:
            raise Exception(
                "Line from git show '%s' did not match expected format"
                % ln
            )
        return FileChanges(
            Git.lines_changed( x.group( 1 ) ),
            Git.lines_changed( x.group( 2 ) ),
            x.group( 3 )
        )
