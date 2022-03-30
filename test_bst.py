import unittest
import AVL_Node as ficAvlNode
from AVL_Node import AVL_Node


class TestBST(unittest.TestCase):

    def test_init(self):
        bst: AVL_Node = AVL_Node(42)
        self.assertEqual(bst._value, 42)

    def test_insert_without_bl(self):

        bst: AVL_Node = AVL_Node(42)
        self.assertEqual(42, bst._value)
        bst = bst.insert(69)
        self.assertEqual(69, bst._right._value)
        bst = bst.insert(20)
        self.assertEqual(20, bst._left._value)
        bst = bst.insert(53)
        self.assertEqual(53, bst._right._left._value)
        bst = bst.insert(80)
        self.assertEqual(80, bst._right._right._value)
        bst = bst.insert(30)
        self.assertEqual(30, bst._left._right._value)
        bst = bst.insert(10)
        self.assertEqual(10, bst._left._left._value)
        bst = bst.insert(1)
        self.assertEqual(1, bst._left._left._left._value)
        bst = bst.insert(800)
        self.assertEqual(800, bst._right._right._right._value)

    def test_insert(self):

        bst: AVL_Node = AVL_Node(42)
        self.assertEqual(42, bst._value)
        bst = bst.insert(69)
        self.assertEqual(69, bst._right._value)
        bst = bst.insert(20)
        self.assertEqual(20, bst._left._value)
        bst = bst.insert(53)
        self.assertEqual(53, bst._right._left._value)
        bst = bst.insert(80)
        self.assertEqual(80, bst._right._right._value)
        bst = bst.insert(30)
        self.assertEqual(30, bst._left._right._value)
        bst = bst.insert(10)
        self.assertEqual(10, bst._left._left._value)
        bst = bst.insert(1)
        self.assertEqual(1, bst._left._left._left._value)
        bst = bst.insert(800)
        self.assertEqual(800, bst._right._right._right._value)

        self.assertEqual(0,  bst._balance)
        self.assertEqual(1,  bst._left._balance)
        self.assertEqual(1,  bst._left._left._balance)
        self.assertEqual(0,  bst._left._left._left._balance)
        self.assertEqual(-1, bst._right._balance)
        self.assertEqual(-1, bst._right._right._balance)
        self.assertEqual(0,  bst._right._right._right._balance)

    # def test_turn_left(self):
    #     ficAvlNode.reset_nb_rot()
    #     rot = 1

    #     bst: AVL_Node = AVL_Node(42)
    #     bst = bst.insert(69)
    #     bst = bst.insert(20)
    #     bst = bst.insert(53)
    #     bst = bst.insert(80)
    #     bst = bst.insert(30)
    #     bst = bst.insert(10)
    #     bst = bst.insert(1)
    #     bst = bst.insert(800)

    #     bst = bst.turn_left()

    #     self.assertEqual(69,  bst._value)
    #     self.assertEqual(80,  bst._right._value)
    #     self.assertEqual(800, bst._right._right._value)
    #     self.assertEqual(42,  bst._left._value)
    #     self.assertEqual(53,  bst._left._right._value)
    #     self.assertEqual(20,  bst._left._left._value)
    #     self.assertEqual(30,  bst._left._left._right._value)
    #     self.assertEqual(10,  bst._left._left._left._value)
    #     self.assertEqual(1,   bst._left._left._left._left._value)

    #     print("test_turn_left", "OK" if ficAvlNode.NB_ROT == rot else "KO")
    #     print("Votre code a effectué :", ficAvlNode.NB_ROT, "rotations")
    #     print("L'auteur de la test suite a fait", rot, "rotations\n\n")

    # def test_turn_right(self):
    #     ficAvlNode.reset_nb_rot()
    #     rot = 1

    #     bst: AVL_Node = AVL_Node(42)
    #     bst = bst.insert(69)
    #     bst = bst.insert(20)
    #     bst = bst.insert(53)
    #     bst = bst.insert(80)
    #     bst = bst.insert(30)
    #     bst = bst.insert(10)
    #     bst = bst.insert(1)
    #     bst = bst.insert(800)

    #     bst = bst.turn_right()

    #     self.assertEqual(20,  bst._value)
    #     self.assertEqual(10,  bst._left._value)
    #     self.assertEqual(1,   bst._left._left._value)
    #     self.assertEqual(42,  bst._right._value)
    #     self.assertEqual(30,  bst._right._left._value)
    #     self.assertEqual(69,  bst._right._right._value)
    #     self.assertEqual(53,  bst._right._right._left._value)
    #     self.assertEqual(80,  bst._right._right._right._value)
    #     self.assertEqual(800, bst._right._right._right._right._value)

    #     print("test_turn_right", "OK" if ficAvlNode.NB_ROT == rot else "KO")
    #     print("Votre code a effectué :", ficAvlNode.NB_ROT, "rotations")
    #     print("L'auteur de la test suite a fait", rot, "rotations\n\n")

    # def test_balance_without_upt_1(self):
    #     bst: AVL_Node = AVL_Node(6)
    #     bst = bst.insert(4)
    #     bst = bst.insert(5)

    #     self.assertEqual(5, bst._value)
    #     self.assertEqual(6, bst._right._value)
    #     self.assertEqual(4, bst._left._value)

    # def test_balance_without_upt_2(self):
    #     bst: AVL_Node = AVL_Node(6)
    #     bst = bst.insert(4)
    #     bst = bst.insert(2)

    #     self.assertEqual(4, bst._value)
    #     self.assertEqual(6, bst._right._value)
    #     self.assertEqual(2, bst._left._value)

    # def test_balance_without_upt_3(self):
    #     bst: AVL_Node = AVL_Node(2)
    #     bst = bst.insert(4)
    #     bst = bst.insert(6)

    #     self.assertEqual(4, bst._value)
    #     self.assertEqual(6, bst._right._value)
    #     self.assertEqual(2, bst._left._value)

    # def test_balance_without_upt_4(self):
    #     bst: AVL_Node = AVL_Node(5)
    #     bst = bst.insert(7)
    #     bst = bst.insert(6)

    #     self.assertEqual(6, bst._value)
    #     self.assertEqual(7, bst._right._value)
    #     self.assertEqual(5, bst._left._value)

    # def test_balance_1(self):
    #     ficAvlNode.reset_nb_rot()
    #     rot = 2

    #     bst: AVL_Node = AVL_Node(6)
    #     bst = bst.insert(4)
    #     bst = bst.insert(5)

    #     self.assertEqual(5, bst._value)
    #     self.assertEqual(6, bst._right._value)
    #     self.assertEqual(4, bst._left._value)

    #     self.assertEqual(0, bst._balance)
    #     self.assertEqual(0, bst._right._balance)
    #     self.assertEqual(0, bst._left._balance)

    #     print("test_balance_1", "OK" if ficAvlNode.NB_ROT == rot else "KO")
    #     print("Votre code a effectué :", ficAvlNode.NB_ROT, "rotations")
    #     print("L'auteur de la test suite a fait", rot, "rotations\n\n")

    # def test_balance_2(self):
    #     ficAvlNode.reset_nb_rot()
    #     rot = 1

    #     bst: AVL_Node = AVL_Node(6)
    #     bst = bst.insert(4)
    #     bst = bst.insert(2)

    #     self.assertEqual(4, bst._value)
    #     self.assertEqual(6, bst._right._value)
    #     self.assertEqual(2, bst._left._value)

    #     self.assertEqual(0, bst._balance)
    #     self.assertEqual(0, bst._right._balance)
    #     self.assertEqual(0, bst._left._balance)

    #     print("test_balance_2", "OK" if ficAvlNode.NB_ROT == rot else "KO")
    #     print("Votre code a effectué :", ficAvlNode.NB_ROT, "rotations")
    #     print("L'auteur de la test suite a fait", rot, "rotations\n\n")

    # def test_balance_3(self):
    #     ficAvlNode.reset_nb_rot()
    #     rot = 1

    #     bst: AVL_Node = AVL_Node(2)
    #     bst = bst.insert(4)
    #     bst = bst.insert(6)

    #     self.assertEqual(4, bst._value)
    #     self.assertEqual(6, bst._right._value)
    #     self.assertEqual(2, bst._left._value)

    #     self.assertEqual(0, bst._balance)
    #     self.assertEqual(0, bst._right._balance)
    #     self.assertEqual(0, bst._left._balance)

    #     print("test_balance_3", "OK" if ficAvlNode.NB_ROT == rot else "KO")
    #     print("Votre code a effectué :", ficAvlNode.NB_ROT, "rotations")
    #     print("L'auteur de la test suite a fait", rot, "rotations\n\n")

    # def test_balance_4(self):
    #     ficAvlNode.reset_nb_rot()
    #     rot = 2

    #     bst: AVL_Node = AVL_Node(5)
    #     bst = bst.insert(7)
    #     bst = bst.insert(6)

    #     self.assertEqual(6, bst._value)
    #     self.assertEqual(7, bst._right._value)
    #     self.assertEqual(5, bst._left._value)

    #     self.assertEqual(0, bst._balance)
    #     self.assertEqual(0, bst._right._balance)
    #     self.assertEqual(0, bst._left._balance)

    #     print("test_balance_4", "OK" if ficAvlNode.NB_ROT == rot else "KO")
    #     print("Votre code a effectué :", ficAvlNode.NB_ROT, "rotations")
    #     print("L'auteur de la test suite a fait", rot, "rotations\n\n")

    # def test_hard_1(self):
    #     ficAvlNode.reset_nb_rot()
    #     rot = 6

    #     bst: AVL_Node = AVL_Node(42)
    #     bst = bst.insert(69)
    #     bst = bst.insert(53)
    #     bst = bst.insert(80)
    #     bst = bst.insert(20)
    #     bst = bst.insert(30)
    #     bst = bst.insert(10)
    #     bst = bst.insert(1)
    #     bst = bst.insert(800)

    #     self.assertEqual(53,  bst._value)
    #     self.assertEqual(30,  bst._left._value)
    #     self.assertEqual(10,  bst._left._left._value)
    #     self.assertEqual(42,  bst._left._right._value)
    #     self.assertEqual(1,   bst._left._left._left._value)
    #     self.assertEqual(20,  bst._left._left._right._value)
    #     self.assertEqual(80,  bst._right._value)
    #     self.assertEqual(69,  bst._right._left._value)
    #     self.assertEqual(800, bst._right._right._value)

    #     self.assertEqual(1, bst._balance)
    #     self.assertEqual(1, bst._left._balance)
    #     self.assertEqual(0, bst._left._left._balance)
    #     self.assertEqual(0, bst._left._right._balance)
    #     self.assertEqual(0, bst._left._left._left._balance)
    #     self.assertEqual(0, bst._left._left._right._balance)
    #     self.assertEqual(0, bst._right._balance)
    #     self.assertEqual(0, bst._right._left._balance)
    #     self.assertEqual(0, bst._right._right._balance)

    #     print("test_hard_1", "OK" if ficAvlNode.NB_ROT == rot else "KO")
    #     print("Votre code a effectué :", ficAvlNode.NB_ROT, "rotations")
    #     print("L'auteur de la test suite a fait", rot, "rotations\n\n")


if __name__ == '__main__':
    unittest.main()

