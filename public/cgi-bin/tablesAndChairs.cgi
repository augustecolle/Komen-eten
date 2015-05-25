#!/usr/bin/env python

import cgi,cgitb

class Table:
    def __init__(self, numOfChairs):
        '''initiates a table. numOfChairs is an int and defines how much chairs should be around the table'''
        try:
            x = numOfChairs + 1
            self.numOfChairs = numOfChairs
        except TypeError:
            print('<script> alert("%r is not a valid number for number of chairs") </script>' %numOfChairs)





print("Content-Type: text/html\n\n")
print("<html>")
print("<head>")
print("<title>This is the title</title>")
print('<style type="text/css"> #canvas_container { width: 1000; height: 500px; border: 1px solid #aaa; } </style>')
print("</head>")
print('<body>')
print('<div id="canvas_container"></div>')
print('</body>')
print("</html>")

print('<script src="../table_and_chairs/svg.js" type="text/javascript"></script>')
print('<script src="../table_and_chairs/svg.parser.js" type="text/javascript"></script>')
print('<script src="../table_and_chairs/svg.import.js" type="text/javascript"></script>')
print('<script src="../table_and_chairs/tryOutAuguste.js" type="text/javascript"></script>')
 
table = Table(5)
