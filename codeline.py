class Codeline(object):
    def __init__(self, ch, author, date, weight):
        self.ch = ch
        self.author = author
        self.date = date
        self.weight = weight

    def __str__(self):
        return str(self.ch) + " " + str(self.author) + " " + str(self.date) + " " + str(self.weight)

    def __eq__(self, otherObj):
        return (
            self.ch == otherObj.ch and
            self.author == otherObj.author and
            self.date == otherObj.date and
            self.weight == otherObj.weight
        )
