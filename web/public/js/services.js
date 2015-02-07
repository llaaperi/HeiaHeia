'use strict';

angular.module('myApp.services', [])
	

.factory('ApiService', function($http){

	return{

		getWarriors: function(callback){
			$http.get('api/getWarriors').success(callback);
		},

		getWorkouts: function(id, callback){
			$http.get("api/getWorkouts?id="+id).success(callback);
		}
	};

});
