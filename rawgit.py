import subprocess
class RawGit( object ):
    def __init__( self, g_p="/usr/bin/git" ):
        self._g_p = g_p
    def _g_r( self, args ):
        return subprocess.check_output([self._g_p] + args).decode( encoding="UTF-8", errors="replace" ).split( "\n" )
    def git_show_numstat( self, commit_hash ):
        return self._g_r(["show", "--pretty=oneline", "--numstat", commit_hash] )
    def git_log_pretty_tformat_H_ai_an( self ):
        return self._g_r(["log", "--no-merges", "--pretty=tformat:%H %ai %an"] )



