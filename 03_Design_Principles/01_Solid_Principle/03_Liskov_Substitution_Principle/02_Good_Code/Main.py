from Concrete_Vehicles.Car import Car
from Concrete_Vehicles.Bicycle import Bicycle


def main():
    car = Car()
    car.start_engine()  # Output: Car-specific engine starting logic
    car.move()          # Output: Movement logic

    bicycle = Bicycle()
    bicycle.move()      # Output: Movement logic

if __name__ == "__main__":
    main()

"""
Output:
Non-Engine Vehicles do not have start engine method
"""
