from pybricks.tools import hub_menu

# This example assumes that you have three other programs in Pybricks Code,
# called "fly_mission", "drive_mission", and "zigzag". This example creates a
# menu that lets you pick which one to run.

# Choose a letter.
selected = hub_menu("1", "2", "3","4")

# Based on the selection, run a program.

if selected == "1":
    import run1_redside #mission 1,2
elif selected == "2":
    import run2_redside #mission 11,12,15 cross over to the blue side
elif selected == "3":
    import run1_blueside #mission 5,6,7
elif selected == "4":
    import run2_blueside #mission 9,10