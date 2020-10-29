
from collections import defaultdict



class DAG:
    def __init__(self):
        self.nodes = dict()         # {'A':[ parents = [], children = [], depth = 0]}
        self.root = None


    def get_nodes(self):
        return self.nodes


    # Insert a unique node into the graph
    def insert_node(self, node, parent, child):

        # Ensure the node name is a string
        node = str(node)

        if (node not in self.nodes):
            values = [[],[],0]
            self.nodes[node] = values

            if (parent != None):
                # Adding the parent node to the childs parent list in dictionary
                self.nodes[node][0].append(parent)

                # Updating the depth of a child node being inserted into dictionary
                self.nodes[node][2] = self.nodes[parent][2] + 1

            if (child != None):
                self.nodes[node][1].append(child)

            return True
        return False


    # Add an edge to the graph
    def add_edge(self, edge):
        parent = edge[0]
        child = edge[1]

        # See if we are able to insert this node into the dictionary
        if (not self.insert_node(parent, None, child)):
            # This parent exists in the dicionary so add child to this parents child set
            if (child not in self.nodes[parent][1]):
                self.nodes[parent][1].append(child)


        # Next step is to check to see if the child exists as its own entry in the dictionary
        if (not self.insert_node(child, parent, None)):
            # The child exists in the dictionary so just add parent to the childs parent list
            if (parent not in self.nodes[child][0]):
                self.nodes[child][0].append(parent)


    # Recursively get all the predecessors of a given node
    def recursiveSearch(self, node, passed_set):
        passed_set.add(node)
        for parent in self.nodes[node][0]:
            passed_set.add(node)
            self.recursiveSearch(parent, passed_set)


    # Find the LCA of the DAG
    def findLCA(self, firstNode, secondNode):

        first_path_nodes = set()
        second_path_nodes = set()


        # Check to make sure first target node is in the graph
        if (firstNode in self.nodes):
            self.recursiveSearch(firstNode, first_path_nodes)
        else:
            return -1


        # Check to make sure the second target node is in the graph
        if (secondNode in self.nodes):
            self.recursiveSearch(secondNode, second_path_nodes)
        else:
            return -1


        # Next only keep the path nodes which are common to both target nodes
        common_nodes = first_path_nodes & second_path_nodes


        # Last step is to go through each of the nodes and find the node with the largest depth
        largestValue = -2
        lca_node = None
        for node in common_nodes:
            if self.nodes[node][2] > largestValue:
                lca_node = node
                largestValue = self.nodes[node][2]


        return lca_node


    # Display the contents of the dictionary in a table format
    def displayTable(self):
        for pair in self.nodes.items():
            print(pair)



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
