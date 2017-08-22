from CustomList import CustomList

class AlphaList(CustomList):
    """
        AlphaList is a list where the keys are alpabetical sorted, the keys are the characters in the string.
    """
    def __init__(self):
        CustomList.__init__(self)
        self._dict = {}

    @staticmethod
    def _search(dic, key_value, index=0, steps=0):
        if index >= len(key_value):
            if "keys" not in dic:
                dic["keys"] = {}
            return dic["keys"], steps
        else:
            key = key_value[index]

            if key not in dic:
                dic[key] = {}
            return AlphaList._search(dic[key], key_value, index+1, steps+1)

    def add_element(self, key, value):
        dic, steps = self._search(self._dict, key)
        if key not in dic:
            dic[key] = value
        else:
            raise Exception("Duplicate keys added")
        return steps

    def search_element(self, key):
        dic, steps = self._search(self._dict, key)
        if key in dic:
            return key, dic[key], steps
        return None, None, steps


if __name__ == "__main__":
    AlphaList().test(10*1000)