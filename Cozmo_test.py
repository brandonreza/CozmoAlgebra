import cozmo
from cozmo.util \
import degrees, distance_mm, speed_mmps


# write a function that takes 2 arguments
# first argument is a number
# second argument is a string
# function returns a string , first appears after the second string



def cozmo_program(robot:cozmo.robot.Robot):
    robot.drive_straight(distance_mm(-5), speed_mmps(5)).wait_for_completed()
    robot.say_text("i maxed skykov in cod yay").wait_for_completed()

    robot.drive_straight(distance_mm(30), speed_mmps(5)).wait_for_completed()
    robot.say_text("i moved yay").wait_for_completed()

    robot.say_text("i will add: " + str(100) + "AND" + str(50)).wait_for_completed()
    answer = cozmo_add(100,50)
    robot.say_text("my addition answer is: " + answer).wait_for_completed()



def cozmo_add (a,b):
    return str(a + b)

cozmo.run_program(cozmo_program)