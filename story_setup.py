from story import Story


main_story = Story(
    title='Lunch.',
    start_id = 'lunch',
    start_option_title = "It's lunch time.",
    start_description= "Where will you go?"
)

main_story.add_new_child(
    parent_id = 'lunch', 
    child_id = 'cyberport',
    child_option_title='Walk to cyberport.',
    child_description="It's a nice day, better to go for a short walk."
    )

main_story.add_new_child(
    parent_id = 'cyberport', 
    child_id = 'fusion',
    child_option_title='Go to fusion.',
    child_description="It's a grocery store day! What should I get?"
    )

main_story.add_new_child(
    parent_id = 'lunch', 
    child_id = 'isf_ablock_cafe',
    child_option_title='Elevator down to A Block Cafeteria.',
    child_description="You're short on time, better to grab something quick downstairs."
    )

main_story.add_new_child(
    parent_id = 'isf_ablock_cafe', 
    child_id = 'optionA',
    child_option_title='Char Siu Rice',
    child_description="Yum, pork!"
    )








