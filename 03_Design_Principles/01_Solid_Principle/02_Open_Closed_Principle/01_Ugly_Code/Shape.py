class Shape:
    
    def __init__(self,type):
        self.type = type
        
    def calculateArea(self):
        if self.type=="circle":
            #circle area calculation
            print("circle area calculation")
        elif self.type=="rectangle":
            #rectangle area calculation
            print("rectangle area calculation")
        else:
            return 0
        
shp = Shape("circle")
shp.calculateArea()
    