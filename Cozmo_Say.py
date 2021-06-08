import cozmo

def cozmo_program(robot:cozmo.robot.Robot):
    robot.say_text("Hey Brandon! Are you going to play Call of Duty? Let me see so I can prove you are a big noob at it!").wait_for_completed()
    cozmo_say("Calling your new function Brandon", robot)

def cozmo_say(sentence, robot: cozmo.robot.Robot):
    robot.say_text(sentence).wait_for_completed()

cozmo.run_program(cozmo_program)