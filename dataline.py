class Dataline(object):
    def __init__(self, ch, author, date, removed, added, file_name):
        self.ch = ch
        self.author = author
        self.date = date
        self.removed = removed
        self.added = added
        self.file_name = file_name

    def __str__(self):
        return " ".join([
            self.ch,
            self.author,
            self.date,
            self.removed,
            self.added,
            self.file_name
        ])

    def __eq__(self, other):
        return (
            self.ch == other.commit_hash and 
            self.date == other.date and 
            self.added == other.added and 
            self.removed == other.removed and 
            self.file_name == other.file_name and 
            self.author == other.author
      
        )
