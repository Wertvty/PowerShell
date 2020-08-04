class Matrix(object):
    st = []
    def __init__(self, matrix_string):
        self.st=matrix_string.split("\n")

    def row(self, index):
        self.ro = []
        for x in self.st[index-1].split(" "):
            self.ro.append(int(x))
        return self.ro

    def column(self, index):
        self.reee=[]
        for k in self.st:
            self.reee.append(int(k.split(" ")[index-1]))
        return self.reee
