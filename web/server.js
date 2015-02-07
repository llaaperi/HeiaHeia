var Sequelize = require('sequelize');
var express = require('express');
var http = require('http');

var router = express.Router();

var app = express();

require('./routes/index')(app);
require('./routes/api')(app, Sequelize);

app.set('views',__dirname+'/views');
app.use(express.static(__dirname+'/public'));

app.set('view engine', 'ejs');
app.engine('html', require('ejs').renderFile);

//START SERVER
var server = app.listen(8888, function(){
	console.log("Server running on port 8888")
});
