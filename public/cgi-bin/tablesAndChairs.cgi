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
        except TypeError:
            print('<script> alert("%r is not a valid number for number of chairs") </script>' %numOfChairs)

    def drawOnCanvas(self, canvas):
        '''draw table and chairs on canvas'''
        angle = math.pi*2/(self.numOfChairs)
        print("<script> var group"+str(self.tableNumber)+" = "+canvas+".group() \n"
        " var table"+str(self.tableNumber)+" = addTable("+canvas+") \n"
        " centerOnCanvas("+canvas+", table"+str(self.tableNumber)+") \n"
        " var xcoord = table"+str(self.tableNumber)+".attr('cx') \n"
        " var ycoord = table"+str(self.tableNumber)+".attr('cy') \n"
        " var radius = table"+str(self.tableNumber)+".attr('rx') \n"
        " var dimOfDOM = getDimOfDOM('canvas_container') \n"
        " group"+str(self.tableNumber)+".add(table"+str(self.tableNumber)+") </script>")
        if (self.numOfChairs < 16):
            for chairs in range(self.numOfChairs):
                print("<script> var chair"+str(self.tableNumber)+str(chairs)+" = addChair("+canvas+") \n"
                " chair"+str(self.tableNumber)+str(chairs)+".canvas.cx(dimOfDOM.width - xcoord - radius - 110) \n"
                " chair"+str(self.tableNumber)+str(chairs)+".canvas.cy(ycoord) \n"
                " var xcoordOri = chair"+str(self.tableNumber)+str(chairs)+".canvas.x() \n"
                " var eventRecord"+str(self.tableNumber)+str(chairs)+"= 0 \n"
                " chair"+str(self.tableNumber)+str(chairs)+".canvas.transform({rotation:"+str(angle*chairs*180/math.pi)+", cx : xcoord, cy : ycoord}) \n"
                " group"+str(self.tableNumber)+".add(chair"+str(self.tableNumber)+str(chairs)+".canvas) \n"
                "animatedChair"+str(self.tableNumber)+str(chairs)+" = chair"+str(self.tableNumber)+str(chairs)+".canvas.animate(0,'=',0)\n"
                "document.getElementById(chair"+str(self.tableNumber)+str(chairs)+".canvas.node.id).onmouseover = function(event) { eventRecord"+str(self.tableNumber)+str(chairs)+"+= 1 \n"
                #" if (chair"+str(self.tableNumber)+str(chairs)+".canvas.x() == xcoordOri){ \n"
"  animatedChair"+str(self.tableNumber)+str(chairs)+".animate(500,'<',0).dx((-chair"+str(self.tableNumber)+str(chairs)+".canvas.x()+xcoordOri-50)) \n"
"} \n"
                "document.getElementById(chair"+str(self.tableNumber)+str(chairs)+".canvas.node.id).onmouseleave = function(event) { \n "
"  animatedChair"+str(self.tableNumber)+str(chairs)+".animate(500,'<',0).dx(-(chair"+str(self.tableNumber)+str(chairs)+".canvas.x()-xcoordOri)) \n"
"} \n"
 "</script> ")
        else:
            scaleFactor = 15.0/self.numOfChairs
            #scale table
            print("<script> table"+str(self.tableNumber)+".attr('rx',radius+160*(1-"+str(scaleFactor)+"))  \n"
            " table"+str(self.tableNumber)+".attr('ry',radius+160*(1-"+str(scaleFactor)+"))  </script>")
            for chairs in range(self.numOfChairs):
                print("<script> var chair"+str(self.tableNumber)+str(chairs)+" = addChair("+canvas+") \n"
                " chair"+str(self.tableNumber)+str(chairs)+".canvas.scale("+str(scaleFactor)+", "+str(scaleFactor)+") \n"
                " chair"+str(self.tableNumber)+str(chairs)+".canvas.cx(dimOfDOM.width - xcoord - radius - 110) \n"
                " chair"+str(self.tableNumber)+str(chairs)+".canvas.cy(ycoord + originalHeight/2*(1-"+str(scaleFactor)+")) \n"
                " chair"+str(self.tableNumber)+str(chairs)+".canvas.transform({rotation:"+str(angle*chairs*180/math.pi)+", cx : xcoord, cy : ycoord}) \n"
                " group"+str(self.tableNumber)+".add(chair"+str(self.tableNumber)+str(chairs)+".canvas) </script>")

    @staticmethod
    def putTablesOnDiv(div):
        '''static method to scale all tables and put in a div'''
        nCols = int(math.ceil(math.sqrt(Table.tableNumber)))
        nRows = int(math.ceil(Table.tableNumber/float(nCols)))
        scaleF = 1.00/(2*nCols)
        print("<script> var dimOfDiv = getDimOfDOM('"+div+"') \n " 
        "var scale2div = dimOfDiv.width/group0.bbox().width \n" 
        " var groupWidth = group0.bbox().width </script>")
        for row in range(nRows):
            for col in range(nCols):
                if ((nCols*row)+(col) < Table.tableNumber):
                    print("<script> group"+str(row*nCols+col)+".scale(scale2div*"+str(scaleF)+",scale2div*"+str(scaleF)+") \n"
                    "group"+str(row*nCols+col)+".cx(-group"+str(row*nCols+col)+".rbox().cx  + group"+str(row*nCols+col)+".bbox().width/2 + dimOfDiv.width/"+str(nCols*2)+"*"+str(col*2+1)+") \n" 
                    " group"+str(row*nCols+col)+".cy(-group"+str(row*nCols+col)+".rbox().cy + group"+str(row*nCols+col)+".bbox().height/2 + dimOfDiv.height/"+str(2*nRows)+"*"+str(row*2+1)+") </script>")

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
    print('<script src="../table_and_chairs/sugar.min.js" type="text/javascript"></script>')
    print('<script src="../table_and_chairs/tryOutAuguste.js" type="text/javascript"></script>')
     
    print("<script> var canvas1 = newCanvas('canvas_container', '100%','100%') </script>")
    #table1 = Table(36)
    #table1.drawOnCanvas('canvas1')
    #table2 = Table(12)
    #table2.drawOnCanvas('canvas1')
    tables = []
    for x in range(5):
        tables.append(Table(6))
        tables[x].drawOnCanvas('canvas1')

    Table.putTablesOnDiv('canvas_container')

main()
