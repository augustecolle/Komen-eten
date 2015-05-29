//http://documentup.com/wout/svg.js
//
//
//-----------------Inkscape figure raw data for drawing the chair-------------------

var originalWidth = 167.14912 //164.98347
var originalHeight = 177.74756 //182.59712
var widthHeightRatio = originalWidth/originalHeight

var rawSVGchair = '<?xml version="1.0" encoding="UTF-8" standalone="no"?> <!-- Created with Inkscape (http://www.inkscape.org/) --> <svg xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" version="1.1" width="167.14912" height="177.74756" id="svg2"> <defs id="defs4" /> <metadata id="metadata7"> <rdf:RDF> <cc:Work rdf:about=""> <dc:format>image/svg+xml</dc:format> <dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage" /> <dc:title></dc:title> </cc:Work> </rdf:RDF> </metadata> <g id="g3046"> <path d="m 160.64912,88.86892 a 63.741441,62.886905 0 1 1 -127.482869,0 63.741441,62.886905 0 1 1 127.482869,0 z" id="zitje" style="fill:none;stroke:#000000;stroke-width:13;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;stroke-dashoffset:0" /> <path d="m 19.334768,88.86892 a 6.4173929,82.167984 0 1 1 -12.8347503,0 6.4173929,82.167984 0 1 1 12.8347503,0 z" id="path3820" style="fill:none;stroke:#000000;stroke-width:13;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;stroke-dashoffset:0" /> <path d="m 12.199835,171.24756 c 11.82842,-13.29298 14.698568,-39.91999 42.157908,-34.90023" id="path3844" style="fill:none;stroke:#000000;stroke-width:13;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" /> <path d="m 11.440297,6.5 c 13.50596,18.1421 23.629946,38.663577 41.291406,37.331767" id="path3844-2" style="fill:none;stroke:#000000;stroke-width:13;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" /> <path d="m 13.662094,88.86892 152.544676,0" id="path2994" style="fill:none;stroke:#000000;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:2, 1;stroke-dashoffset:0" /> <path d="m 96.907687,11.527475 0,152.544675" id="path2994-1" style="fill:none;stroke:#000000;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:2, 1;stroke-dashoffset:0" /> </g> </svg>'


var rawSVGchair1 = '<?xml version="1.0" encoding="UTF-8" standalone="no"?> <!-- Created with Inkscape (http://www.inkscape.org/) --> <svg xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" version="1.1" width="164.98347" height="182.59712" id="svg2"> <defs id="defs4" /> <metadata id="metadata7"> <rdf:RDF> <cc:Work rdf:about=""> <dc:format>image/svg+xml</dc:format> <dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage" /> <dc:title></dc:title> </cc:Work> </rdf:RDF> </metadata> <path d="m 158.45623,91.516994 a 63.741441,62.886905 0 1 1 -127.482872,0 63.741441,62.886905 0 1 1 127.482872,0 z" id="zitje" style="fill:none;stroke:#000000;stroke-width:13;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;stroke-dashoffset:0" /> <path d="m 17.141875,91.516331 a 6.4173929,81.751115 0 1 1 -12.8347504,0 6.4173929,81.751115 0 1 1 12.8347504,0 z" id="path3820" style="fill:none;stroke:#000000;stroke-width:13;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;stroke-dashoffset:0" /> <path d="M 10.006942,173.47711 C 21.835362,160.18413 24.70551,133.55712 52.16485,138.57688" id="path3844" style="fill:none;stroke:#000000;stroke-width:13;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" /> <path d="M 9.2474039,8.7295529 C 22.753364,26.871653 32.87735,47.39313 50.53881,46.06132" id="path3844-2" style="fill:none;stroke:#000000;stroke-width:13;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" /> </svg>'
//-------------------------------------------------------------------------------------

function scale(svg, factor){
    //lock dimension ratio
    svg.scale(factor, factor)
    }

function newCanvas(container, procHeight, procWidth){
    //container is a string representing the DOM element where the SVG will be drawn
    //procHeight is a string representing the procentual height of the DOM element which will be used to draw the canvas, defaults to 100%
    //same for procWidth
    //returns a SVG object 
    procHeight = typeof procHeight !== 'undefined' ? procHeight : '100%';
    procWidth = typeof procWidth !== 'undefined' ? procWidth : '100%';
    return SVG(container).size(procHeight, procWidth)
    }

function addChair(oricanvas){
    //canvas is a SVG object, draws a chair on the canvas
    //returns the chair as an SVG object
    //returns an object containing the references to all objects in the SVG chair drawing 
    var nested = oricanvas.nested().size(originalHeight, originalWidth)
    return {canvas:nested, objects:nested.svg(rawSVGchair)}
    }

function addTable(canvas){
    var nested = canvas.nested()
    return nested.circle(500).fill('none').stroke({color: '#000000', opacity: 1, width: 10})
    }      

function fillChair(chair, color){
    //fill seat of chair, chair is an object containing the references to all objects in the SVG chair drawing, color is a hexadecimal string format ex. '#FF0000'
    chair.get('zitje').style('fill:'+color+';stroke:#000000;stroke-width:13;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;stroke-dashoffset:0')
    }
    
function getDimOfDOM(DOMid){
    //returns the dimensions of the DOM element with id DOMid
    var width = document.getElementById(DOMid).offsetWidth;
    var height = document.getElementById(DOMid).offsetHeight;
    return {width:width, height:height} 
    }

function getDimOfCanvas(canvas){
    //returns the dimensions of the canvas
    var dim = getDimOfDOM(canvas.parent.id)
    var hperc = parseFloat(canvas.attr('height'))/100.0
    var wperc = parseFloat(canvas.attr('width'))/100.0
    var width = dim.width*wperc
    var height = dim.height*hperc
    return {width:width, height:height} 
    }

function centerOnCanvas(canvas, SVG){
    //canvas is the canvas where the SVG is drawn on
    SVG.center(getDimOfCanvas(canvas).width/2, getDimOfCanvas(canvas).height/2)
    }

function centerOnDiv(divId, SVG){
    //divId is the id of the div conatining the SVG
    console.log(getDimOfDOM(divId).width/2)
    SVG.center(getDimOfDOM(divId).width/2, getDimOfDOM(divId).height/2)
    }





//test code
//var canvas1 = newCanvas('canvas_container', '100%','100%')
//var chair1 = addChair(canvas1)
//chair1.canvas.transform({
//  rotation: 45,
//  x: 50,
//  y: 50
//})

//var chair2 = addChair(canvas1)
//fillChair(chair2.objects, '#FF0000')
//var table1 = addTable(canvas1)
//centerOnCanvas(canvas1, table1)
//getDimOfCanvas(canvas1)
