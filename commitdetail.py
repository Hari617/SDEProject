class Commitdetail(object):
    def __init__(self, ch, author, date, changesInFile):
        self.ch = ch
        self.author = author
        self.date = date
        self.changesInFile = changesInFile

    def __str__(self):
        detail = str(self.ch) + " " + str(self.author) + " " + str(self.date)
        detail = detail + "\n"
        detail += "\n".join((" " + str(change)) for change in self.changesInFile)
        return detail
    
    def __eq__(self, otherObj):
        return (
            self.ch == otherObj.ch and self.changesInFile == otherObj.changesInFile
        )
