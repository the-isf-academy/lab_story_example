from InquirerPy import inquirer, get_style  # importing a Terminal menu system

class View:

    def menu(self,prompt, options):
        # This function creates an interactive Terminal menu.
        # it returns the selected Node 

        choice = inquirer.select(
            message= f"\n{prompt}",
            choices= options,
            qmark="",
            amark="",
            style= get_style({ 
                "answer": "#438fa8",
                "pointer": "#438fa8",
                "questionmark": "hidden"},

                ),
            ).execute()

        return choice
    
    def start_game(self, story):
        # prints out a start message for the user,
        # including the title and description of the start node
        print("="*50)
        print(f"Title: {story.title}")
        print(f"\n{story.current_node.option_title}")
        print(f"{story.current_node.description}")
        print("="*50)

    def show_current_description(self,node):
        print(f"{node.description}")

    def end_game(self):
        print("\n")
        print("="*50)
        print("End of Story")
        print("="*50)


