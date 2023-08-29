class MaxHeap:

    def __init__(self):
        self.data = []

    # Return root node
    def rootNode(self):
        return self.data[0] if self.data else None

    # Return last node
    def lastNode(self):
        return self.data[-1] if self.data else None
    
    # To find the left child of any node -> (index * 2) + 1
    def leftChildIndex(self, index):
        return (index * 2) + 1

    # To find the right child of any node -> (index * 2) + 2
    def rightChildIndex(self, index):
        return (index * 2) + 2

    # To find parent's node we use (index - 1) // 2
    def parentIndex(self, index):
        return (index - 1) // 2

    # Insertion
    def insert(self, value):
        self.data.append(value)
        newNodeIndex = len(self.data) - 1

        while newNodeIndex > 0 and self.data[newNodeIndex] > self.data[self.parentIndex(newNodeIndex)]:
            # Swap the elements if the parent is smaller
            self.data[newNodeIndex], self.data[self.parentIndex(newNodeIndex)] = self.data[self.parentIndex(newNodeIndex)], self.data[newNodeIndex]
            newNodeIndex = self.parentIndex(newNodeIndex)

    # Deletion
    def deletion(self):
        if not self.data:
            return None

        valueToDelete = self.rootNode()
        lastValue = self.data.pop()
        
        if not self.data:
            return valueToDelete

        self.data[0] = lastValue

        trickleNodeIndex = 0

        while self.hasGreaterChild(trickleNodeIndex):
            largerChildIndex = self.calculateLargerChildIndex(trickleNodeIndex)
            self.data[trickleNodeIndex], self.data[largerChildIndex] = self.data[largerChildIndex], self.data[trickleNodeIndex]

            trickleNodeIndex = largerChildIndex
        return valueToDelete

    def hasGreaterChild(self, index):
        left_child_index = self.leftChildIndex(index)
        right_child_index = self.rightChildIndex(index)
        if left_child_index < len(self.data) and right_child_index < len(self.data):
            return self.data[left_child_index] > self.data[index] or self.data[right_child_index] > self.data[index]
        elif left_child_index < len(self.data):
            return self.data[left_child_index] > self.data[index]
        elif right_child_index < len(self.data):
            return self.data[right_child_index] > self.data[index]
        return False

    def calculateLargerChildIndex(self, index):
        left_child_index = self.leftChildIndex(index)
        right_child_index = self.rightChildIndex(index)
        if right_child_index < len(self.data) and self.data[right_child_index] > self.data[left_child_index]:
            return right_child_index
        else:
            return left_child_index

if __name__ == "__main__":
    # Create a heap instance
    my_heap = MaxHeap()

    # Insert some values into the heap
    my_heap.insert(5)
    my_heap.insert(10)
    my_heap.insert(7)
    my_heap.insert(3)
    my_heap.insert(15)

    # Print the current heap data
    print("Heap Data:", my_heap.data)

    # Delete the root node
    deleted_value = my_heap.deletion()
    print("Deleted Value:", deleted_value)

    # Print the updated heap data
    print("Updated Heap Data:", my_heap.data)
