

class ListItem(object):
    def __init__(self, data, link=None):
        self.data = data
        self.link = link



class LinkedList(object):

    def add(self, value):
        if self.head is None:
            self.head = ListItem(value)
            self.end = self.head
            self.indices = 0
        else:
            tmp = self.end
            self.end = ListItem(value)
            tmp.link = self.end
            self.indices += 1

    def __init__(self, *args):
        self.head = None
        self.end = None
        self.indices = 0
        if args:
            for item in args:
                self.add(item)


    def get_prev_by_value(self, value):
        item = self.head
        while item.link is not None:
            if item.link.data == value:
                return item
            item = item.link
        return None


    def get_by_index(self, index):
        counter = 0
        item = self.head

        while item.link is not None:
            if counter == index:
                break
            counter += 1
            item = item.link
        return item


    def insert(self, index, value):
        if index > self.indices or self.head is None:
            self.add(value)
            return
        if index == 0:
            item = self.head
            self.head = ListItem(value, item)
        else:
            item = self.get_by_index(index-1)
            new_item = ListItem(value, item.link)
            item.link = new_item
        self.indices += 1


    def get(self, index):
        if index > self.indices:
            raise IndexError
        return self.get_by_index(index).data


    def remove(self, value):

        if self.head is None:
            return
        if self.head.data == value:
            if self.head.link is not None:
                self.head = self.head.link
            else:
                self.clear()
        else:
            prev = self.get_prev_by_value(value)
            if prev is None:
                raise ValueError
            prev.link = prev.link.link
        self.indices -= 1


    def remove_at(self, index):
        if index == 0:
            if self.head.link is not None:
                value = self.head.data
                self.head = self.head.link
            else:
                value = self.head.data
                self.head = None
        else:
            prev = self.get_by_index(index - 1)
            value = prev.link.data
            prev.link = prev.link.link

        self.indices -= 1
        return value


    def clear(self):
        self.__init__()


    def contains(self, value):
        return self.get_prev_by_value(value) is not None

    def len(self):
        return self.__len__()

    def __len__(self):
        if self.head is None:
            return 0
        return self.indices + 1


    def is_empty(self):
        return self.head == None


    def __iter__(self):
        self.copy = self.indices + 1
        return self

    def __next__(self):
        while self.copy :
            self.copy -= 1
            return self.get_by_index(self.indices - self.copy).data
        raise StopIteration


if __name__ == '__main__':
    import random
    ll2 = LinkedList(6, -8, 7, 0, 6, 3, -5, -3, 5, 0, -2, 9, -10)
    print([l for l in ll2])
    ll2.add(20)
    print([l for l in ll2])
    print(ll2.len())
    ll2.insert(0, 30)
    for i in range(ll2.len()):
        item = random.randrange(ll2.len())
        print(item)
        print(ll2.remove_at(item))
        print([l for l in ll2])

