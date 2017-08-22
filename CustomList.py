
class CustomList:
    FOUND = TrueH = 3  # the amount of items that is the needed amount for manual search

    def __init__(self):
        """ Constructor for creating the List object, the internal lists of keys and values is initialized"""
        pass

    def search_element(self, key):
        """
        Searching for a element in the list
        :param key: The item that is searched for
        :return:
            key: The key of the found item
            value: The value of the found item
            steps: The steps needed for finding the key
        """
        pass

    def add_element(self, key, value):
        """
        Add a element to the list
        :param key: The key of the element (is searched for etc..)
        :param value: The value corresponding to the key (can anything like objects/integers/strings)
        :return: Returns the amount of steps that is needed to add this element
        """
        pass

    def test(self, elements_amount=1000):
        """
        A method for testing the list on efficiency and speed
        :param elements_amount:
        :return: TODO add return value
        """
        import time

        steps_needed = 0
        items = []
        start_time = time.time()

        # add all the requested elements to the list
        from string import ascii_letters, digits
        import random
        key_range = ascii_letters + digits
        key_length = 10
        for item in range(0, elements_amount):
            if item % (elements_amount/100) == 0:
                print("filling {:,}/{:,}".format(item + (elements_amount/100), elements_amount))
            key = "".join(key_range[random.randrange(0, len(key_range))] for x in range(0, key_length))
            items.append(key)
            steps_needed += self.add_element(key, item)

        fill_time = time.time() - start_time
        fill_steps = steps_needed
        fill_avg_time = fill_time / elements_amount
        fill_avg_steps = fill_steps / elements_amount
        steps_needed = 0
        start_time = time.time()

        print("\ndone filling! starting searching ...\n")

        # search all the elements in the list
        for item in range(0, elements_amount):
            if item % (elements_amount/100) == 0:
                print("searching {:,}/{:,}".format(item + (elements_amount/100), elements_amount))
            key, value, steps = self.search_element(items[item])
            steps_needed += steps
            if key != items[item]:
                raise Exception("The found key: {} is not equal to searched key: {}".format(key, items[item]))

        search_time = time.time() - start_time
        search_steps = steps_needed
        search_avg_time = search_time / elements_amount
        search_avg_steps = search_steps / elements_amount

        print("-" * 40)
        print("\n{:,} time needed to fill".format(fill_time))
        print("{:,} steps needed to fill".format(fill_steps))
        print("{} avg time needed to fill".format(fill_avg_time))
        print("{} avg steps needed to fill".format(fill_avg_steps))

        print("\n{:,} time needed to search".format(search_time))
        print("{:,} steps needed to search".format(search_steps))
        print("{} avg time needed to search".format(search_avg_time))
        print("{} avg steps needed to search".format(search_avg_steps))
