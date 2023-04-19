from story_setup import main_story
from view import View

view = View()

view.start_game(main_story)

chosen_node = view.menu("[what will you do?]", main_story.get_current_children())

view.end_game()

