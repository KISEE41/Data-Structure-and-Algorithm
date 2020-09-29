class Node:
    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

    def __str__(self):
        return self.data


class List:
    def __init__(self):
        self.head = None

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        # Initially
        if self.head is None:
            self.head = Node(data)
            return

        node = Node(data, self.head)
        self.head.previous = node
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            print("list is empty. So inserting in list.")
            self.insert_at_begining(data)

        itr = self.head
        while itr:
            if itr.next is None:
                node = Node(data, None, self.head)
                itr.next = node
                break
            itr = itr.next

    def insert_after(self, node, data):
        if data is None:
            raise Exception("Insert the valid data!!!")

        itr = self.head 
        while itr:
            if itr.data == node:
                itr.next = Node(data, itr.next, itr)
                break
            itr = itr.next

            if itr.next is None:
                print("Inserting at end")
                self.insert_at_end(data)
                break
    
    def insert_before(self, node, data):
        if data is None:
            raise Exception("Insert the valid data!!!")

        itr = self.head 
        while itr:
            if itr.data is node:
                node = Node(data, itr, itr.previous.next)
                #print(node)
                itr.previous = node
                #print(itr)
                itr = itr.previous.previous
                #print(itr)
                itr.next = node
                #print(itr)
                break

            elif itr.next is None:
                print("Inserting at end")
                self.insert_at_end(data)
                break

            itr = itr.next

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += ' --> ' + str(itr.data)
            itr = itr.next
        print(llstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            self.head.previous = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.previous.next = itr.next
                if itr.next:
                    itr.next.previous = itr.previous
                break

            itr = itr.next
            count+=1


if __name__ == "__main__":
    list = List()
    list.insert_at_begining('b')
    list.insert_at_begining('a')
    list.insert_at_end('d')
    list.insert_at_end('f')
    list.insert_at_end('h')
    list.insert_after('e', 'd')
    list.insert_after('f', 'g')
    list.insert_before('d', 'c')
    print("From forward propagation:")
    list.print_forward()
    list.remove_at(4)
    print("From forward propagation:")
    list.print_forward()
