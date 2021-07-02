import cozmo
from cozmo.util \
import degrees, distance_mm, speed_mmps


def cozmo_program(robot: cozmo.robot.Robot):

#    cozmo_forLoop(robot)
#    cozmo_whileLoop(robot)
#    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#    array = [1000, 2000, 3000]
#    array = ["p","o","o",2,"p","o","o"]
#    array = ["", "", "", "", "", "", "" ]
    array = ["lmn"]
    blah = cozmo_tostring(array,robot)
#    robot.say_text(blah).wait_for_completed()
    print("outside the function cozmo_tostring: blah: ", blah)

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


def cozmo_tostring(array,robot: cozmo.robot.Robot):

    result = ""
    for x in array:
        result += str(x)
        robot.say_text(str(x)).wait_for_completed()

    print("in the function cozmo_tostring - result: ", result)
    robot.say_text(result).wait_for_completed()
    return result

cozmo.run_program(cozmo_program)
