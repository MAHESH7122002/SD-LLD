from Concrete_Vehicles.Car import Car
from Concrete_Vehicles.Bicycle import Bicycle, UnsupportedOperationException


def main():
    car = Car()
    bicycle = Bicycle()
    print("Car:")
    car.start_engine()
    print("\nBicycle:")
    try:
        bicycle.start_engine()
    except UnsupportedOperationException as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

"""
Output:
Car:
Car engine started.

Bicycle:
Error: Bicycles don't have engines
"""
