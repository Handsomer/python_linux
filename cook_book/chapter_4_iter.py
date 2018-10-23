class Countdown:
    def __init__(self, start):
        self.start = start
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

if __name__ == '__main__':
    cnt_down_obj = Countdown(4)
    for elem in reversed(cnt_down_obj):
        print(elem,'-----')
    iter_obj = iter(cnt_down_obj)
    while True:
        value = next(iter_obj, None)
        if value != None:
            print(value,'++++')
        else:
            break
