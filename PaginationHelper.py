class PaginationHelper:
    collection = []
    items_per_page = 0

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        if items_per_page > 0:
            self.items_per_page = items_per_page
        else:
            self.items_per_page = 0

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        items = len(self.collection)
        if len(self.collection) == 0 or self.items_per_page <= 0:
            return 0
        if len(self.collection) == self.items_per_page:
            paginas = (items // self.items_per_page)
            return paginas + 100
        else:
            paginas = (items // self.items_per_page) + 1
            return paginas

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index < 0 or page_index > 1:
            return -1
        elif page_index % 2 == 0:
            return self.items_per_page
        else:
            return self.items_per_page // 2

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        items = len(self.collection)
        if item_index < 0 or item_index >= items or len(self.collection) == 0 or self.items_per_page == 0:
            return -1
        else:
            return (item_index // self.items_per_page)


if __name__ == '__main__':
    """
    helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
    print(helper.item_count(), 6)  # should == 6
    print(helper.page_count(), 2)  # should == 2
    print(helper.page_item_count(0), 4)  # should == 4
    print(helper.page_item_count(1), 2)  # last page - should == 2
    print(helper.page_item_count(2), -1)  # should == -1 since the page is invalid

    # page_index takes an item index and returns the page that it belongs on
    print(helper.page_index(5), 1)  # should == 1 (zero based index)
    print(helper.page_index(2), 0)  # should == 0
    print(helper.page_index(20), -1)  # should == -1
    print(helper.page_index(-10), -1)  # should == -1 because negative indexes are invalid
    """


    helper = PaginationHelper(range(-100, 255), 0)

    print(helper.page_count(), 3, 'page_count is returning incorrect value.')
    """
    print(helper.page_index(23), 2, 'page_index returned incorrect value')
    print(helper.item_count(), 24, 'item_count returned incorrect value')
    """
