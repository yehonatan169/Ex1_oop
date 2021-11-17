

class Calls:

    def __init__(self, callelev: str, time=0, source=0, destention=0, flag=0, index=-1):
        self.call = callelev
        self.time = time
        self.source = source
        self.destention = destention
        self.flag = flag
        self.index = index

    def set_index(self, ind: int):
        self.index = ind
