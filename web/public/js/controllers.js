'use strict';

/* Controllers */

angular.module('myApp.controllers', ['chart.js'])
	.controller('WarriorCtrl', ['$scope', '$timeout', 'ApiService', function ($scope, $timeout, ApiService){

	$scope.warriors = [];
	console.log("Init warrior controller");
	ApiService.getWarriors(function(warriors){
		console.log("Get warriors");
		console.log(warriors);
		$scope.warriors = warriors;
		update_chart();
	});

	function update_chart(){
		var data = [];
		for (var i = 0; i < $scope.warriors.length; i++){
			var warrior = $scope.warriors[i];
			var hours = 0;
			for (var j = 0; j < warrior.workouts.length; j++){
				var workout = warrior.workouts[j];
				hours += workout.duration;
			}
			hours /= 3600;//Seconds to hours
			var warrior_data = {x:warrior.name,y:[hours]};
			data.push(warrior_data);
		}
		$scope.data1.data = data;
	};
	
	$scope.labels = ["January", "February", "March", "April", "May", "June", "July"];
  $scope.series = ['Series A', 'Series B'];
  $scope.data = [
    [65, 59, 80, 81, 56, 55, 40],
    [28, 48, 40, 19, 86, 27, 90]
  ];
  $scope.onClick = function (points, evt) {
    console.log(points, evt);
  };

  // Simulate async data update
  $timeout(function () {
    $scope.data = [
      [28, 48, 40, 19, 86, 27, 90],
      [65, 59, 80, 81, 56, 55, 40]
    ];
  }, 3000);

	$scope.data1 = {
		series: ['Hours'],
		data: []
	};

	$scope.chartType = 'bar';

	$scope.config1 = {
		labels: false,
		title: "Workout hours",
		legend: {
			display: false,
			position: 'left'
		},
		innerRadius: 0
	};

}]);