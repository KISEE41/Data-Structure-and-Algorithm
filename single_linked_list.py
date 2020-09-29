#Every node is represented by an object
class Node:
    def __init__(self, data, next=None):
        #data is the real data of a node
        self.data = data           
        #next represent to an object next to the node.
        # At default it is None notifying there no any node     
        self.next = next


class List:
    def __init__(self):
        # At the begining there is no any node
        self.head = None

    def insert_at_begining(self, data):
        self.head = Node(data, self.head)

    def insert_at_end(self, data):
        if self.head is None:
            print('List is Null so creating list')
            self.insert_at_begining(data)
            return

        # temporary variable for traversal
        itr = self.head
        while itr.next:
            itr = itr.next
            if itr.next is None:
                node = Node(data)
                itr.next = node
                break
    
    def insert_after_node(self, node, data):
        if data is None:
            raise Exception("Insert the valid data!!!")
        
        itr = self.head
        while itr:
            if itr.data == node:
                itr.next = Node(data, itr.next)
                break
            
            itr = itr.next

            if itr.next is None:
                print("Inserting at end")
                self.insert_at_end(data)
                break

    def remove_node(self, node):
        if self.head is None:
            return

        if self.head.data == node:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == node:
                itr.next = itr.next.next
                break
            itr = itr.next
    
    def printing_list(self):
        if self.head is None:
            print("List is empty")

        first_node = self.head
        traversal = '' 
        itr = self.head   
        while itr is not None:
            traversal +=  '->' + itr.data 
            itr = itr.next    
        print(traversal)
        print(f"The length of list is {self.length_of_list()}")


    def length_of_list(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count


if __name__ == "__main__":
    linked_list = List()
    linked_list.insert_at_begining('apple')
    linked_list.insert_at_begining('banana')
    linked_list.insert_at_begining('carrot')
    linked_list.insert_after_node('carrot', 'rabbit')
    linked_list.insert_at_end('dan')
    linked_list.printing_list()
    linked_list.remove_node('rabbit')
    linked_list.printing_list()