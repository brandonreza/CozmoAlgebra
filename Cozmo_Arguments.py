import cozmo
from cozmo.util \
import degrees, distance_mm, speed_mmps



def cozmo_program(robot:cozmo.robot.Robot):
# 180 is the lenght of the square on the table
#    test_parralelo(robot)

# call for equilateral triangle
    cozmo_triangleidentify(180,180,180,60,60,60,robot)
# call for isosceles triangle
    cozmo_triangleidentify(360,360,1.414*360,90,45,45,robot)
# call for scalene triangle
    cozmo_triangleidentify(4.18*120,1.99*120,3.92*120,68.55,28.17,83.27,robot)

def test_parralelo(robot:cozmo.robot.Robot):
# call with arguments with angle that gives error
    cozmo_parralelo(180, 180, 180, robot)

# call with arguments for a square
    cozmo_parralelo(180,180,90,robot)

#call with arguments for a rhombus
    cozmo_parralelo(180, 180, 120, robot)

# call for a simple parallelogram
    cozmo_parralelo(360, 180, 120, robot)


# create a function that takes in 4 arguments for a parrallelogram
# first argument - length - length of longest side
# second argument - width - length of shortest side
# third argument is the angle between long side and short side
# fourth argument is the robot
# test for a square or rhombus
# make Cozmo drive it
# do not hard code values in the function

def cozmo_parralelo(L,W,A,robot:cozmo.robot.Robot):
    if A < 90 or A > 170:
        robot.say_text("incorrect input for angle").wait_for_completed()
        return

    B = 180 - A

    if L == W and A == 90:
        # cozmo says " a square"
        robot.say_text("A square").wait_for_completed()
    elif L == W and A != 90:
        # cozmo says " a rhombus"
        robot.say_text("A rhombus").wait_for_completed()
    else:
        robot.say_text("A parallelogram").wait_for_completed()


    robot.drive_straight(distance_mm(L), speed_mmps(25)).wait_for_completed()
    robot.turn_in_place(degrees(-A)).wait_for_completed()
    robot.drive_straight(distance_mm(W), speed_mmps(25)).wait_for_completed()
    robot.turn_in_place(degrees(-B)).wait_for_completed()
    robot.drive_straight(distance_mm(L), speed_mmps(25)).wait_for_completed()
    robot.turn_in_place(degrees(-A)).wait_for_completed()
    robot.drive_straight(distance_mm(W), speed_mmps(25)).wait_for_completed()
    robot.turn_in_place(degrees(-B)).wait_for_completed()



def cozmo_triangleidentify(A,B,C,D,E,F,robot:cozmo.robot.Robot):
    if A == B and B == C:
        robot.say_text("An equaladeral triangle").wait_for_completed()
    elif A == B or B == C or A == C:
        robot.say_text("An isoscelese triangle").wait_for_completed()
    else:
        robot.say_text("A scalene triangle").wait_for_completed()


    if D == 90 or E == 90 or F == 90:
        robot.say_text("A right triangle").wait_for_completed()
#        if C*C != (A*A + B*B):
#            robot.say_text("This is not a triangle").wait_for_completed()
#            return

    robot.drive_straight(distance_mm(A), speed_mmps(25)).wait_for_completed()
    robot.turn_in_place(degrees(-(90-E)-90)).wait_for_completed()
    robot.drive_straight(distance_mm(C), speed_mmps(25)).wait_for_completed()
    robot.turn_in_place(degrees(F-180)).wait_for_completed()
    robot.drive_straight(distance_mm(B), speed_mmps(25)).wait_for_completed()
    robot.turn_in_place(degrees(-(90-D)-90)).wait_for_completed()



def cozmo_triangle(robot:cozmo.robot.Robot):
    robot.drive_straight(distance_mm(180), speed_mmps(25)).wait_for_completed()
    robot.turn_in_place(degrees(-90)).wait_for_completed()
    robot.drive_straight(distance_mm(180), speed_mmps(25)).wait_for_completed()
    robot.turn_in_place(degrees(-135)).wait_for_completed()
    robot.drive_straight(distance_mm(1.414*180), speed_mmps(25)).wait_for_completed()
    robot.turn_in_place(degrees(-135)).wait_for_completed()



def cozmo_triangle(robot:cozmo.robot.Robot):
    robot.drive_straight(distance_mm(180), speed_mmps(25)).wait_for_completed()
    robot.turn_in_place(degrees(-90)).wait_for_completed()
    robot.drive_straight(distance_mm(180), speed_mmps(25)).wait_for_completed()
    robot.turn_in_place(degrees(-135)).wait_for_completed()
    robot.drive_straight(distance_mm(1.414*180), speed_mmps(25)).wait_for_completed()
    robot.turn_in_place(degrees(-135)).wait_for_completed()



def cozmo_rectangle(robot:cozmo.robot.Robot):
    robot.drive_straight(distance_mm(520), speed_mmps(25)).wait_for_completed()
    robot.turn_in_place(degrees(-90)).wait_for_completed()
    robot.drive_straight(distance_mm(360), speed_mmps(25)).wait_for_completed()
    robot.turn_in_place(degrees(-90)).wait_for_completed()
    robot.drive_straight(distance_mm(520), speed_mmps(25)).wait_for_completed()
    robot.turn_in_place(degrees(-90)).wait_for_completed()
    robot.drive_straight(distance_mm(360), speed_mmps(25)).wait_for_completed()
    robot.turn_in_place(degrees(-90)).wait_for_completed()

def cozmo_square(robot:cozmo.robot.Robot):
    robot.drive_straight(distance_mm(180), speed_mmps(25)).wait_for_completed()
    robot.turn_in_place(degrees(-90)).wait_for_completed()
    robot.drive_straight(distance_mm(180), speed_mmps(25)).wait_for_completed()
    robot.turn_in_place(degrees(-90)).wait_for_completed()
    robot.drive_straight(distance_mm(180), speed_mmps(25)).wait_for_completed()
    robot.turn_in_place(degrees(-90)).wait_for_completed()
    robot.drive_straight(distance_mm(180), speed_mmps(25)).wait_for_completed()
    robot.turn_in_place(degrees(-90)).wait_for_completed()

cozmo.run_program(cozmo_program)