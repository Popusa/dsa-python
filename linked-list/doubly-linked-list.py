#This is the exercise for this data structure.
class node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

##TO BE EDITED

class doubly_linked_list:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,data):
        added_node = node(data,self.head)
        self.head = added_node
    
    def insert_at_end(self,data):
        if self.head == None:
            self.head = node(data,None)
            return
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = node(data,None)
    # Setting new_list flag to true will add list of values to current list. If it is kept false,
    # a new linked list will be made with the list of values only.
    def insert_values(self,arr,new_list = False):
        if  not new_list:
            self.head = None
        else:
            pass
        for data in arr:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        if self.head == None:
            print("Linked list is empty.")
            return
        
        if self.head.data == data_after:
            self.head.next = node(data_to_insert,self.head.next)
        
        found_data = False
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = node(data_to_insert,itr.next)
                found_data = True
                break
            else:
                itr = itr.next
        if not found_data:
            print("Data not found.")

    #Setting the first_only flag to be false will cause the list to find all nodes with the corresponding data and remove them.
    #Keeping it at true will only remove the first occurrence.
    def remove_by_value(self, data,first_only = True):
        if self.head is None:
            print("Linked list is empty.")
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        counter = 0
        found_data = False
        itr = self.head
        while itr:
            if itr.data == data:
                found_data = True
                self.remove_at_index(counter)
                if first_only:
                    break
                else:
                    itr.next = next
            else:
                itr = itr.next
                counter = counter + 1
        
        if not found_data:
            print("Data not found.")

    def remove_beginning(self):
        self.head = self.head.next
    
    def remove_end(self):
        itr = self.head
        counter = 0
        while itr:
            if counter == self.get_length() - 2:
                itr.next = None
            else:
                itr = itr.next
                counter = counter + 1

    def insert_at_index(self,index,data):
        if index < 0 or index >= self.get_length():
            print("Invalid Index")
            return
        
        if index == 0:
            self.insert_at_beginning(data)
            return

        if index == self.get_length() - 1:
            self.insert_at_end(data)
        
        counter = 0
        itr = self.head
        while itr:
            if counter == index - 1:
                itr.next = node(data,itr.next)
                break
            else:
                itr = itr.next
                counter = counter + 1

    def remove_at_index(self,index):
        if index < 0 or index >= self.get_length():
            print("Invalid Index")
            return

        if index == 0:
            self.remove_beginning()
            return
        
        if index == self.get_length() - 1:
            self.remove_end()
            return
        else:
            counter = 0
            itr = self.head
            while itr:
                if counter == index - 1:
                    itr.next = itr.next.next
                    break
                else:
                    counter = counter + 1
                    itr = itr.next

    def print_ll(self):
        if self.head == None:
            print("linked list is empty")
        ll_str = ""
        itr = self.head
        while itr:
            if itr.next == None:
                ll_str = ll_str + str(itr.data)
            else:
                ll_str = ll_str + str(itr.data) + " ---> "
            itr = itr.next

        print(ll_str)

    def get_length(self):
        counter = 0
        itr = self.head
        while itr:
            counter = counter + 1
            itr = itr.next
        return counter

if __name__ == '__main__':
    ll = doubly_linked_list()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_ll()
    ll.insert_after_value("mango","apple")
    ll.print_ll()
    ll.remove_by_value("orange")
    ll.print_ll()
    ll.remove_by_value("figs")
    ll.print_ll()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print_ll()