class Fibs(object):
    a, b = 0, 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration
        return self.a

    def __iter__(self):
        return self

if __name__ == "__main__":

    fibs = Fibs()
    for el in fibs:
        print(el)
