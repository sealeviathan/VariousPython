class LinkNode:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.root = None
        self.end = None
        self.size = 0

    def Append(self, item):
        if self.root is None:
            n = LinkNode(item)
            self.root = n
            self.end = n
            self.size += 1
            return True
        appendNode = LinkNode(item)
        oldRoot = self.root
        self.root = appendNode
        appendNode.next = oldRoot
        oldRoot.prev = self.root
        self.size += 1

    def Pop(self, index):
        if self.size == 1:
            item = self.root.item
            self.root = None
            self.end = None
            self.size -= 1
            return item
        elif self.size > 0:
            i = index
            if index < 0:
                i = self.size + index
            #If there is a list, set the index relatively. As such, 0 <= i < self.size
            #If input index is negative, go to the end of the list and move backwards, inclusive of course
            #So that -1 = last element instead of second to last
            if index == 0:
                #pop the root
                item = self.root.item
                self.root = self.root.next
                self.root.prev = None
                self.size -= 1
                return item
            elif index == -1:
                #pop the end
                item = self.end.item
                self.end = self.end.prev
                self.end.next = None
                self.size -= 1
                return item
            else:
                if i < self.size//2 + 1:
                    # if index is in the first half, start from the beginning and go to the middle
                    current = self.root
                    n = 0
                    while n < i:
                        if current.next is None:
                            raise IndexError('Forwards traversal, next step is a NoneType!')
                        current = current.next
                        n += 1
                    item = current.item
                    current.prev.next = current.next
                    self.size -= 1
                    return item
                else:
                    # if index is in the last half, start from the end and go backwards to the middle
                    current = self.end
                    n = self.size - 1
                    while n > i:
                        if current.prev is None:
                            raise IndexError('Backwards traversal, next step is a NoneType!')
                        current = current.prev
                        n -= 1
                    item = current.item
                    current.prev.next = current.next
                    self.size -= 1
                    return item

            #With access to the next and previous, operations become much different than usual.

        #S.E.
        raise IndexError('List is empty!')
        return None

    def Exists(self, item):
        current = self.root
        while current is not None:
            if current.item == item:
                return True
            current = current.next
        return False

    def __getitem__(self, index):
        if self.size > 0:
            i = index
            if index < 0:
                i = self.size + index
            print(f'u{i}u')
            #If there is a list, set the index relatively. As such, 0 <= i < self.size
            #If input index is negative, go to the end of the list and move backwards, inclusive of course
            #So that -1 = last element instead of second to last
            if index == 0:
                return self.root.item
            elif index == -1:
                return self.end.item
            else:
                if i < self.size//2 + 1:
                    # if index is in the first half, start from the beginning and go to the middle
                    current = self.root
                    n = 0
                    while n < i:
                        if current.next is None:
                            raise IndexError('Forwards traversal, next step is a NoneType!')
                        current = current.next
                        n += 1
                    return current.item
                else:
                    # if index is in the last half, start from the end and go backwards to the middle
                    current = self.end
                    n = self.size - 1
                    if n < i:
                        raise IndexError('Index out of range!')
                    while n > i:
                        if current.prev is None:
                            raise IndexError('Backwards traversal, next step is a NoneType!')
                        current = current.prev
                        n -= 1
                    return current.item

        raise IndexError('List is empty!')
        return None

    def __setitem__(self, index, value):
        if self.size > 0:
            i = index
            if index < 0:
                i = self.size + index
            #If there is a list, set the index relatively. As such, 0 <= i < self.size
            #If input index is negative, go to the end of the list and move backwards, inclusive of course
            #So that -1 = last element instead of second to last
            if index == 0:
                self.root.item = value
                return True
            elif index == -1:
                self.end.item = value
                return True
            else:
                if i < self.size//2 + 1:
                    # if index is in the first half, start from the beginning and go to the middle
                    current = self.root
                    n = 0
                    while n < i:
                        if current.next is None:
                            raise IndexError('Forwards traversal, next step is a NoneType!')
                        current = current.next
                        n += 1
                    current.item = value
                    return True
                else:
                    # if index is in the last half, start from the end and go backwards to the middle
                    current = self.end
                    n = self.size - 1
                    if n < i:
                        raise IndexError('Index out of range!')
                    while n > i:
                        if current.prev is None:
                            raise IndexError('Backwards traversal, next step is a NoneType!')
                        current = current.prev
                        n -= 1
                    current.item = value
                    return True

        raise IndexError('List is empty!')
        return False

    def __len__(self):
        return self.size

    def __contains__(self, item):
        return self.Exists(item)
