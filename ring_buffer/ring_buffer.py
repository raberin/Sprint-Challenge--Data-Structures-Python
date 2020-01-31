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
            self.current = self.storage.head
        # If it has reached max capacity replace head with new val
        else:
            if self.current == self.storage.tail:
                next_oldest_node = self.storage.head
            else:
                # Save node after current
                next_oldest_node = self.current.next
            # Overwrite currents value with new item
            self.current.value = item
            # Set node after current as current
            self.current = next_oldest_node

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # TODO: Your code here
        current = self.storage.head
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
