#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_Count):
        self.title = title
        self.page_Count = page_Count
        if (self.page_Count.isdigit()):
            print(f"page_count must be an integer") 

    def turn_page():
        print("Flipping the page...wow, you read fast!")
