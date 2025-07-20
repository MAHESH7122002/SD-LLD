from ..Interfaces import Printer,Scanner, Fax

class AllInOnePrinter(Printer, Scanner, Fax):
    def fax(self):
        pass

    def print(self):
        pass

    def scan(self):
        pass