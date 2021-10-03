from threading import Thread
import time


class CrossSearch:

    def __init__(self, list_data: list, element):
        #  Initializing variables asper the arguments.
        self.element = element
        self.list = list_data
        self.searching = True
        self.index = None
    
    # Function to start searching, it starts a thread for forward function
    # and then starts the reverse function in main thread.
    # It also returns the result i.e the index of the element
    # which will be found by the reverse or forward function
    def search(self):
        Thread(self.forward())
        self.reverse()
        return self.index
 
    # This function checks the element from end.
    def reverse(self):
        len_all = len(self.list)
        for i in range(len(self.list) - 1):
            try:
                if not self.searching:
                    break
                i = len_all - i
                if self.list[i] == self.element:
                    self.searching = False
                    self.index = i
                    break
            except Exception:
                pass

    # This function checks the element from start.
    def forward(self):
        for i in range(len(self.list) - 1):
            try:
                if not self.searching:
                    break
                if self.list[i] == self.element:
                    self.searching = False
                    self.index = i
                    break
            except Exception:
                pass


list_i = [i for i in range(800, 9800)]
print("Searching by my algorithm...")

index_element = CrossSearch(list_i, 8999).search()
print(index_element)
