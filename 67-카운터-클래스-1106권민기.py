class Counter:
    def __init__(self):
        self.value = 0
    def reset(self,initValue):
        self.value = initValue
    def increment(self):
        self.value += 1
    def get(self):
        return self.value
    
a = Counter()
b = Counter()

a.reset(0)
a.increment()
print(a.get())

b.reset(100)
b.increment()
print(b.get())