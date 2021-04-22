class LinkNode:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None
        self.size = 0

    def Append(self, item):
        if self.root is None:
            self.root = LinkNode(item)
            self.size += 1
            return True
        appendNode = LinkNode(item)
        oldRoot = self.root
        self.root = appendNode
        appendNode.next = oldRoot
        self.size += 1

    def Pop(self, index):
        if self.size > 0:
            i = index
            if index < 0:
                i = self.size + index
            #If there is a list, set the index relatively. As such, 0 <= i < self.size
            #If input index is negative, go to the end of the list and move backwards, inclusive of course
            #So that -1 = last element instead of second to last
            current = self.root
            if i == 0:
                if current.next is None:
                    item = self.root.item
                    self.root = None
                    self.size -= 1
                    return item
                elif current.next is not None:
                    item = self.root.item
                    self.root = current.next
                    self.size -= 1
                    return item
                else:
                    print("Error indexing: next index is none")
                    return None
            #checked for the initial item due to the way rechaining operates
            elif i == 1:
                if current.next is not None:
                    item = current.next.item
                    if current.next.next is None:
                        self.root.next = None
                        self.size -= 1
                        return item
                    else:
                        self.root.next = current.next.next
                        self.size -= 1
                        return item
                else:
                    print("Error indexing: next index is none")
                    return None
            #checked for the second item due to the way rechaining operates
            n = 0
            while n < i - 1:
                if current.next is None:
                    print("Error indexing: next index is none")
                    return None
                current = current.next
                n += 1
            #looped through nexts until we reached the one before the one we want
            item = current.next.item
            current.next = current.next.next
            #rechained
            self.size -= 1
            return item

        print("Error indexing: list is empty")
        return None


    def Exists(self, item):
        current = self.root
        while current is not None:
            if current.item == item:
                return True
            current = current.next
        return False

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        pass

    def __len__(self):
        return self.size
