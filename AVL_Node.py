import unittest
NB_ROT = 0
def reset_nb_rot():
    global NB_ROT
    NB_ROT = 0

class AVL_Node:

    # Initialisation de la Node AVL
    def __init__(self, value: int) -> None:
        self._value = value
        self._left = None
        self._right = None
        self._balance = 0

    def insert(self, value: int):
        return self.insert_wrapper(value)[0]

    def insert_wrapper(self, value): #Value is the value of balance
        if self._value < value:
            if self._right == None:
                # Insert in right with a node 
                self._right = AVL_Node(value)
                self._right._balance = 0
                self._balance = self._balance - 1
                return (self, int(self._left is None)) 
                # if there is a node return 0 
                # else return 1 (there is nothing) 
            else:
                node_right, b = self._right.insert_wrapper(value)
                self._balance = self._balance - b
                if (self._balance == -2):
                    # print("Appelle rotation left")
                    return self.rotation_left(node_right), 0

        elif self._value > value:   
            if self._left == None:
                self._left = AVL_Node(value)
                self._left._balance = 0
                self._balance = self._balance + 1
                return (self, int(self._right is None))
            else:
                node_left, b = self._left.insert_wrapper(value)
                self._balance = self._balance + b
                if (self._balance == 2):
                    # print("Appelle rotation right")
                    return self.rotation_right(node_left), 0
        return self, 0

    def rotation_left(self, node_right):
        global NB_ROT

        if node_right._balance > 0: # désequilibre à droite
            node_right._right = node_right._left
            node_right._left = None
        node_right._left = self
        self._right = None
        node_right._balance = 0
        self._balance = 0
        if node_right._value > node_right._right._value:
            remplace = node_right._value
            node_right._value = node_right._right._value
            node_right._right._value = remplace
            NB_ROT = NB_ROT + 1
        NB_ROT = NB_ROT + 1
        return node_right

    def rotation_right(self, node_left):
        global NB_ROT

        if node_left._balance < 0: # désequilibre à droite
            node_left._left = node_left._right
            node_left._right = None

        var_self = self
        self = node_left
        self._right = var_self
        self._left = node_left._left

        self._left._balance = 0
        self._right._balance = 0
        self._balance = 0

        if node_left._value < node_left._left._value:
            remplace = node_left._value
            node_left._value = node_left._left._value
            node_left._left._value = remplace
            NB_ROT = NB_ROT + 1
        NB_ROT = NB_ROT + 1
        return(node_left)

# ------------------------------------------------------------------------------

    def rot_left(self):
        assert (self._right is not None)
        node_right = self._right # 69
        node_left = self._right._left # 53
        self._right = node_left
        node_right._left = self
        global NB_ROT
        NB_ROT = NB_ROT + 1
        return node_right

    def rot_right(self):
        assert (self._right is not None)
        node_left = self._left # 20
        node_right = self._left._right # 30
        self._left = node_right
        node_left._right = self
        global NB_ROT
        NB_ROT = NB_ROT + 1
        return node_left

    def delete(self, value):
        if (self._value == value):
            if self._left is None and self._right is None:
                self = None
                return
            elif self._left is not None and self._right is not None:
                save_node = self
                self = self._right
                self._left = save_node._left
                return
            elif self._left is None and self._right is not None:
                self = self._right
                return
            elif self._left is not None and self._right is None:
                self = self._left
                return
        elif self._value < value:
            self._right.delete(value)
            return
        elif self._value > value:
            self._left.delete(value)
            return




