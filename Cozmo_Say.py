import cozmo
from cozmo.util \
import degrees, distance_mm, speed_mmps


def cozmo_program2(robot: cozmo.robot.Robot):
    # Drive forwards for 150 millimeters at 50 millimeters-per-second.
    robot.drive_straight(distance_mm(-5), speed_mmps(5)).wait_for_completed()

    # Turn 90 degrees to the left.
    # Note: To turn to the right, just use a negative number.
#    robot.turn_in_place(degrees(90)).wait_for_completed()



def cozmo_program(robot:cozmo.robot.Robot):
#    robot.drive_wheels(-1, -1)
    robot.drive_straight(distance_mm(-5), speed_mmps(5)).wait_for_completed()
    robot.say_text("Hey Brandon!").wait_for_completed()
    cozmo_say("Calling your new function Brandon", robot)

def cozmo_say(sentence, robot: cozmo.robot.Robot):
    robot.say_text(sentence).wait_for_completed()

cozmo.run_program(cozmo_program)