var gulp = require('gulp');
var sass = require('gulp-sass');
var sourcemaps = require('gulp-sourcemaps');
var autoprefixer = require('gulp-autoprefixer');

gulp.task('styles', function() {
    gulp.src('templates/styles.scss')
    	// .pipe (sourcemaps.init())
        .pipe(sass().on('error', sass.logError))
        // .pipe(sourcemaps.write())
    	.pipe(autoprefixer())
        .pipe(gulp.dest('static/css/'))
});

//Watch task
gulp.task('default',function() {
    gulp.watch('templates/styles.scss',['styles']);
});