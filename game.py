# 💻 Finish this file so it properly plays through the story 

from story_setup import story_setup
from view import View

view = View()
main_story = story_setup()

view.start_game(main_story)

chosen_node = view.menu("[what will you do?]", main_story.get_current_children())


view.end_game()




