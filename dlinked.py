#!/usr/bin/env python
# coding: utf-8

# In[4]:


class DLinkedListNode:
    # An instance of this class represents a node in Doubly-Linked List
    def __init__(self,initData,initNext,initPrevious):
        self.data = initData
        self.next = initNext
        self.previous = initPrevious
        
        if initNext != None:
            self.next.previous = self
        if initPrevious != None:
            self.previous.next = self
    


class DLinkedList:
    # An instance of this class represents the Doubly-Linked List
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def clear(self):
        # oriented from the front
        current=self.head
        current.setNext(None)
        self.head=None
        self.size=0

    def peek(self):
        # oriented from tail of list
        current=self.head
        while current.next!=None:
            current=current.next
        return current.data
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.data == item:
                found= True
            else:
                current = current.next
        return found
        
    def index(self, item):
        current = self.head
        found = False
        index = 0
        while current != None and not found:
            if current.data == item:
                found= True
            else:
                current = current.next
                index = index + 1
        if not found:
                index = -1
        return index        
         
    def add(self, item):
        # if our head is nothing we set previous of head to be the new node and then assign head to new node
        temp = DLinkedListNode(item, self.head, None) 
        if self.head != None:
            self.head.setPrevious(temp) 
        else:
            self.tail=temp 
        self.head = temp 
        self.size += 1
        
    def remove(self, item):
        # search for the item and remove it # the method assumes the item exists 
        current = self.head
        previous=None
        found = False
        while not found:
            if current.data == item: found = True
            else:
                # previous is a cursor that tracks the element before current
                previous = current
                current = current.next
        # this implies head needs to be current.next
        if previous == None:
            self.head = current.next
        else:
            # if it isnt the next of previous should be current.getNext( since we remove)
            previous.setNext(current.next)
        if (current.next != None):
            # if we arent at tail we iterate over the list and set previous
            current.next.setPrevious(previous)
        else:
            # if we are at tail set tail = previous
            self.tail=previous
        self.size -= 1
        
        
    def append(self, item):
        # adds the item to the end of the list
        temp=DLinkedListNode(item,None,None)
        if (self.head == None):
            self.head=temp 
        else:
            self.tail.setNext(temp) 
            temp.setPrevious(self.tail)
        self.tail=temp 
        self.size +=1
        
    def insert(self, pos, item):
        # traverse from head 
        # optimizing this we could traverse from tail or head depending on if pos is on left or right half of list
        assert type(pos)==int,'Error:pos is not an integer'
        assert pos>=0,'Error:pos must be positive'
        current=self.head
        new_node= DLinkedListNode(item,None,None)    
        if pos==0:
            self.add(item)
        elif pos==self.size:
            self.append(item)
        elif pos>self.size:
            raise Exception('Position attempted to enter is larger than the size of linked list.')
        else:
            current_pos=0
            while(current.next!=None):
                if (pos)==current_pos:
                    # attach new node from both sides set prev and nex of new node and attach that using right and left to rest of list
                    right=current
                    left=current.getPrevious()
                    right.setPrevious(new_node)
                    left.setNext(new_node)
                    new_node.setPrevious(left)
                    new_node.setNext(right)
                    return 0
                current=current.next
                current_pos+=1
            self.size+=1

        
    def pop1(self):
        # change tail to previous of old tail and return old tails data
        oldtail=self.tail
        newtail=oldtail.getPrevious()
        oldtail.setNext(None)
        
        self.tail=newtail
        self.size -=1
        
        return oldtail.data
    
    def pop(self, pos=None):
        if pos!=None:
            assert pos<=self.size,'Pos must be within list'
            assert type(pos)==int,'Pos must be an int'
            assert pos>=0,'Pos must not be negative'
        current=self.head
        current_pos=0
        if pos==(self.getSize()-1) or pos==None:
            data_from_method=self.pop1()
            return data_from_method
        else:
            
            while current.next!=None:
                if pos==current_pos:
                    data=current.data
                    left=current.getPrevious()
                    right=current.next
                    left.setNext(right)
                    right.setPrevious(left)
                    return data
                current_pos+=1
                current=current.next
 
        
    def searchLarger(self, item):
        current=self.head
        current_pos=0
        while current.next!=None:
            if item<current.data:
                return current_pos
            current=current.next
            current_pos+=1
        return -1
            
        
    def getSize(self):
         return self.size
    
    def getItem(self, pos):
        assert type(pos)==int,'position must be type int'
        assert abs(pos)<=self.size,'Position is outside of the list'
        # if pos is =0 or greater than then we traverse from head
        if pos>=0:
            current=self.head
            current_pos=0
            while current!=None:
                if current_pos==pos:
                    return current.data
                current_pos+=1
                current=current.next
        # if pos is negative traverse from tail
        elif pos<0:
            current_pos=0
            current=self.tail
            while current!=None:
                if current_pos==pos+1:
                    return current.data
                current_pos-=1
                current=current.getPrevious()
   
               
    def __str__(self):
        # returns a string representation of the list
        current = self.head
        string = ''
        
        while current != None:
            if current.next==None:
                string = string + str(current.data)+''
            else:
                string=string+str(current.data)+' '
            
            current = current.next
        return string






# In[ ]:




