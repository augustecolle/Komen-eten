#!/usr/bin/env python
import imp # to find our user_database module
mod = imp.find_module("session_manager",["."])
session_manager = imp.load_module("session_manager",*mod)

import cgi,cgitb
import math

class Table:

    tableNumber = 0 #number of tables created

    def __init__(self, numOfChairs):
        '''initiates a table. numOfChairs is an int and defines how much chairs should be around the table'''
        try:
            x = numOfChairs + 1
            self.numOfChairs = numOfChairs
            self.tableNumber = Table.tableNumber
            Table.tableNumber += 1
            print("<script> console.log("+str(self.tableNumber)+") </script>")
        except TypeError:
            print('<script> alert("%r is not a valid number for number of chairs") </script>' %numOfChairs)

    def drawOnCanvas(self, canvas):
        '''draw table and chairs on canvas'''
        print('<script> var table'+str(self.tableNumber)+' = addTable('+canvas+') </script>')
        print('<script> centerOnCanvas('+canvas+', table'+str(self.tableNumber)+') </script>')
        angle = math.pi*2/(self.numOfChairs)
        r = 300
        print("<script> var xcoord = table"+str(self.tableNumber)+".attr('cx') </script>")
        print("<script> var ycoord = table"+str(self.tableNumber)+".attr('cy') </script>")
        print("<script> var radius = table"+str(self.tableNumber)+".attr('rx') </script>")
        print("<script> console.log(radius) </script>")
        print("<script> var dimOfDOM = getDimOfDOM('canvas_container') </script>")

        if (self.numOfChairs < 16):
            for chairs in range(self.numOfChairs):
                print("<script> console.log("+str(self.tableNumber)+str(chairs)+") </script>")
                print("<script> var chair"+str(self.tableNumber)+str(chairs)+" = addChair("+canvas+") </script>")
                print("<script> chair"+str(self.tableNumber)+str(chairs)+".canvas.cx(dimOfDOM.width - xcoord - radius - 110) </script>")
                print("<script> chair"+str(self.tableNumber)+str(chairs)+".canvas.cy(ycoord) </script>")
                print("<script> chair"+str(self.tableNumber)+str(chairs)+".canvas.transform({rotation:"+str(angle*chairs*180/math.pi)+", cx : xcoord, cy : ycoord}) </script>")
        else:
            scaleFactor = 15.0/self.numOfChairs
            for chairs in range(self.numOfChairs):
                print("<script> table"+str(self.tableNumber)+".attr('rx',radius+160*(1-"+str(scaleFactor)+"))  </script>")
                print("<script> table"+str(self.tableNumber)+".attr('ry',radius+160*(1-"+str(scaleFactor)+"))  </script>")
                print("<script> var chair"+str(self.tableNumber)+str(chairs)+" = addChair("+canvas+") </script>")
                print("<script> chair"+str(self.tableNumber)+str(chairs)+".canvas.scale("+str(scaleFactor)+", "+str(scaleFactor)+") </script>")
                print("<script> chair"+str(self.tableNumber)+str(chairs)+".canvas.cx(dimOfDOM.width - xcoord - radius - 110) </script>")
                print("<script> chair"+str(self.tableNumber)+str(chairs)+".canvas.cy(ycoord + originalHeight/2*(1-"+str(scaleFactor)+")) </script>")
                print("<script> chair"+str(self.tableNumber)+str(chairs)+".canvas.transform({rotation:"+str(angle*chairs*180/math.pi)+", cx : xcoord, cy : ycoord}) </script>")

# only allow the execution of this function when user is authenticated
@session_manager.sessionAuth
def main():
    print("Content-Type: text/html\n\n")
    print("<html>")
    print("<head>")
    print("<title>This is the title</title>")
    print('<style type="text/css"> #canvas_container { width: 1500; height: 1000; border: 1px solid #aaa; } </style>')
    print("</head>")
    print('<body>')
    print('<div id="canvas_container"></div>')
    print('</body>')
    print("</html>")

    print('<script src="../table_and_chairs/svg.js" type="text/javascript"></script>')
    print('<script src="../table_and_chairs/svg.parser.js" type="text/javascript"></script>')
    print('<script src="../table_and_chairs/svg.import.js" type="text/javascript"></script>')
    print('<script src="../table_and_chairs/tryOutAuguste.js" type="text/javascript"></script>')
     
    print("<script> var canvas1 = newCanvas('canvas_container', '100%','100%') </script>")
    table1 = Table(30)
    table1.drawOnCanvas('canvas1')

main()
