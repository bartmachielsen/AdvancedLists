from CustomList import CustomList


class QuickList(CustomList):
    """
    QuickList is a simple list that uses the following method:

        It makes sure that all the elements are character-arrays ( strings)
        All the elements are alphabetical sorted to make searching easy

        The element/position of element are found by the following way:

            The list is splitted and the middle element is compared to the key (where we are searching for)
            If the middle element is smaller than the key then we search the bottom half of the list.
            If the key is larger than the middle element then the top half is searched
            --> This method is continued until the list is too small.
            Then the elements are manual searched for the correct key

            If the key is not found then the position of the key is returned. New keys are placed on the given pos.

    """
    FOUND = True  # used for returning if the key is found
    NOT_FOUND = False  # used for returning if the key is found
    ERROR = None  # used for returning that there occurred a error in searching the key

    MANUAL_SEARCH = 3  # the amount of items that is the needed amount for manual search

    def __init__(self):
        """ Constructor for creating the List object, the internal lists of keys and values is initialized"""
        CustomList.__init__(self)
        self._list = []
        self._values = []

    @staticmethod
    def _search(lst, key, start=0, end=-1, steps=0):
        """
        Search the list for a certain key
        :param lst: The list that is searched for
        :param key: The key that needs to be found
        :param start: The index to start from (default: 0)
        :param end: The search-limit (default: the size of lst)
        :param steps: Used for keeping track of the steps needed to find the key (or the usual place)
        :return: The amount of steps that are used
        """
        if end == -1:  # search whole list
            end = len(lst)

        if end == 0:  # empty list!
            return None, QuickList.ERROR, steps

        if (end-start) <= QuickList.MANUAL_SEARCH:
            # Used when the total amount of items that we are searching is too small
            # --> we are going to search manual and return when not found!
            for index, item in enumerate(lst[start:end]):
                steps += 1
                if item == key:
                    return start + index, QuickList.FOUND, steps
                steps += 1
                if item > key:
                    return start + index , QuickList.NOT_FOUND, steps
            return end, QuickList.NOT_FOUND, steps

        # calculate which element is the middle (rounded to bottom)
        middle = start+int((end-start) / 2)

        if lst[middle] == key:
            # check if the middle element is the element we are searching for (lucky you then!)
            return middle, QuickList.FOUND, steps
        if lst[middle] > key:
            # check if the middle element is larger than the element we are sarching for
            # --> look for key in the first half, limit the list
            return QuickList._search(lst, key, start, middle, steps + 2)
        elif lst[middle] < key:
            # check if the middle element is smaller than the element we are sarching for
            # --> look for key in the second half, limit the list
            return QuickList._search(lst, key, middle, end, steps + 2)

    def search_element(self, key):
        """
        Searching for a element in the list
        :param key: The item that is searched for
        :return:
            key: The key of the found item
            value: The value of the found item
            steps: The steps needed for finding the key
        """
        index, result, steps = QuickList._search(self._list, key)

        if result == QuickList.FOUND:
            return self._list[index], self._values[index], steps
        return None, None, steps

    def add_element(self, key, value):
        """
        Add a element to the list
        :param key: The key of the element (is searched for etc..)
        :param value: The value corresponding to the key (can anything like objects/integers/strings)
        :return: Returns the amount of steps that is needed to add this element
        """
        result = QuickList._search(self._list, key)
        index = result[0]
        if index is None:
            index = 0
        self._list.insert(index, key)
        self._values.insert(index, value)
        return result[2]


def test():
    q_list = QuickList()

    import random
    import string
    length = 10

    amount = 500*1000
    total_steps = 0
    for i in range(0, amount):
        if i > 0 and i % 1000 == 0:
            print("{} - {}".format(i, total_steps/(i-1)))
        key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))
        total_steps += q_list.add_element(key, i)

    total_steps = 0
    for i in range(0, amount):
        if i > 0 and i % 1000 == 0:
            print("{} - {}".format(i, total_steps/(i-1)))
        index, value, steps = q_list.search_element(q_list._list[i])
        total_steps += steps
    print("steps: {} average: {}".format(total_steps, total_steps/amount))

if __name__ == "__main__":
    # test()
    QuickList().test(1000*1000)
