from readline import insert_text


class AVL_Node:
    NB_ROT = 0
    def reset_nb_rot():
        global NB_ROT
        NB_ROT = 0

    def __init__(self, value: int) -> None:
        self._value = value
        self._left = None
        self._right = None
        self._balance = 0

    def insert(self, value: int):
        return self.insert_wrapper(value)[0]

    def insert_wrapper(self, value):
        if self._value < value: # right
            if self._right == None:
                self._right = AVL_Node(value)
                self._right._balance = 0
                self._balance = self._balance - 1
                return (self, int(self._left is None))
            else:
                node_right, b = self._right.insert_wrapper(value)
                self._balance = self._balance - b
                if (self._balance == -2):
                    if node_right._balance > 0: # désequilibre à droite
                        node_right._right = node_right._left
                        node_right._left = None
                    node_right._left = self
                    self._right = None
                    node_right._balance = 0
                    self._balance = 0
                    return (node_right, 0)

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
                    if node_left._balance < 0: # désequilibre à droite
                        node_left._left = node_left._right
                        node_left._right = None
                    node_left._right = self
                    self._left = None
                    node_left._balance = 0
                    self._balance = 0
                    return(node_left, 0)
        return self, 0
