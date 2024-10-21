# Base class
class Robot:
    def __init__(self, name, model, function):
        self.__name = name        # Encapsulation: __name is private to the class
        self.__model = model
        self.__function = function

    # Public method to introduce the robot
    def introduce(self):
        print(f"Hello! I am {self.__name}.")
        print(f"My model is {self.__model}.")
        print(f"My main function is {self.__function}.")
    
    # Protected method (can be accessed in subclass)
    def _robot_greeting(self):
        print("Beep boop! I am always happy to assist humans.")

# Derived class (Inheritance)
class AssistantRobot(Robot):
    def __init__(self, name, model, function, specialization):
        super().__init__(name, model, function)  # Calling the base class constructor
        self.__specialization = specialization   # Additional attribute for this class

    # Overriding method
    def introduce(self):
        super().introduce()  # Call the base class's introduce method
        print(f"I specialize in {self.__specialization}.")
        self._robot_greeting()  # Call protected method from base class

# Creating an instance of the AssistantRobot class
robot1 = AssistantRobot(name="ChatGPT", model="GPT-4", function="Conversational AI", specialization="Answering questions and helping with tasks")

# Introduce the robot
robot1.introduce()
