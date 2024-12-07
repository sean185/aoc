
eg1 = [[[[[9,8],1],2],3],4]
eg2 = [7,[6,[5,[4,[3,2]]]]]
eg3 = [[6,[5,[4,[3,2]]]],1]
eg4 = [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]

class Node():
    left, right = None, None
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Tree():
    order = []
    def __init__(self, sfnum):
        def make_tree(sfnum):
            L, R = sfnum
            if type(L) == int and type(R) == int:
                self.add(Node(L, R))
            if type(L) == list:
                self.add(Node(L, R))
                node = make_tree(sfnum)
            else:
                [make_tree
        
    def add(self, node):
        self.order.append(node)
