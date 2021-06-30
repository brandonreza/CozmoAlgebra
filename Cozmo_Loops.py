import cozmo
from cozmo.util \
import degrees, distance_mm, speed_mmps


def cozmo_program(robot: cozmo.robot.Robot):

    cozmo_forLoop(robot)
#    cozmo_whileLoop(robot)



def cozmo_forLoop(robot: cozmo.robot.Robot):
    robot.say_text("In For loop").wait_for_completed()

    forloop = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    for x in forloop:
        robot.turn_in_place(degrees(-90)).wait_for_completed()
        robot.say_text(str(x)).wait_for_completed()

    robot.say_text(str("finished")).wait_for_completed()


def cozmo_whileLoop(robot: cozmo.robot.Robot):
    robot.say_text("In while loop").wait_for_completed()

    i = 1
    while i < 11:
        robot.turn_in_place(degrees(-90)).wait_for_completed()
        robot.say_text(str(i)).wait_for_completed()
        if (i == 10):
            break
        i += 1

    robot.say_text(str("finished")).wait_for_completed()

cozmo.run_program(cozmo_program)