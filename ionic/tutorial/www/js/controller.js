angular.module('tutorial')
 
  .controller('AppCtrl', function() {})
  .controller('LoginCtrl', function() {})
  .controller('DashCtrl', function($scope) {
    console.log(Table.numTables)
    $scope.table = {}
    $scope.table.numTables = function(){return Table.numTables}
  })
  .controller('TableCtrl', function(){
    var draw = SVG('container').size('100%','100%')
    var tafel = new Table(20)
    var group = tafel.drawTable(draw)
    tafel.animateChairs();
    group.move(200,200);
    var tafel2 = new Table(2)
    group = tafel2.drawTable(draw)
    tafel2.animateChairs();
    group.move(1000,2000)
    var tafel3 = new Table(7)
    group = tafel3.drawTable(draw)
    tafel3.animateChairs();
    group.move(4000,2500)
    var tableList = [];
    for (var i=0; i<20; i++) {
	tableList.push(new Table(i*2));
	group = tableList[i].drawTable(draw);
	tableList[i].animateChairs();
	group.move(200*i,200*i)	
    }
  });

