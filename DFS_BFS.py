class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|--' if self.parent else " " * 3
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def DFS(self, stack=[]):
        stack.append(self.data)
        if self.children:
            for child in self.children:
                child.DFS()
        return stack

    def BFS(self, queue=[], visited=[]):
        visited.append(self)
        queue.append(self)
        while queue:
            s = queue.pop(0)
            for child in s.children:
                visited.append(child)
                queue.append(child)

        return visited


def build_tree(): 
    root = Node('A')
    B = Node('B')
    C = Node('C')
    D = Node('D')
    E = Node('E')
    F = Node('F')
    G = Node('G')

    root.add_child(B)
    root.add_child(C)

    B.add_child(D)
    B.add_child(E)

    C.add_child(F)
    C.add_child(G)

    return root

if __name__ == "__main__":
    root = build_tree()
    print("-----------------------------------------------------------------")
    print("The tree looks like:")
    root.print_tree()
    print("-----------------------------------------------------------------")
    print("The DFS traversal is:")
    res = root.DFS()
    result = ''
    for i in res:
        result += '-->' + str(i)
    print(result)

    print("The BFS traversal is:")
    queue = root.BFS()
    result = ''
    for i in queue:
        result += '-->' + str(i.data)
    print(result)
    