class Node():
    def __init__(self, id, option_title, description):
        # initializes a node object with its properties
        
        self.id = id # a unique id
        self.children = []  #a list of Node objects
        self.option_title = option_title  # text for display in the menu          
        self.description = description  # text to show if this option is selected 

    def __str__(self):
        # defines how a node will be printed out
        
        return f"{self.option_title}"

    def add_child(self, child_node):
        # adds a new child to this node

        self.children.append(child_node)

    def find(self, id):
        # 🚨 DO NOT EDIT THIS METHOD 🚨
        # It searches through the nodes to return the node with the given id
        # It uses a fancy technique called recursion to find the correct node
        # If you're interested in learning more, ask a teacher! 

        if self.id == id: 
            return self
        
        for child in self.children:
            n = child.find(id)
            if n is not None: 
                return n
        return None
    
    
