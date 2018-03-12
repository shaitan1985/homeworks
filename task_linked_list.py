

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
            if item.data == value:
                return item
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
        if index > self.indices:
            self.add(value)
            return
        item = self.get_by_index(index-1)
        new_item = ListItem(value, item.link)
        item.link = new_item


    def get(self, index):
        if index > self.indices:
            raise IndexError
        return self.get_by_index(index).data


    def remove(self, value):
        prev = get_prev_by_value(value)
        if prev is None:
            raise ValueError
        prev.link = prev.link.link


    def remove_at(self, index):
        if index == 0:
            value = self.head.data
            self.head = self.head.link
        else:
            prev = get_by_index(index - 1)
            value = prev.link.data
            prev.link = prev.link.link

        return value


    def clear(self):
        self.__init__()


    def contains(self, value):
        return get_prev_by_value(value) is not None


    def len(self):
        if self.head is None:
            return 0
        return self.indices + 1


    def is_empty(self):
        return self.head == None


    def __iter__(self):
        self.copy = self.indices
        return self

    def __next__(self):
        while self.copy:
            self.copy -= 1
            return self.get_by_index(self.indices - self.copy).data
        raise StopIteration


