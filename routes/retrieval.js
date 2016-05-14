var pgp = require('pg-promise')();
var router = require('koa-router')();
var PythonShell = require('python-shell');

PythonShell.run('assets/py/data.py', function (err) {
	if (err) throw err;
	console.log('finished');
});

module.exports = router;
