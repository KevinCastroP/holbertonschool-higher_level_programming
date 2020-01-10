#!/usr/bin/python3
class Robot:
    """Represents a robot, with a name."""

    #a class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        """Initializes the data."""
        self.name = name
        print("(Initializing {})".format(self.name))

        #when this person is created, the robot adds to the population
        Robot.population += 1

    def die(self):
        """I'm dying."""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one".format(self.name))

        else:
            print("there are still {:d} robots working.".format(Robot.population))

    def say_hi(self):
        """greeting by the robot.

        yeah, they can do that."""
        print("greeting, my masters call me {}".format(self.name))

    @classmethod
    def how_many(cls):
        """prints the current population"""
        print("we have {:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()
