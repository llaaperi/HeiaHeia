'use strict';

/* Controllers */

angular.module('myApp.controllers', [])
	.controller('WarriorCtrl', ['$scope', 'ApiService', function ($scope, ApiService){

	$scope.warriors = [];
	console.log("Init warrior controller");
	ApiService.getWarriors(function(warriors){
		console.log("Get warriors");
		//console.log(warriors);
		$scope.warriors = warriors;
		update_chart();
	});

	$scope.data={
		labels: [],
		datasets:[
			{
				label: 'Hours',
				fillColor: "rgba(151,187,205,0.5)",
           		strokeColor: "rgba(151,187,205,0.8)",
            	highlightFill: "rgba(151,187,205,0.75)",
            	highlightStroke: "rgba(151,187,205,1)",
            	data: []
			}
		]
	};

	function update_chart(){
		$scope.data.labels = []
		$scope.data.datasets[0].data = []
		for (var i = 0; i < $scope.warriors.length; i++){
			var warrior = $scope.warriors[i];
			$scope.data.labels.push(warrior.name)
			var hours = 0;
			for (var j = 0; j < warrior.workouts.length; j++){
				var workout = warrior.workouts[j];
				hours += workout.duration;
			}
			hours /= 3600;//Seconds to hours
			$scope.data.datasets[0].data.push(hours)
		}
		console.log($scope.data);

		var ctx = document.getElementById("hourChart").getContext("2d");
		var hourChart = new Chart(ctx).Bar($scope.data, {});
	};
}]);