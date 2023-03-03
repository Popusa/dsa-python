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
    
    def print_forward(self):
        if self.head == None:
            print("linked list is empty.")
            return
        
        itr = self.head
        ll_str = ""
        while itr:
            if itr.next == None:
                ll_str = ll_str + itr.data
            else:    
                ll_str = ll_str + itr.data + " ---> "
            itr = itr.next

        print(ll_str)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

    def print_backward(self):
        last_node = None
        if self.head == None:
            print("linked list is empty.")
            return
        
        itr = self.get_last_node()
        ll_str = ""
        while itr:
            if itr.prev == None:
                ll_str = ll_str + itr.data
            else:    
                ll_str = ll_str + itr.data + " ---> "         
            itr = itr.prev
        print(ll_str)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        if self.head == None:
            node = node(data, self.head, None)
            self.head = node
        else:
            node = node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = node(data, None, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = node(data, None, itr)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

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
    ll.print_forward()
    ll.print_backward()