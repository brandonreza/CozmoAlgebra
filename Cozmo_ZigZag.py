import cozmo
from cozmo.util \
import degrees, distance_mm, speed_mmps



def cozmo_program(robot:cozmo.robot.Robot):
    cozmo_zigzag(robot)


def cozmo_triangle(robot:cozmo.robot.Robot):
    robot.drive_straight(distance_mm(365), speed_mmps(25)).wait_for_completed()
    robot.turn_in_place(degrees(-90)).wait_for_completed()
    robot.drive_straight(distance_mm(365), speed_mmps(25)).wait_for_completed()
    robot.turn_in_place(degrees(-135)).wait_for_completed()
    robot.drive_straight(distance_mm(1.414*365), speed_mmps(25)).wait_for_completed()
    robot.turn_in_place(degrees(-135)).wait_for_completed()

def cozmo_zigzag(robot:cozmo.robot.Robot):
    robot.drive_straight(distance_mm(1.414*365), speed_mmps(25)).wait_for_completed()
    robot.turn_in_place(degrees(135)).wait_for_completed()
    robot.drive_straight(distance_mm(365), speed_mmps(25)).wait_for_completed()
    robot.turn_in_place(degrees(135)).wait_for_completed()
    robot.drive_straight(distance_mm(1.414*365), speed_mmps(25)).wait_for_completed()
    robot.turn_in_place(degrees(-135)).wait_for_completed()
    robot.drive_straight(distance_mm(365), speed_mmps(25)).wait_for_completed()
    robot.turn_in_place(degrees(-90)).wait_for_completed()
cozmo.run_program(cozmo_program)