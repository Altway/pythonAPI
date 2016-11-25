var gulp = require('gulp');
var babelify = require('babelify');
var babel = require('gulp-babel')
var browserify = require('browserify')
var gulpBrowser = require('gulp-browser');
var size = require('gulp-size');
var sourcemaps = require('gulp-sourcemaps');
//gulp.task('transform', function () {
//  var stream = gulp.src('./apps/static/scripts/jsx/*.js')
//    .pipe(gulpBrowser.browserify({transform: ['babelify']}))
//    .pipe(gulp.dest('./apps/static/scripts/js/'))
//    .pipe(size());
//  return stream;
//});

// Concatenate jsFiles.vendor and jsFiles.source into one JS file.
// Run copy-react and eslint before concatenating
gulp.task('compile', function() {
  return gulp.src('./apps/static/scripts/jsx/*.js')
    .pipe(sourcemaps.init())
    .pipe(babel({
	presets: ['es2015']
    }))
    .pipe(sourcemaps.write('./'))
    .pipe(gulp.dest('./apps/static/scripts/js/'))
    .pipe(size());
});
