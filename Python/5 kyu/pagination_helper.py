"""
5 kyu - PaginationHelper

For this exercise you will be strengthening your page-fu mastery. You will complete the PaginationHelper class, which is a utility class helpful for querying paging information related to an array.

The class is designed to take in an array of values and an integer indicating how many items will be allowed per each
page. The types of values contained within the collection/array are not relevant.

The following are some examples of how this class is used:

var helper = new PaginationHelper(['a','b','c','d','e','f'], 4);
helper.pageCount(); //should == 2
helper.itemCount(); //should == 6
helper.pageItemCount(0); //should == 4
helper.pageItemCount(1); // last page - should == 2
helper.pageItemCount(2); // should == -1 since the page is invalid

// pageIndex takes an item index and returns the page that it belongs on
helper.pageIndex(5); //should == 1 (zero based index)
helper.pageIndex(2); //should == 0
helper.pageIndex(20); //should == -1
helper.pageIndex(-10); //should == -1
"""


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
        return math.ceil(self.item_count() / self._items_per_page)

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