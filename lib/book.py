#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_Count):
        self.title = title
        self.page_Count = page_Count

    def set_page_Count(self, value):
        if (self.page_Count.isdigit()):
            self._page_Count = value
        else:
            print(f"page_count must be an integer") 

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
