import Machine 
class BasicPrinter(Machine):
    def print(self):
        pass

    def scan(self):
        raise NotImplementedError("Cannot scan")

    def fax(self):
        raise NotImplementedError("Cannot fax")