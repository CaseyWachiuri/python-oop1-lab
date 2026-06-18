#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        if ( page_count.isdigit() ):
            self.page_count = page_count
        else:
            print("page_count must be an integer")

        self.title = title

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
