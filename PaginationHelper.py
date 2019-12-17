# TODO: complete this class
import math


class PaginationHelper:
    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self._collection = collection
        self._items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self._collection)

    # returns the number of pages
    def page_count(self):
        return int(math.ceil(self.item_count() / self._items_per_page))

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        # check if its out of range
        if (page_index + 1) > self.page_count() or page_index < 0:
            return -1
        # check if its the last page
        if (page_index + 1) * self._items_per_page > self.item_count():
            return self.item_count() % self._items_per_page
        return self._items_per_page

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index > (self.item_count() - 1) or item_index < 0:
            return -1
        return math.ceil((item_index + 1) / self._items_per_page) - 1


"""
collection = range(1, 25)
helper = PaginationHelper(collection, 10)
print(helper.page_count())  # should == 3
print((helper.page_index(23)))  # should == 2
print(helper.item_count())  # should == 24

helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
print("")
print(helper.page_count())  # should == 2
print(helper.item_count())  # should == 6
print(helper.page_item_count(0))  # should == 4
print(helper.page_item_count(1))  # last page - should == 2
print(helper.page_item_count(2))  # should == -1 since the page is invalid
print("")
# page_index takes an item index and returns the page that it belongs on
print(helper.page_index(5))  # should == 1 (zero based index)
print(helper.page_index(2))  # should == 0
print(helper.page_index(20))  # should == -1
print(helper.page_index(-10))  # should == -1 because negative indexes are invalid 
"""
