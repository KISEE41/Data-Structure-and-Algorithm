class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert_node(self, data):
        if data == self.data:
            return
        
        # traverse and insertion at left child node
        if data < self.data:
            if self.left:
                self.left.insert_node(data)
            else:
                self.left = TreeNode(data)

        #traverse and insertion at right child node
        if data > self.data:
            if self.right:
                self.right.insert_node(data)
            else:
                self.right = TreeNode(data)

    def in_order_traversal(self):
        elements = []

        #visit left tree first
        if self.left:
            elements += self.left.in_order_traversal()
        
        #append base node
        elements.append(self.data)

        #visit right node
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)

        #visit left child
        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        #visit left leaf node first
        if self.left:
            elements += self.left.post_order_traversal()

        #visit right leaf node after visiting left child node
        if self.right:
            elements += self.right.post_order_traversal()

        #appending base node
        elements.append(self.data)
        return elements

    def search(self, data):
        if self.data == data:
            return print(f"Value found {data}")

        elif data < self.data:
            if self.left:
                self.left.search(data)

            else:
                return print("Value: {data} doesnot exist in tree.") 

        elif data > self.data:
            if self.right:
                self.right.search(data)

            else:
                return print("Value: {data} doesnot exist in tree.") 
        
    def calculate_sum(self):
        if self.left:
            left_sum = self.left.calculate_sum()
        else:
            left_sum = 0
            
        if self.right:
            right_sum = self.right.calculate_sum()

        else: 
            right_sum = 0

        return (self.data + left_sum + right_sum )

    def min_val(self):
        if self.left:
            self.left.min_val()
        else:
            return print(f"Minimum value is {self.data}")

    def max_val(self):
        if self.right:
            self.right.max_val()
        else:
            return print(f"Maximum value is {self.data}")

        def calculate_sum(self):
            if self.left:
                left_sum = self.left.calculate_sum()
            else:
                left_sum = 0
                
            if self.right:
                right_sum = self.right.calculate_sum()

            else: 
                right_sum = 0
            
            
            return (self.data + left_sum + right_sum )
    

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            
            min_value = self.right.find_min()
            self.data = min_value
            self.right = self.right.delete(min_val)
        return self



if __name__ == "__main__":
    numbers = []
    print("Enter the data for node:(first one you enter is root node)")
    print("-------------------------")
    i = 0
    while 1:
        i += 1
        a = int(input(f"{i}th number:".format(i)))
        numbers.append(a)
        choice = str(input("Continue(y/n)"))
        if choice.upper() == 'N':
            break
    
    root = TreeNode(numbers[0])
    for i in range(1, len(numbers)):
        root.insert_node(numbers[i])

    print(f"Inorder Traversal result: {root.in_order_traversal()}")
    print(f"Post Order Traversal result: {root.post_order_traversal()}")
    print(f"Pre Order Traversal result: {root.pre_order_traversal()}")

    print("---------------------------------------------------------------------")
    search = int(input("Which number you want to search:"))
    root.search(search)
    print("---------------------------------------------------------------------")
    root.min_val()
    root.max_val()
    print(f"Sum of all nodes: {root.calculate_sum()}")
    print("---------------------------------------------------------------------")
    delt = int(input("Which node you want to delete:"))
    root.delete(delt)
    print(f"Result after deletion: {root.in_order_traversal()}")

