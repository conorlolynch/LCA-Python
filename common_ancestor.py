

class node:
    def __init__(self, value):
        try:
            self.value = int(value)
        except:
            self.value = None

        self.left = None
        self.right = None

    def addChild(self, value):
        bool = False
        if (self.value != None):
            if (value != None):
                try:
                    if (value < self.value):
                        if (self.left != None):
                            bool = self.left.addChild(value)
                        else:
                            new_node = node(value)
                            self.left = new_node
                            return True

                    elif (value > self.value):
                        if (self.right != None):
                            bool = self.right.addChild(value)
                        else:
                            new_node = node(value)
                            self.right = new_node
                            return True

                    else:
                        # We dont add duplicates
                        return False
                except:
                    pass

        return bool


class BT:
    def __init__(self):
        self.number_items = 0
        self.root = None
        self.height = 0


    def addHead(self, value):
        if (self.root == None):
            try:
                value = int(value)
                self.root = node(value)
                self.number_items += 1
                return True
            except:
                self.root = None
                return False

        return False



    def getRoot(self):
        return self.root



    def addValue(self, value):
        if (self.root == None):
            return self.addHead(value)
        else:
            if (self.root.addChild(value)):
                self.number_items += 1
                return True

        return False



# Time complexity O(N)
def findLCA(root, node_value1, node_value2):
    path_1 = []
    path_2 = []

    # First find all the nodes that connect to the first node
    found_path_1 = findPath(root, node_value1, path_1)

    # Then find all the nodes that connect to the second node
    found_path_2 = findPath(root, node_value2, path_2)

    # Check if no path was found to either nodes
    if (not found_path_1 or not found_path_2):
        return -1

    # The LCA of the two nodes will be the first index in both path arrays that are different
    index = 0
    while (index < len(path_1) and index < len(path_2)):
        if (path_1[index] != path_2[index]):
            break
        index += 1

    return path_1[index-1]


def findPath(root, node_value, path_arr):
    bool = False
    if (root != None):
        if (node_value != None):
            try:
                if (node_value > root.value):
                    # Add this node to the path array
                    path_arr.append(root.value)

                    # Then move onto the next
                    bool = findPath(root.right, node_value, path_arr)

                elif (node_value < root.value):
                    # Add this node to the path array
                    path_arr.append(root.value)

                    # Then move onto the next
                    bool = findPath(root.left, node_value, path_arr)

                else:
                    # We have arrived at the node we were looking for
                    path_arr.append(root.value)
                    return True
            except:
                bool = False

    return bool
