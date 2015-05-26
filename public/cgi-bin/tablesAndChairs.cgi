#!/usr/bin/env python

import cgi,cgitb
import math

class Table:

    tableNumber = 0 #number of tables created

    def __init__(self, numOfChairs):
        '''initiates a table. numOfChairs is an int and defines how much chairs should be around the table'''
        try:
            x = numOfChairs + 1
            self.numOfChairs = numOfChairs
            Table.tableNumber += 1
            print("<script> console.log("+str(self.tableNumber)+") </script>")
        except TypeError:
            print('<script> alert("%r is not a valid number for number of chairs") </script>' %numOfChairs)

    def drawOnCanvas(self, canvas):
        '''draw table and chairs on canvas'''
        print('<script> var table'+str(Table.tableNumber)+' = addTable('+canvas+') </script>')
        print('<script> centerOnCanvas('+canvas+', table'+str(Table.tableNumber)+') </script>')
        angle = math.pi*2/(self.numOfChairs)
        r = 300
        print("<script> var xcoord = table1.attr('cx') </script>")
        print("<script> var ycoord = table1.attr('cy') </script>")
        print("<script> console.log(xcoord) </script>")
        print("<script> var dimOfDOM = getDimOfDOM('canvas_container') </script>")
        for chairs in range(self.numOfChairs):
            print("<script> console.log("+str(chairs)+") </script>")
            print("<script> var chair"+str(chairs)+" = addChair("+canvas+") </script>")
            print("<script> chair"+str(chairs)+".canvas.transform({rotation:"+str(angle*chairs*180/math.pi)+", x:dimOfDOM.width/2-(250+30+originalWidth), y:dimOfDOM.height/2-originalHeight/2, cx : xcoord, cy : ycoord}) </script>")

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
table1 = Table(15)
table1.drawOnCanvas('canvas1')
