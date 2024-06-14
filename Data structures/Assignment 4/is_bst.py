#!/usr/bin/python3

import sys
import threading

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**25)   # new thread will get stack of such size

def IsBinarySearchTree(tree):
    if not tree:
        return True

    stack = [(0, float('-inf'), float('inf'))]

    while stack:
        index, min_key, max_key = stack.pop()
        if index == -1:
            continue
        key, left, right = tree[index]
        if key < min_key or key >= max_key:
            return False
        stack.append((right, key, max_key))
        stack.append((left, min_key, key))

    return True

def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for _ in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()


