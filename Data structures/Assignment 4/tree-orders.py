# python3

import sys, threading
sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size

class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrderTraversal(self, index):
        if index == -1:
            return
        self.inOrderTraversal(self.left[index])
        self.result.append(self.key[index])
        self.inOrderTraversal(self.right[index])

    def inOrder(self):
        self.result = []
        self.inOrderTraversal(0)
        return self.result

    def preOrderTraversal(self, index):
        if index == -1:
            return
        self.result.append(self.key[index])
        self.preOrderTraversal(self.left[index])
        self.preOrderTraversal(self.right[index])

    def preOrder(self):
        self.result = []
        self.preOrderTraversal(0)
        return self.result

    def postOrderTraversal(self, index):
        if index == -1:
            return
        self.postOrderTraversal(self.left[index])
        self.postOrderTraversal(self.right[index])
        self.result.append(self.key[index])

    def postOrder(self):
        self.result = []
        self.postOrderTraversal(0)
        return self.result

def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
