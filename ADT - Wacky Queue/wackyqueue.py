"""
# Copyright Nick Cheng, 2018
# Copyright Justin Lyn, 2018
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSCA48, Winter 2018
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""

from wackynode import WackyNode

# Do not add import statements or change the one above.
# Write your WackyQueue class code below.


# Class to represent a WackyQueue
class WackyQueue():

    # Create a wackyqueue
    def __init__(self):
        '''(WackyQueue) -> NoneType
        Method to create an empty wackyqueue
        '''
        # Representation invariant:
        # ._oddhead is a pointer to the odd positioned nodes in the list
        # points to nodes 1, 3, 5, 7...... and so on
        # ._oddhead will have a fixed priority of 1 to meet requirments
        # ._evenhead is a pointer to the even positioned nodes in the list
        # points to nodes 2, 4 6, 8...... and so on
        # ._evenhead will have a fixed priority of 1 to meet requirments
        self._oddhead = WackyNode(None, 1)
        self._evenhead = WackyNode(None, 1)

    def insert(self, obj, pri):
        '''(WackyQueue, obj, int) -> NoneType
        This method is designed to insert a given object with a certain
        priority into the wackyqueue. Duplicate items with duplicate priorities
        are allowed. Larger positive numbers have a higher priority, smaller
        more negative numbers have lower priority, and if the node being
        inserted has the same priority as an existing node the node already
        existing will have the higher priority. Method won't return anything.
        '''
        # Create the new node
        new_node = WackyNode(obj, pri)
        # Use an if statement to see if this is the first node being inserted
        if (self.isempty()):
            self._oddhead.set_next(new_node)
        # Check if its the second node
        elif ((self._oddhead.get_next() is not None) and
              (self._evenhead.get_next() is None)):
            # Case where the second node has the second highest priority
            if (self._oddhead.get_next().get_priority() > pri):
                self._evenhead.set_next(new_node)
            # Else when second node has the new highest priority
            else:
                self._evenhead.set_next(self._oddhead.get_next())
                self._oddhead.set_next(new_node)
        # Any other inserted node past the second one
        else:
            # Get the last nodes in each respected list
            # Get last node in the even list
            even_curr = self._evenhead.get_next()
            while (even_curr.get_next() is not None):
                even_curr = even_curr.get_next()
            # Get the last node in the odd list
            odd_curr = self._oddhead.get_next()
            while (odd_curr.get_next() is not None):
                odd_curr = odd_curr.get_next()
            # Check if the new node will go to the front of the list
            if (pri > self._oddhead.get_next().get_priority()):
                # Get the following node
                following = self._oddhead.get_next()
                # Get the even nodes
                even_nodes = self._evenhead.get_next()
                # Insert the new highest node
                self._oddhead.set_next(new_node)
                # Swap the odd and even nodes and re link them
                odd_to_even = following
                even_to_odd = even_nodes
                self._oddhead.get_next().set_next(even_to_odd)
                self._evenhead.set_next(odd_to_even)
            # Case when the inserted node will be somewhere in the middle
            elif ((pri <= self._oddhead.get_next().get_priority()) and
                  ((pri >= even_curr.get_priority()) or
                   (pri >= odd_curr.get_priority()))):
                # Run a loop to go through the lists and find the correct spot
                cur_odd = self._oddhead.get_next()
                cur_even = self._evenhead.get_next()
                prev_odd = self._oddhead
                prev_even = self._evenhead
                found = False
                while ((cur_even or cur_odd is not None) and (not found)):
                    # Case when the node will fall between (Odd-Even)
                    if ((pri < cur_odd.get_priority()) and
                            (pri > cur_even.get_priority())):
                        # Get the nodes which will be swapped
                        odd_to_even = cur_odd.get_next()
                        even_to_odd = cur_even
                        # Insert the node and re link everything accordingly
                        prev_even.set_next(new_node)
                        prev_even.get_next().set_next(odd_to_even)
                        cur_odd.set_next(even_to_odd)
                        # Stop the loop
                        found = True
                    # Case when the node will fall between (Even-Odd)
                    elif ((pri > cur_odd.get_priority()) and
                          (pri < prev_even.get_priority())):
                        # Get the nodes that will be swapped
                        even_to_odd = cur_even
                        odd_to_even = cur_odd
                        # Insert the node and re link everything accordingly
                        prev_odd.set_next(new_node)
                        prev_odd.get_next().set_next(even_to_odd)
                        prev_even.set_next(odd_to_even)
                        # Stop the loop
                        found = True
                    # Case when inserting priority and there are already
                    # 2+ off the same priority
                    elif ((cur_even and cur_odd is not None) and
                          (pri == cur_odd.get_priority()) and
                          (pri == cur_even.get_priority())):
                        # Get the nodes that will be swapped
                        even_to_odd = cur_even.get_next()
                        odd_to_even = cur_odd.get_next()
                        # Insert the node and re link everything accordingly
                        cur_odd.set_next(new_node)
                        cur_odd.get_next().set_next(even_to_odd)
                        cur_even.set_next(odd_to_even)
                        # Stop the loop
                        found = True
                    # Case when the same priority is found in the odd list
                    elif (pri == cur_odd.get_priority()):
                        # Get the nodes that will be swapped
                        even_to_odd = cur_even
                        odd_to_even = cur_odd.get_next()
                        # Insert the node and relink everything accordingly
                        prev_even.set_next(new_node)
                        prev_even.get_next().set_next(odd_to_even)
                        cur_odd.set_next(even_to_odd)
                        # Stop the loop
                        found = True
                    # Case when the same priority is found in even list
                    elif (pri == cur_even.get_priority()):
                        # Get the nodes that will be swapped
                        even_to_odd = cur_even.get_next()
                        odd_to_even = cur_odd.get_next()
                        # Insert the node and re link everything accordingly
                        cur_odd.set_next(new_node)
                        cur_odd.get_next().set_next(even_to_odd)
                        cur_even.set_next(odd_to_even)
                        # Stop the loop
                        found = True
                    # Only increment if havent found the spot to prevent
                    # getting NoneType errors
                    if (found is not True):
                        # Move to the next nodes and set the previous ones
                        prev_odd = cur_odd
                        prev_even = cur_even
                        cur_odd = cur_odd.get_next()
                        cur_even = cur_even.get_next()
            # When the node will be inserted at the end of the list
            else:
                # The case when the new node will be inserted at the end of odd
                if (pri < even_curr.get_priority() and
                        even_curr.get_priority() < odd_curr.get_priority()):
                    odd_curr.set_next(new_node)
                # Being inserted at the end of the even list
                else:
                    even_curr.set_next(new_node)

    def extracthigh(self):
        '''(WackyQueue) -> obj
        This method is designed to remove and return the object at the front
        of the queue. Returns an object.
        REQ: The queue must have AT LEAST one node/object in it (Not empty)
        '''
        # Get the first node that is following the odd lists head
        node = self._oddhead.get_next()
        # Get the node that points to the remaining nodes
        following_nodes = node.get_next()
        # Get the node that points to the even heads
        even_nodes = self._evenhead.get_next()
        # Swap the nodes (even goes to odd) and (odd to even)
        odd_to_even = following_nodes
        even_to_odd = even_nodes
        # Re link the nodes
        self._oddhead.set_next(even_to_odd)
        self._evenhead.set_next(odd_to_even)
        # Return the object with the highest priority
        return (node.get_item())

    def isempty(self):
        '''(WackyQueue) -> bool
        This method is designed to return whether or not the wackyqueue is
        empty. Returns boolean value.
        '''
        # If the odd head points to None then the list is empty
        return (self._oddhead.get_next() is None)

    def changepriority(self, obj, pri):
        '''(WackyQueue, obj, int) -> NoneType
        This method is designed to change the desired objects priority to the
        desired one. If the object in the wackyqueue doesn't exist or already
        has that priority nothing will happen to the queue. Method won't
        return anything.
        '''
        # Run a loop until we find the desired node
        cur_odd = self._oddhead.get_next()
        cur_even = self._evenhead.get_next()
        prev_odd = self._oddhead
        prev_even = self._evenhead
        found = False
        while ((cur_even or cur_odd is not None) and not found):
            # Find the node with the desired obj and make sure it has a
            # different priority
            # Checking the odd list
            if ((cur_odd.get_item() == obj) and
                    (cur_odd.get_priority() != pri)):
                # Get the nodes which are going to be swapped
                even_to_odd = cur_even
                odd_to_even = cur_odd.get_next()
                # Re link the nodes accordingly
                prev_odd.set_next(even_to_odd)
                prev_even.set_next(odd_to_even)
                found = True
            # Checking the even list
            elif ((cur_even.get_item() == obj) and
                  (cur_even.get_priority() != pri)):
                # Get the nodes which are going to be swapped
                odd_to_even = cur_odd.get_next()
                even_to_odd = cur_even.get_next()
                # Re link the nodes accordingly
                cur_odd.set_next(even_to_odd)
                prev_even.set_next(odd_to_even)
                found = True
            # Get the next nodes only if we havent found the desired node
            if (found is not True):
                prev_odd = cur_odd
                prev_even = cur_even
                cur_odd = cur_odd.get_next()
                cur_even = cur_even.get_next()
        if (found is True):
            # Send the node and new priority to the insert method
            self.insert(obj, pri)

    def negateall(self):
        '''(WackyQueue) -> NoneType
        This method is designed to reverse the objects in the wacky queue.
        For the nodes that were inserted with the same priority they will also
        be reversed. Method won't return anything.
        '''
        # Make sure the list being negated is not empty
        if (self.isempty() is False):
            # Use a loop to go through the odd list and reset set next for all
            # node (The nodes next will now point to the prev node ie reversed)
            prev_node = None
            cur_node = self._oddhead.get_next()
            next_node = cur_node.get_next()
            odd_length = 1
            while (next_node is not None):
                # Set the current node to point to the previous
                cur_node.set_next(prev_node)
                # Negate the priority by multiplying by negative
                cur_node.set_priority(-(cur_node.get_priority()))
                # Set cur equal to next, get next and set prev to current
                prev_node = cur_node
                cur_node = next_node
                next_node = next_node.get_next()
                # Set current to point to prev
                cur_node.set_next(prev_node)
                # Increase the size
                odd_length += 1
            # Negate the priority by multiplying by negative
            cur_node.set_priority(-(cur_node.get_priority()))
            # Reset the new head
            self._oddhead.set_next(cur_node)
            # Use a loop to go through the even list and reset set next for all
            # node (The nodes next will now point to the prev node ie reversed)
            prev_node = None
            cur_node = self._evenhead.get_next()
            next_node = cur_node.get_next()
            even_length = 1
            while (next_node is not None):
                # Set the current node to point to the previous
                cur_node.set_next(prev_node)
                # Negate the priority by multiplying by negative
                cur_node.set_priority(-(cur_node.get_priority()))
                # Set cur equal to next, get next and set prev to current
                prev_node = cur_node
                cur_node = next_node
                next_node = next_node.get_next()
                # Set current to point to prev
                cur_node.set_next(prev_node)
                # Increase the size
                even_length += 1
            # Negate the priority by multiplying by negative
            cur_node.set_priority(-(cur_node.get_priority()))
            # Reset the new head
            self._evenhead.set_next(cur_node)
            # If statement to determine if relinked the head properly
            if ((self._evenhead.get_next().get_priority() >=
                self._oddhead.get_next().get_priority()) and
               (odd_length == even_length)):
                # Get the nodes after the head to be swapped
                odd_to_even = self._oddhead.get_next()
                even_to_odd = self._evenhead.get_next()
                # Re link the heads properly
                self._oddhead.set_next(even_to_odd)
                self._evenhead.set_next(odd_to_even)

    def getoddlist(self):
        '''(WackyQueue) -> WackyNode
        This method is designed to return a pointer to a linked list which will
        contain all the odd nodes. Method will return a wackynode.
        '''
        # Return the pointer to the odd list
        return (self._oddhead.get_next())

    def getevenlist(self):
        '''(WackyQueue) -> WackyNode
        This method is designed to return a pointer to a linked list which will
        contain all the even nodes. Method will return a wackynode.
        '''
        # Return the pointer to the even list
        return (self._evenhead.get_next())





    # Below code used for testing purposes



    def __str__(self):
        '''(PriorityQueue_2) -> str
        returns a string representing this PQ'''
        # Run a loop to place the new_node in accordance with its priority
        fcurr = self._oddhead.get_next()
        fnodes = ""
        scurr = self._evenhead.get_next()
        snodes = ""
        while (fcurr is not None):
            fnodes = fnodes + " " + str(fcurr)
            fcurr = fcurr.get_next()
        while (scurr is not None):
            snodes = snodes + " " + str(scurr)
            scurr = scurr.get_next()

        result = "\nOddList: " + fnodes + "  \nEvenList: " + snodes
        return result

w = WackyQueue()
print (w.isempty())
w.insert("A", 5)
w.insert("B", 4)
w.insert("C", 12)
w.insert("D", 4)
w.insert("E", 4)
w.insert("F", 1)
w.insert("G", 5)
w.insert("H", 1)
w.insert("I", 12)
w.insert("J", 6)
w.insert("K", 13)
w.insert("L", 7)
print(w.getevenlist())
print(w.getoddlist())
print (w.isempty())
print (w)
w.negateall()
print (w)
print (w.isempty())
print (w.getoddlist())
print (w.getevenlist())
w.changepriority("A", 5)
w.changepriority("B", 4)
w.changepriority("C", 12)
w.changepriority("D", 4)
w.changepriority("E", 4)
w.changepriority("F", 1)
w.changepriority("G", 5)
w.changepriority("H", 1)
w.changepriority("I", 12)
w.changepriority("J", 6)
w.changepriority("K", 13)
w.changepriority("L", 7)
print (w)
print(w.extracthigh())
print(w.extracthigh())
print(w.extracthigh())
print(w.extracthigh())
print(w.extracthigh())
print(w.extracthigh())
print(w.extracthigh())
print(w.extracthigh())
print(w)