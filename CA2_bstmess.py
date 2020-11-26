class BSTNode:
    """ An internal node for a Binary Search Tree.  """

    def __init__(self, item):
        """ Initialise a BSTNode on creation, with value==item. """
        self._element = item
        self._leftchild = None
        self._rightchild = None
        self._parent = None
        self.length = 0

    def __str__(self):
        """ Return a string representation of the tree rooted at this node.

        The string will be created by an in-order traversal.
        """
        outstr = ''
        if self._leftchild:
            outstr = outstr + str(self._leftchild)
        outstr = outstr + ' ' + str(self._element)
        if self._rightchild:
            outstr = outstr + str(self._rightchild)
        return outstr

    def _stats(self):
        """ Return the basic stats on the tree. """
        return ('size = ' + str(self.size())
                + '; height = ' + str(self.height()))

    def search(self, searchitem):
        """ Return object matching searchitem, or None.

        Args:
            searchitem: an object of any class stored in the BST

        """

    def search_node(self, searchitem):
        """ Return the BSTNode (with subtree) containing searchitem, or None.

        Args:
            searchitem: an object of any class stored in the BST
        """
        node = BSTNode(searchitem)
        if self._element is None:
            return None
        elif node._element < self._element:
            self._leftchild.search_node(searchitem)
        elif self._element < node._element:
            self._rightchild.search_node(searchitem)
        else:
            return self

    def add(self, obj):
        """ Add item to the tree, maintaining BST properties.

        Returns the item added, or None if a matching object was already there.
        """
        node = BSTNode(obj)
        if obj == self._element:
            return
        else:
            if obj < self._element:
                if self._leftchild is None:
                    node._parent = self
                    self._leftchild = node
                else:
                    self._leftchild.add(obj)
            elif self._element < obj:
                if self._rightchild is None:
                    node._parent = self
                    self._rightchild = node
                else:
                    self._rightchild.add(obj)

    def findmaxnode(self):
        """ Return the BSTNode with maximal element at or below here. """
        if self._element is None:
            return None

    def height(self):
        """ Return the height of this node.

        Note that with the recursive definition of the tree the height of the
        node is the same as the depth of the tree rooted at this node.
        """
        leftheight = -1
        if self._leftchild:
            leftheight = self._leftchild.height()
        rightheight = -1
        if self._rightchild:
            rightheight = self._rightchild.height()
        return 1 + max(leftheight, rightheight)

    def size(self):
        """ Return the size of this subtree.

        The size is the number of nodes (or elements) in the tree,
        including this node.
        """
        return self.length

    def leaf(self):
        """ Return True if this node has no children. """
        if self._leftchild._element is None and self._rightchild._element is None:
            return True
        return False

    def semileaf(self):
        """ Return True if this node has exactly one child. """
        if self._leftchild._element is None and self._rightchild._element is not None:
            return True
        elif self._leftchild._element is not None and self._rightchild._element is None:
            return True
        return False

    def full(self):
        """ Return true if this node has two children. """
        if self._leftchild._element is not None and self._rightchild._element is not None:
            return True
        return False

    def internal(self):
        """ Return True if this node has at least one child. """
        if self._leftchild._element is not None or self._rightchild._element is not None:
            return True
        return False

    def remove(self, searchitem):
        """ Remove and return the object matching searchitem, if there.

        Args:
            searchitem - an object of any class stored in the BST

        Remove the matching object from the tree rooted at this node.
        Maintains the BST properties.
        """
        # method body goes here

    def remove_node(self):
        """ Remove this BSTNode from its tree, and return its element.

        Maintains the BST properties.
        """
        # if self.full():

        # find the biggest item in the left tree
        #  - there must be a left tree, since this is a full node
        #  - the node for that item can have no right children
        # move that item up into this item
        # remove that old node, which is now a semileaf
        # return the original element
        # else if this has no children
        # find who the parent was
        # set the parent's appropriate child to None
        # wipe this node
        # return this node's element
        # else if this has no right child (but must have a left child)
        # shift leftchild up into its place, and clean up
        # return the original element
        # else this has no left child (but must have a right child)
        # shift rightchild up into its place, and clean up
        # return the original element

        # method body goes here

    def _print_structure(self):
        """ (Private) Print a structured representation of tree at this node. """
        if self._isthisapropertree() == False:
            print("ERROR: this is not a proper Binary Search Tree. ++++++++++")
        outstr = str(self._element) + ' (hgt=' + str(self.height()) + ')['
        if self._leftchild is not None:
            outstr = outstr + "left: " + str(self._leftchild._element)
        else:
            outstr = outstr + 'left: *'
        if self._rightchild is not None:
            outstr = outstr + "; right: " + str(self._rightchild._element) + ']'
        else:
            outstr = outstr + '; right: *]'
        if self._parent is not None:
            outstr = outstr + ' -- parent: ' + str(self._parent._element)
        else:
            outstr = outstr + ' -- parent: *'
        print(outstr)
        if self._leftchild is not None:
            self._leftchild._print_structure()
        if self._rightchild is not None:
            self._rightchild._print_structure()

    def _properBST(self):
        """ Return True if this is the root of a proper BST; False otherwise.

        First checks that this is a proper tree (i.e. parent and child
        references all link up properly.

        Then checks that it obeys the BST property.
        """
        if not self._isthisapropertree():
            return False
        return self._BSTproperties()[0]

    def _BSTproperties(self):
        """ Return a tuple describing state of this node as root of a BST.

        Returns:
            (boolean, minvalue, maxvalue):
                boolean is True if it is a BST, and false otherwise
                minvalue is the lowest value in this subtree
                maxvalue is the highest value in this subtree
        """
        minvalue = self._element
        maxvalue = self._element
        if self._leftchild is not None:
            leftstate = self._leftchild._BSTproperties()
            if not leftstate[0] or leftstate[2] > self._element:
                return (False, None, None)
            minvalue = leftstate[1]

        if self._rightchild is not None:
            rightstate = self._rightchild._BSTproperties()
            if not rightstate[0] or rightstate[1] < self._element:
                return (False, None, None)
            maxvalue = rightstate[2]

        return (True, minvalue, maxvalue)

    def _isthisapropertree(self):
        """ Return True if this node is a properly implemented tree. """
        ok = True
        if self._leftchild is not None:
            if self._leftchild._parent != self:
                ok = False
            if self._leftchild._isthisapropertree() == False:
                ok = False
        if self._rightchild is not None:
            if self._rightchild._parent != self:
                ok = False
            if self._rightchild._isthisapropertree() == False:
                ok = False
        if self._parent is not None:
            if (self._parent._leftchild != self
                    and self._parent._rightchild != self):
                ok = False
        return ok
