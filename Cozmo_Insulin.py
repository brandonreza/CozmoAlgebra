import cozmo
from cozmo.util \
import degrees, distance_mm, speed_mmps



def cozmo_program(robot:cozmo.robot.Robot):
    robot.drive_straight(distance_mm(-5), speed_mmps(5)).wait_for_completed()
    robot.say_text("Hey Brandon!").wait_for_completed()


# write a function that calculates insulin units for number of carbs

    carbs = cozmo_carbs(40)
    robot.say_text("for 40 carbs you need: " + str(carbs) + " units").wait_for_completed()

# write a function that calculates insulin units for correcting above target glucose reading
# target is 120

    number = cozmo_number(154)
    robot.say_text("if your number is 154 you should get: " + str(number) + " units").wait_for_completed()


# what is your total units of insulin
    total = number + carbs
    robot.say_text("your number plus your carbs is: " + str(total) + " units").wait_for_completed()



def cozmo_carbs(carbs):
    return carbs / 10

def cozmo_number(number):
    if number - 120 > 0:
        return (number - 120) / 50
    else:
        return 0

cozmo.run_program(cozmo_program)


