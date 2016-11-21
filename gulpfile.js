// requirements
require('require-dir')('./tasks', {recurse: false});
var gulp = require('gulp');

// tasks
gulp.task('default', ['del'], function() {
  gulp.start('transform');
  gulp.watch('./apps/static/scripts/jsx/*.js', ['transform']);
});

