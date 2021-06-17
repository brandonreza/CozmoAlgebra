import cozmo
from cozmo.util \
import degrees, distance_mm, speed_mmps



def cozmo_program(robot:cozmo.robot.Robot):
    robot.drive_straight(distance_mm(-5), speed_mmps(5)).wait_for_completed()
    robot.say_text("Hey Brandon!").wait_for_completed()


# addition
#    robot.say_text("subtract: " + str(5) + " AND " + str(2)).wait_for_completed()
#    answer = cozmo_subtract(5,2,robot)
#    robot.say_text("your subtraction answer is: " + str(answer)).wait_for_completed()
# subtraction
#    robot.say_text("subtract: " + str(5) + " AND " + str(2)).wait_for_completed()
#   answer = cozmo_subtract(5,2,robot)
#    robot.say_text("your subtraction answer is: " + str(answer)).wait_for_completed()


# mulitplication
#    robot.say_text("multiply: " + str(5) + " AND " + str(2)).wait_for_completed()
#    answer = cozmo_multiply(5,2,robot)
#    robot.say_text("your multiplication answer is: " + str(answer)).wait_for_completed()

# division
#    robot.say_text("divide: " + str(6) + " AND " + str(4)).wait_for_completed()
#   answer = cozmo_divide(6,4,robot)
#    robot.say_text("your division answer is: " + str(answer)).wait_for_completed()

# function to give me total number of egggs given number of dozens of eggs
    robot.say_text("A chicken laid 8 dozen eggs. How many eggs are there?").wait_for_completed()
    answer = cozmo_eggs(8)
    robot.say_text("the total number of eggs is: " + str(answer)).wait_for_completed()


# write a function to do addition (two arguments: a and b)
# call your  function with some numbers


def cozmo_add(a,b, robot:cozmo.robot.Robot):
    return a + b

def cozmo_subtract(a,b, robot:cozmo.robot.Robot):
    return a - b

def cozmo_multiply(a, b, robot: cozmo.robot.Robot):
    return a * b

def cozmo_divide(a, b, robot: cozmo.robot.Robot):
    return a / b

def cozmo_eggs(dozens):
    return dozens * 12

cozmo.run_program(cozmo_program)