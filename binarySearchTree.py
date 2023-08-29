class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.leftChild = left
        self.rightChild = right

    def search(self, searchValue):
        if self is None or self.value == searchValue:
            return self
        elif searchValue < self.value:
            if self.leftChild is None:
                return None
            return self.leftChild.search(searchValue)
        else:
            if self.rightChild is None:
                return None
            return self.rightChild.search(searchValue)

    def insert(self, value):
        if value < self.value:
            if self.leftChild is None:
                self.leftChild = TreeNode(value)
            else:
                self.leftChild.insert(value)
        elif value > self.value:
            if self.rightChild is None:
                self.rightChild = TreeNode(value)
            else:
                self.rightChild.insert(value)

    def delete(self, valueToDelete):
        if self is None:
            return None
        elif valueToDelete < self.value:
            if self.leftChild is not None:
                self.leftChild = self.leftChild.delete(valueToDelete)
        elif valueToDelete > self.value:
            if self.rightChild is not None:
                self.rightChild = self.rightChild.delete(valueToDelete)
        elif valueToDelete == self.value:
            if self.leftChild is None:
                return self.rightChild
            elif self.rightChild is None:
                return self.leftChild
            else:
                self.rightChild, self.value = self.rightChild.lift(self)
        return self

    def lift(self, nodeToDelete):
        if self.leftChild:
            self.leftChild, value = self.leftChild.lift(nodeToDelete)
            self.value = value
            return self, value
        else:
            nodeToDelete.value = self.value
            return self.rightChild, self.value


    def traverse_and_print(self):
        if self is None:
            return
        if self.leftChild:
            self.leftChild.traverse_and_print()
        print(self.value)
        if self.rightChild:
            self.rightChild.traverse_and_print()


if __name__ == "__main__":
    # Create a sample binary search tree
    root = TreeNode(5)
    root.insert(3)
    root.insert(7)
    root.insert(2)
    root.insert(4)
    root.insert(6)
    root.insert(8)

    print("Original Tree:")
    root.traverse_and_print()

    # Search for a value
    search_value = 4
    result = root.search(search_value)
    if result:
        print(f"Found {search_value} in the tree.")
    else:
        print(f"{search_value} not found in the tree.")

    # Delete a node
    delete_value = 5
    root = root.delete(delete_value)

    print("Tree after deleting node with value 5:")
    root.traverse_and_print()
