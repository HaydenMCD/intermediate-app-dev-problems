import time


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LLIterator:
    def __init__(self, ll):
        self.ll = ll
        self.next_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self.ll.get(self.next_index)
            self.next_index += 1
            return result
        except IndexError:
            raise StopIteration


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        if self.head.data is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    # Pop function
    def pop(self):
        if self.head.next is None:
            if self.head.data is None:
                # Error checking incase list is empty
                raise IndexError("The list is empty, Please add data")
            else:
                data = self.head.data
                self.head.data = None
                return data
        else:
            previous_node = Node()
            current_node = self.head
            while current_node.next:
                previous_node = current_node
                current_node = current_node.next
            previous_node.next = None
            return current_node.data

    # Get function
    def get(self, index):
        if index >= 0:
            if index >= len(self):
                raise IndexError('Index is out of bounds')
            current_index = 0
            current_node = self.head
            while True:
                if current_index == index:
                    return current_node.data
                current_node = current_node.next
                current_index += 1
        else:
            if abs(index) > len(self):
                raise IndexError('Index is out of bounds')
            current_index = -1 * len(self)
            current_node = self.head
            while True:
                if current_index == index:
                    return current_node.data
                current_node = current_node.next
                current_index += 1

    # Length Function
    def __len__(self):
        count = 0
        if self.head.next is None:
            if self.head.data is None: #If head is empty return count (0)
                return count
            else:
                count += 1
                return count
        else:
            count += 1
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
                count += 1
            return count

    def __iter__(self):
        return LLIterator(self)


def main():
    ll = LinkedList()

    print('I will add 10 numbers to the list')
    for i in range(1, 11):
        ll.append(i)

    print('======================================================================')
    time.sleep(2)

    print('I will now delete the last 5 numbers from the list')
    for i in range(4):
        print(f'Number: {ll.pop()} has been deleted\n')

    print('======================================================================')
    time.sleep(2)

    print(f'The length of the linked list is: {len(ll)}')

    print('======================================================================')
    time.sleep(2)

    print('The numbers left in the list are:')
    for item in ll:
        print(item)
    print('\n======================================================================')


if __name__ == '__main__':
    main()
