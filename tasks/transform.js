var gulp = require('gulp');
var reactify = require('reactify');
var gulpBrowser = require("gulp-browser");
var size = require('gulp-size');

gulp.task('transform', function () {
  var stream = gulp.src('./apps/static/scripts/jsx/*.js')
    .pipe(gulpBrowser.browserify({transform: ['reactify']}))
    .pipe(gulp.dest('./apps/static/scripts/js/'))
    .pipe(size());
  return stream;
});

