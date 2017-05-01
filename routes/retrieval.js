var pgp = require('pg-promise')();
var router = require('koa-router')();
var PythonShell = require('python-shell');

// Helper for linking to external query files:
function sql(file) {
	return new pgp.QueryFile(file, {minify: true});
}

// Create QueryFile globally, once per file:
var sqlInsert = sql('./sql/inserts.sql');
/*
PythonShell.run('assets/py/data.py', function (err) {
	if (err) throw err;
	console.log('finished');

	db.one(sqlInsert)
		.then(function (data) {
			console.log(data); // display found audit records;
		})
		.catch(function (error) {
				console.log(error); // display the error;
		});
});*/



module.exports = router;
