class Node_down:
    def __init__(self):
        """
        Index 0 = Down 1
        Index 1 = Down 2
        Index 2 = Down 3
        Index 3 = Down 4
        """
        self.down_list = [Node_dst(), Node_dst(), Node_dst(), Node_dst()]

class Node_dst:
    def __init__(self):
        """
        Index 0 = Short
        Index 1 = Medium
        Index 2 = Long
        """
        self.dst_list = [Node_type(), Node_type(), Node_type()]

class Node_type:
    def __init__(self):
        """
        Index 0 = Run
        Index 1 = Pass
        """
        self.type_list = [Node_playset(), Node_playset()]

class Node_playset:
    def __init__(self):
        self.playset = [None, None, None]

class Node_Info:
    def __init__(self, name):
        self.playName = name

"""
The Play_Structure Class is the wrapper that 
contains my functions to add and find plays.
"""

class play_structure:
    def __init__(self):
        self.root = Node_down()

    def add_play(self, playset, name):
        for i in range(len(playset)):
            if playset[i] == None:
                playset[i] = Node_Info(name)
                break
        return self

    def find_playset(self, down, dst, type):
        for i in range(len(self.root.down_list)):
            if i == (down - 1):
                for j in range(len(self.root.down_list[i].dst_list)):
                    if j == (dst - 1):
                        for k in range(len(self.root.down_list[i].dst_list[j].type_list)):
                            if k == (type - 1):
                                return self.root.down_list[i].dst_list[j].type_list[k].playset