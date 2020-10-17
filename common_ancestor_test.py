
import unittest
import common_ancestor
import math

class TestCommonAncestor(unittest.TestCase):

    def test_Node(self):

        """ Test creating node with None parameter """
        node = common_ancestor.node(None)
        self.assertIsNotNone(node)
        self.assertIsNone(node.value)


        """ Test trying to add a child to node with no key value """
        self.assertFalse(node.addChild(1))
        self.assertFalse(node.addChild(2))


        """ Test passing String parameter"""
        node = common_ancestor.node("a")
        self.assertIsNotNone(node)
        self.assertIsNone(node.value)


        """ Test passing List parameter """
        node = common_ancestor.node([1,2,3,4])
        self.assertIsNotNone(node)
        self.assertIsNone(node.value)


        """ Test creating node with Float parameter """
        node = common_ancestor.node(1.7)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, math.floor(1.7))


        """ Test creating node with Negative Integer parameter """
        node = common_ancestor.node(-1)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, -1)


        """ Test creating node with String representation of Integer """
        node = common_ancestor.node('1')
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 1)


        """ Test adding duplicate key to node key """
        node = common_ancestor.node(1)
        self.assertFalse(node.addChild(1))
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)


        """ Test creating node with no children """
        node = common_ancestor.node(2)
        self.assertIsNotNone(node.value)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)


        """ Test adding a left child to node """
        self.assertTrue(node.addChild(1))
        self.assertIsNotNone(node.left)
        self.assertIsNotNone(node.left.value)


        """ Test adding a right child to node """
        self.assertTrue(node.addChild(3))
        self.assertIsNotNone(node.right)
        self.assertIsNotNone(node.right.value)


        """ Test duplicate of left child is not added """
        self.assertFalse(node.addChild(1))
        self.assertIsNone(node.left.left)
        self.assertIsNone(node.left.right)


        """ Test duplicate of right child is not added """
        self.assertFalse(node.addChild(3))
        self.assertIsNone(node.right.right)
        self.assertIsNone(node.right.left)



    def test_BT(self):

        """ Test constructor for Binary Tree"""
        bt = common_ancestor.BT()
        self.assertIsNotNone(bt)
        self.assertIsNone(bt.getRoot())

        # ------------------------- addHead() -----------------------------

        """ Test adding head to empty BT """
        self.assertTrue(bt.addHead(1))
        self.assertIsNotNone(bt.getRoot())


        """ Test adding head to BT which already has head """
        self.assertFalse(bt.addHead(2))
        self.assertIsNotNone(bt.getRoot())


        """ Test passing String as parameter for head of BT """
        bt = common_ancestor.BT()
        self.assertFalse(bt.addHead("a"))
        self.assertIsNone(bt.getRoot())


        """ Test passing List as parameter for head of BT """
        bt = common_ancestor.BT()
        self.assertFalse(bt.addHead([1,2,3]))
        self.assertIsNone(bt.getRoot())


        """ Test passing Float as parameter for head of BT """
        bt = common_ancestor.BT()
        self.assertTrue(bt.addHead(1.2))
        self.assertEqual(bt.getRoot().value, 1)


        """ Test passing Negative Integer as parameter for head of BT """
        bt = common_ancestor.BT()
        self.assertTrue(bt.addHead(-1))
        self.assertIsNotNone(bt.getRoot())


        # ------------------------- getRoot() -----------------------------

        """ Test getting root of empty BT"""
        bt = common_ancestor.BT()
        self.assertIsNone(bt.getRoot())


        """ Test getting root of non empty BT """
        bt.addHead(2)
        self.assertEqual(bt.getRoot().value, 2)


        # ------------------------- addValue() -----------------------------

        """ Test adding to empty BT """
        bt = common_ancestor.BT()
        self.assertTrue(bt.addValue(2))
        self.assertEqual(bt.getRoot().value, 2)


        """ Test adding to left sub tree """
        self.assertTrue(bt.addValue(1))
        self.assertEqual(bt.getRoot().left.value, 1)


        """ Test adding to right sub tree """
        self.assertTrue(bt.addValue(3))
        self.assertEqual(bt.getRoot().right.value, 3)


        """ Test failing to add duplicate key to BT """
        self.assertFalse(bt.addValue(2))
        self.assertFalse(bt.addValue(3))


        """ Test passing String parameter"""
        self.assertFalse(bt.addValue("bad"))


        """ Test passing List parameter """
        self.assertFalse(bt.addValue([2,3,4,5]))


        """ Test passing Negative Integer parameter """
        self.assertTrue(bt.addValue(-1))


        """ Test passing Float parameter """
        self.assertTrue(bt.addValue(7.8))



    def test_findPath(self):
        bt = common_ancestor.BT()
        bt.addValue(2)
        bt.addValue(1)
        bt.addValue(3)

        # ------------------- Testing passing parameters -----------------------

        """ Test find path with None root """
        self.assertFalse(common_ancestor.findPath(None, 1, []))


        """ Test find path with None node_value """
        self.assertFalse(common_ancestor.findPath(bt.getRoot(), None, []))


        """ Test find path with None path_arr"""
        self.assertFalse(common_ancestor.findPath(bt.getRoot(), 2, None))


        """ Test find path passing String as root object parameter """
        self.assertFalse(common_ancestor.findPath("abc", 2, []))


        """ Test find path passing String as node_value parameter """
        self.assertFalse(common_ancestor.findPath(bt.getRoot(), "2", []))
        self.assertFalse(common_ancestor.findPath(bt.getRoot(), "abc", []))


        """ Test find path passing String as path_arr parameter """
        self.assertFalse(common_ancestor.findPath(bt.getRoot(), 2, ""))


        """ Test find path passing Integer as root object parameter """
        self.assertFalse(common_ancestor.findPath(1, 2, []))


        """ Test find path passing Boolean as root object parameter """
        self.assertFalse(common_ancestor.findPath(True, 2, []))
        self.assertFalse(common_ancestor.findPath(False, 2, []))


        """ Test find path passing List as root object parameter """
        self.assertFalse(common_ancestor.findPath([1,2,3], 2, []))
        self.assertFalse(common_ancestor.findPath(['b', 'c', 'd'], 2, []))


        """ Test find path passing List object as node_value parameter """
        self.assertFalse(common_ancestor.findPath(bt.getRoot(), [1,2,3], []))


        """ Test find path passing String as path_arr parameter"""
        self.assertFalse(common_ancestor.findPath(bt.getRoot(), 1, "abc"))


        # ---------------------- Test Logic of Function ------------------------

        bt = common_ancestor.BT()

        """ Test find path with empty BT """
        self.assertFalse(common_ancestor.findPath(bt.getRoot(), 2, []))


        """ Test find path in BT with 1 element """
        bt.addValue(10)
        arr = []
        self.assertTrue(common_ancestor.findPath(bt.getRoot(), 10, arr))
        self.assertEqual(arr, [10])


        """ Test find path going into left sub tree """
        bt.addValue(5)
        arr = []
        self.assertTrue(common_ancestor.findPath(bt.getRoot(), 5, arr))
        self.assertEqual(arr, [10,5])


        bt.addValue(3)
        bt.addValue(7)

        arr = []
        self.assertTrue(common_ancestor.findPath(bt.getRoot(), 3, arr))
        self.assertEqual(arr, [10,5,3])



        """ Test find path going into right sub tree """
        bt.addValue(13)
        arr = []
        self.assertTrue(common_ancestor.findPath(bt.getRoot(), 13, arr))
        self.assertEqual(arr, [10,13])

        bt.addValue(16)
        arr = []
        self.assertTrue(common_ancestor.findPath(bt.getRoot(), 16, arr))
        self.assertEqual(arr, [10,13, 16])


        """ Test find path in BT which doesnt contain specified node_value """
        arr = []
        self.assertFalse(common_ancestor.findPath(bt.getRoot(), 100, arr))
        self.assertEqual(arr, [10,13,16])

        arr = []
        self.assertFalse(common_ancestor.findPath(bt.getRoot(), 0, arr))
        self.assertEqual(arr, [10,5,3])




    def test_findLCA(self):

        """ Test on Empty BT """
        bt = common_ancestor.BT()
        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), 1, 2), -1)


        """ Test on BT with 1 element """
        bt.addValue(2)
        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), 1, 2), -1)
        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), 2, 2), 2)


        """ Test on BT with 2 elements """
        bt.addValue(1)
        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), 1, 2), 2)


        """ Test on Bt with more than 2 elements """
        bt = common_ancestor.BT()
        arr = [8,1,9,10,4,5,3,7,2,6]
        for x in arr:
            bt.addValue(x)

        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), 1, 9), 8)
        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), 4, 10), 8)
        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), 4, 1), 1)
        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), 3, 5), 4)
        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), 2, 5), 4)
        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), 10, 6), 8)

        # Testing if root shows up twice
        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), bt.getRoot().value, bt.getRoot().value), bt.getRoot().value)


        """ Test on BT with only left sub tree """
        bt = common_ancestor.BT()
        for i in reversed(range(10)):
            bt.addValue(i)

        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), 9, 1), 9)
        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), 1, 9), 9)
        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), 7, 5), 7)
        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), 0, 0), 0)


        """ Test on BT with only right sub tree """
        bt = common_ancestor.BT()
        for i in range(10):
            bt.addValue(i)

        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), 1, 2), 1)
        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), 1, 9), 1)
        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), 9, 9), 9)


        """ Test for None inputs """
        bt = common_ancestor.BT()
        bt.addValue(2)
        bt.addValue(3)
        bt.addValue(1)
        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), None, None), -1)
        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), None, 2), -1)
        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), 2, None), -1)


        """ Test for string inputs """
        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), "a", "b"), -1)
        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), "a", 2), -1)
        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), 3, "b"), -1)


        """ Test for float inputs """
        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), 2.1, 3.2), -1)
        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), 3.9, 3.2), -1)


        """ Test for list inputs """
        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), [1,2], 3), -1)
        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), [1,2], [2,1]), -1)
        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), 2, [3]), -1)


        """ Test for negative integer inputs as key values
              -3
             /   \
           -5     -1
           / \      \
         -6  -4      2

        """
        bt = common_ancestor.BT()
        bt.addValue(-3)
        bt.addValue(-5)
        bt.addValue(-1)
        bt.addValue(-6)
        bt.addValue(-4)
        bt.addValue(2)

        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), -3, -1), -3)
        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), -6, -4), -5)
        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), -5, -3), -3)
        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), -6, 2), -3)
        self.assertEqual(common_ancestor.findLCA(bt.getRoot(), -1, 2), -1)
