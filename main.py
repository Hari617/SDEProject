
import subprocess
import sys

from githistorydata.csv import Csv
from githistorydata.expand_commits import expand_authors, expand_lines
from githistorydata.git import Git
from githistorydata.rawgit import RawGit
from githistorydata.settings import Settings


def main( argv, out, err ):
    aaa = Settings()
    try:
        git = Git( RawGit(aaa["git_path"]) )
        ghi = Csv(out,( "Commit", "Date", "Author", "Added", "Removed", "File" ) )
        for x in expand_lines( git, expand_authors( git.log() ) ):
            ghi.line( (x.commit_hash,x.date.date().isoformat(),x.author,x.added,x.removed,x.filename,) )
    except subprocess.CalledProcessError as e:
        print(str(e))
        sys.exit(1)
    finally:
        out.flush()
