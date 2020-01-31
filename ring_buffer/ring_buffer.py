from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # If capacity < len(storage) add to tail
        if self.capacity > self.storage.length:
            # Add to tail
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        # If it has reached max capacity replace head with new val
        else:
            # Remove oldest aka head and append new node
            print(self.storage.head)
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # TODO: Your code here
        current = self.current
        while current:
            list_buffer_contents.append(current.value)
            current = current.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
