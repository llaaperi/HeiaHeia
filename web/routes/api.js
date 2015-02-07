
module.exports=function(app, Sequelize){

	var sequelize = new Sequelize("_databaseName_", "_username_", "_password_", {
		dialect: 'sqlite',
		storage: "../warrior.db",
		define:{
			timestamps: false
		}
	});

	var Warrior = sequelize.define('warriors',{
		name: Sequelize.STRING,
		rss_id: Sequelize.STRING
	});
	var Workout = sequelize.define('workouts',{
		sport: Sequelize.STRING,
		distance: Sequelize.FLOAT,
		duration: Sequelize.INTEGER,
		date: Sequelize.INTEGER
	});
	Warrior.hasMany(Workout, {foreignKey: 'warrior_id'});

	app.get('/api/getWarriors',function(req,res){
		Warrior.findAll({include:[Workout]})
		.complete(function(err, warriors){
			res.json(warriors);
		});
	});

	app.get('/api/getWorkouts', function(req,res){
		id = req.param('id');
		Workout.findAll({where: {warrior_id: id}})
		.complete(function(err, workouts){
			res.json(workouts);
		});
	});

}
