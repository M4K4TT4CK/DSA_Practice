class MinHeap:

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

        while newNodeIndex > 0:
            parentIndex = self.parentIndex(newNodeIndex)
            if self.data[newNodeIndex] < self.data[parentIndex]:  # Compare with parent (for min-heap)
                self.data[newNodeIndex], self.data[parentIndex] = self.data[parentIndex], self.data[newNodeIndex]  # Swap if needed
                newNodeIndex = parentIndex
            else:
                break

    # Deletion
    def deletion(self):
        if not self.data:
            return None

        # Swap the root (smallest) with the last element
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        valueToDelete = self.data.pop()  # Remove the smallest element
        
        trickleNodeIndex = 0

        while self.hasSmallerChild(trickleNodeIndex):
            smallerChildIndex = self.calculateSmallerChildIndex(trickleNodeIndex)
            if self.data[trickleNodeIndex] > self.data[smallerChildIndex]:  # Compare with smaller child (for min-heap)
                self.data[trickleNodeIndex], self.data[smallerChildIndex] = self.data[smallerChildIndex], self.data[trickleNodeIndex]  # Swap if needed
                trickleNodeIndex = smallerChildIndex
            else:
                break

        return valueToDelete

    def hasSmallerChild(self, index):
        left_child_index = self.leftChildIndex(index)
        right_child_index = self.rightChildIndex(index)
        if left_child_index < len(self.data) and right_child_index < len(self.data):
            return self.data[left_child_index] < self.data[index] or self.data[right_child_index] < self.data[index]
        elif left_child_index < len(self.data):
            return self.data[left_child_index] < self.data[index]
        elif right_child_index < len(self.data):
            return self.data[right_child_index] < self.data[index]
        return False

    def calculateSmallerChildIndex(self, index):
        left_child_index = self.leftChildIndex(index)
        right_child_index = self.rightChildIndex(index)
        if right_child_index < len(self.data) and self.data[right_child_index] < self.data[left_child_index]:
            return right_child_index
        else:
            return left_child_index

if __name__ == "__main__":
    # Create a min-heap instance
    my_heap = MinHeap()

    # Insert some values into the heap
    my_heap.insert(5)
    my_heap.insert(10)
    my_heap.insert(7)
    my_heap.insert(3)
    my_heap.insert(15)

    # Print the current heap data
    print("Heap Data:", my_heap.data)

    # Delete the root node (smallest element)
    deleted_value = my_heap.deletion()
    print("Deleted Value:", deleted_value)

    # Print the updated heap data
    print("Updated Heap Data:", my_heap.data)
