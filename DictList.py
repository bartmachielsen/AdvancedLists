from CustomList import CustomList

class DictList(CustomList):
    def __init__(self):
        CustomList.__init__(self)
        self._dict = {}

    def add_element(self, key, value):
        self._dict[key] = value
        return 1

    def search_element(self, key):
        if key in self._dict:
            return key, self._dict[key], 1
        return None, None, 1


if __name__ == "__main__":
    DictList().test(1000*1000)