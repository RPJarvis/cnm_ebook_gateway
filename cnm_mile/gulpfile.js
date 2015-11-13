var gulp = require('gulp');
var sass = require('gulp-sass');

gulp.task('styles', function() {
    gulp.src('templates/styles.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('static/css/'))
});

//Watch task
gulp.task('default',function() {
    gulp.watch('templates/styles.scss',['styles']);
});