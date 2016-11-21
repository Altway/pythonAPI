var del = require('del');
var gulp = require('gulp');

gulp.task('del', function () {
  return del(['./apps/static/scripts/js']);
});

