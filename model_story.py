from model_node import Node

class Story():
    def __init__(self, title, start_id, start_option_title, start_description):
        # initializes a Story object with its properties

        self.title = title # the title of your story
        self.current_node = Node(start_id, start_option_title, start_description) #the current Node of your story
        self.first_node = self.current_node # the first Node of your story
        

    def add_new_child(self, parent_id, child_id, child_option_title, child_description):
        parent_node = self.current_node.find(parent_id)

        new_child_node = Node(
            id = child_id,
            option_title = child_option_title,
            description= child_description
        )
        
        parent_node.add_child(new_child_node)

    def get_current_children(self):
        return self.current_node.children

    def set_current_node(self,chosen_node):
        self.current_node = chosen_node
  
    def is_finished(self):
        if len(self.current_node.children) == 0:
            return True
        else:
            return False 
    






    




