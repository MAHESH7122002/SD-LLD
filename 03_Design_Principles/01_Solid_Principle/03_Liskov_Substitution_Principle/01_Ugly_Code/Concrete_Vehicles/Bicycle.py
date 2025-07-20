from Vehicle import Vehicle

class Bicycle(Vehicle):
    def start_engine(self):
        raise UnsupportedOperationException("Bicycles don't have engines")

class UnsupportedOperationException(Exception):
    pass
