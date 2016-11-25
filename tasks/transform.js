/*var gulp = require('gulp');
var babelify = require('babelify');
var browserify = require('browserify')
var gulpBrowser = require('gulp-browser');
var size = require('gulp-size');

gulp.task('transform', function () {
  var stream = gulp.src('./apps/static/scripts/jsx/*.js')
    .pipe(gulpBrowser.browserify({transform: ['babelify']}))
    .pipe(gulp.dest('./apps/static/scripts/js/'))
    .pipe(size());
  return stream;
});

*/
