from view import View
from story_setup import main_story

view = View()

view.start_game(main_story)

while main_story.is_running() == False: 

    chosen_node = view.menu("[what will you do?]", main_story.get_current_children())

    # 💻 finish the code below 💻 


view.end_game()




