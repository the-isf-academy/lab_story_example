from story_setup import story_setup
from view import View

# setup
view = View()
main_story = story_setup()

# show the start message
view.start_game(main_story)



# 💻 FINISH THIS FILE SO IT PROPERLY PLAYS THROUGH THE STORY 

# show a menu of all the options, and save the choice in a variable
chosen_node = view.menu("[what will you do?]", main_story.get_current_children())



# show the end message
view.end_game()




