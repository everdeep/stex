var router = require('koa-router')();

router.get('/', function* () {

	this.status = 200;
	this.body = 'Hello from index';
});

router.get('/posts', function* () {

	var posts = yield db.many(`SELECT * FROM announcements`);

	yield this.render('posts', {
		posts: posts,
	});
});


router.get('/posts/:id', function* () {

	var id = this.params.id;

	try {
		var post = yield db.one(`SELECT * FROM announcements WHERE id = $1`, [id]);

		yield this.render('post', {
			post: post,
		});
	} catch (e) {
		this.status = 404;
		this.body = 'Not Found';
	}
});

router.get('/posts/posts_all', function* () {

	var id = this.params.id;

	try {
		var post = yield db.one(`SELECT * FROM posts WHERE id = $1`, [id]);

		yield this.render('post', {
			post: post,
		});
	} catch (e) {
		this.status = 404;
		this.body = 'Not Found';
	}
});

router.get('/api/posts/:id', function* () {

	var id = this.params.id;

	try {
		var post = yield db.many(`SELECT * FROM posts WHERE id = $1`, [id]);
		yield this.render('post', {
			post: post
		});
	} catch (e) {
		this.status = 404;
		this.body = 'Not Found';
	}
});

router.get('/api/posts', function* () {

	var posts = yield db.many(`SELECT * FROM posts`);

	this.status = 200;
	this.body = {
		posts: posts
	};
});

router.post('/post', function* () {

	var title = this.request.body.title || 'Untitled';
	var content = this.request.body.content || '...';

	var post = yield db.one(`
		INSERT INTO posts(title, content)
		VALUES ($1, $2) RETURNING *`, [title, content]);

	this.status = 201;
	this.body = {
		post: post
	};
});

module.exports = router;
