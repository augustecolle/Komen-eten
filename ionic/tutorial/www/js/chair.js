var rawChair = '<?xml version="1.0" encoding="UTF-8" standalone="no"?> <!-- Created with Inkscape (http://www.inkscape.org/) --> <svg xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" version="1.1" width="167.14912" height="177.74756" id="svg2"> <defs id="defs4" /> <metadata id="metadata7"> <rdf:RDF> <cc:Work rdf:about=""> <dc:format>image/svg+xml</dc:format> <dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage" /> <dc:title></dc:title> </cc:Work> </rdf:RDF> </metadata> <g id="stoel"> <path d="m 160.64912,88.86892 a 63.741441,62.886905 0 1 1 -127.482869,0 63.741441,62.886905 0 1 1 127.482869,0 z" id="zitje" style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:13;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;stroke-dashoffset:0" /> <path d="m 19.334768,88.86892 a 6.4173929,82.167984 0 1 1 -12.8347503,0 6.4173929,82.167984 0 1 1 12.8347503,0 z" id="leuningboven" style="fill:#000000;fill-opacity:1;stroke:#000000;stroke-width:13;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;stroke-dashoffset:0" /> <g id="leuningzij"> <path d="m 12.199835,171.24756 c 11.82842,-13.29298 14.698568,-39.91999 42.157908,-34.90023" id="path3844" style="fill:none;stroke:#000000;stroke-width:13;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" /> <path d="M 11.102374,4.8103844 C 24.608334,22.952484 35.070243,45.163577 52.731703,43.831767" id="path3844-2" style="fill:none;stroke:#000000;stroke-width:13;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" /> </g> <path d="m 32.258489,88.86892 138.085801,0" id="path3061" style="fill:none;stroke:#000000;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:0.35294118;stroke-dasharray:4, 1;stroke-dashoffset:0" /> <path d="m 96.907686,7.6266953 0,162.4844447" id="path3059" style="fill:none;stroke:#000000;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:0.35294118;stroke-dasharray:4, 1;stroke-dashoffset:0" /> <path d="m 24.663292,138.45189 c 0.07928,-0.80551 0.351648,-6.07795 0.605254,-11.71654 0.368562,-8.19445 0.461148,-15.80994 0.461325,-37.945606 2.17e-4,-27.163047 -0.224105,-37.056499 -1.150178,-50.727286 -0.114093,-1.684252 -0.198387,-3.08084 -0.187319,-3.103529 0.01107,-0.02269 1.098576,1.169474 2.416687,2.649252 3.724412,4.181214 8.078086,7.732294 11.773783,9.603303 l 1.388669,0.703037 -2.137476,3.262231 c -5.822719,8.886678 -9.719286,19.7735 -10.888983,30.423298 -0.377503,3.437063 -0.377238,11.289093 4.79e-4,14.520221 1.333709,11.408719 5.136761,21.844829 11.378568,31.224379 0.953977,1.43354 1.689146,2.63802 1.633708,2.67663 -0.05543,0.0386 -0.819754,0.28392 -1.698495,0.54514 -4.047052,1.20307 -8.905657,4.28314 -12.195785,7.73142 l -1.544387,1.61862 0.14415,-1.46457 z" id="path3763" style="fill:#ffffff;fill-opacity:1;stroke:#ffffff;stroke-width:1;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;stroke-dashoffset:0" /> </g> </svg>'

//----------------------- later wordt dit klasse Table --------------------



function Table(numChairs){
    this.numChairs = numChairs;
    this.radius = 250*this.numChairs/12;
    this.listOfChairs = [];
    this.listOfNames = [];
    this.group = null;
}

//static variables
Table.numTables = 0;
Table.listOfTables = [];

Table.prototype.drawTable = function(SVG){
    //SVG is an SVG object of the svg.js library and is the canvas where the table will be drawn on
    Table.numTables += 1;
    this.table = SVG.circle(this.radius*2).fill('none').stroke({width:10}).cx(0).cy(0);
    var group = SVG.group();
    var scaleF = 3;
    group.add(this.table);
    //put chairs around the table
    for (i=0;i<this.numChairs;i++){
	this.listOfChairs[i] = SVG.svg(rawChair);
	this.listOfNames[i] = SVG.text("free seat!").font({
	    family:   ' arsenalwhite',
	    size:     51,
	    anchor:'middle',
	}).addClass('noselect; text')
	this.listOfNames[i].cy(((360/this.numChairs*i>90 && 360/this.numChairs*i<=270)?-(this.listOfChairs[i].get('zitje').cy()/scaleF+2.5):this.listOfChairs[i].get('zitje').cy()/scaleF-2.5))
	this.table.transform({
	    x:this.listOfChairs[i].get('zitje').cx(),
	    y:this.listOfChairs[i].get('zitje').cy(),
	    });
	this.listOfChairs[i].get('stoel').transform({
	    cx:this.listOfChairs[i].get('zitje').cx(),
	    cy:this.listOfChairs[i].get('zitje').cy(),
	    rotation:360/this.numChairs*i,
	    x:-this.radius-this.listOfChairs[i].get('zitje').width()*0.7,
	    });
	group.add(this.listOfChairs[i].get('stoel'));
	group.add(this.listOfNames[i]);
	this.listOfNames[i].transform({
	    cx:this.listOfChairs[i].get('zitje').cx(),
	    cy:this.listOfChairs[i].get('zitje').cy(),
	    rotation:360/this.numChairs*i,
	    x:-this.radius-this.listOfChairs[i].get('zitje').width()*2-this.listOfNames[i].bbox().width*0.7,
	    scaleY:((360/this.numChairs*i>90 && 360/this.numChairs*i<=270)?-scaleF:scaleF),
	    scaleX:((360/this.numChairs*i>90 && 360/this.numChairs*i<=270)?-scaleF:scaleF),
	    });
	this.listOfNames[i].style('opacity:0')
	this.listOfChairs[i].get('stoel').front()
    };
    //make tables with more chairs larger
    group.scale(0.3+0.001*this.numChairs)
    this.group = group
    Table.listOfTables.push(group);
    return group;
};

Table.prototype.setSeatColor = function(chairnumber, color){
    this.listOfChairs[chairnumber].get('zitje').style('fill:'+color)
    //this.table.attr({fill:'#f03'}) 
}

Table.prototype.animateChairs = function(){

    var that = this; //to pass the table object to the anonymous function

    var mouseover = function(){
	for (i=0; i<that.numChairs; i++){
	    that.listOfChairs[i].get('stoel').animate(300,'<',0).x(-that.radius-90)
    	    that.listOfChairs[i].get('stoel').children()[0].style('fill:#ffffff')
    	    that.listOfNames[i].animate(300,'<',0).style('opacity:0')
    	}	
	this.children()[0].style('fill:#000000')
	this.animate(300,'>',0).x(-that.radius-120).after(function(){
	that.listOfNames[(that.group.children().indexOf(this)-2)/2].animate(300,'<',0).style('opacity:1')
	})
    };

    for (i=0;i<this.numChairs;i++) {
	this.listOfChairs[i].get('stoel').on('mouseover',mouseover)
	this.listOfChairs[i].get('stoel').on('touchstart',mouseover)
    }
}

//--------------------------------------------------------------------------


//var draw = SVG('div').size('100%','100%')
//var tafel = new Table(2)
//tafel.drawTable(draw)
//tafel.animateChairs();
//var chair = draw.svg(rawChair)
//var chair2 = draw.svg(rawChair)
//
//chair.get('stoel').rotate(50, chair.get('zitje').cx(), chair.get('zitje').cy())
//chair.get('stoel').translate(500,0)
