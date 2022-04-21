class Csv(object):
    def __init__(self, out, cols):
        self.out = out
        self.cols = cols
        self._write(cols)
    
    def line(self, items):
        assert len(items) == len(self.cols)
        self._write(items)
    
    def _write(self, items):
        self.out.write(u", ".join(self._fmt(item) for item in items))
        self.out.write(u"\n")
    
    def _fmt(self, item):
        try:
            float(item)
            return str(item)
        except ValueError:
            return '"%s"' % item
