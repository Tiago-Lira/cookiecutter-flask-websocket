
////////////////////////////////////
// Dependencies
/////////////////////////////////////

var gulp = require('gulp');
var scss = require('gulp-sass');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');
var bower = require('gulp-bower');
var html2js = require('gulp-html2js');
var cssmin = require('gulp-cssmin');
var order = require("gulp-order");
var notify = require('gulp-notify');
var gutil = require('gulp-util');
var path = require('path');



/////////////////////////////////////
// Path constants
/////////////////////////////////////

var BUILD_DIR = path.join(__dirname, './vendor');
var JS_DIR = path.join(BUILD_DIR, 'js');
var CSS_DIR = path.join(BUILD_DIR, 'css');

var SOURCES = {
    js: 'angular/**/*.js',
    scss: 'scss/app.scss',
    css: path.join(CSS_DIR, 'app.css'),
    templates: 'angular/**/*.html',
};

var WATCH = {
    js: SOURCES.js,
    scss: ['scss/**/*.scss', 'scss/*.scss'],
    templates: SOURCES.templates,
};



/////////////////////////////////////
// Main tasks
/////////////////////////////////////

gulp.task('dev', [
    'bower',
    'scripts:dev',
    'styles',
]);

gulp.task('prod', [
    'bower',
    'scripts',
    'styles',
]);

gulp.task('styles', [
    'styles:scss',
    'styles:minify'
]);

gulp.task('scripts', [
    'scripts:concat',
    'scripts:templates',
    'scripts:minify'
]);

gulp.task('scripts:dev', [
    'scripts:concat',
    'scripts:templates'
]);

gulp.task('watch', function() {
    gulp.watch(WATCH.js, ['scripts:dev']);
    gulp.watch(['angular/views/**/*.html', 'angular/views/*.html'], ['scripts:templates']);
    gulp.watch(WATCH.scss, ['styles:scss', 'styles:minify']);
});

gulp.task('bower', function() {
  return bower({interactive: true});
});



/////////////////////////////////////
// TASKS
/////////////////////////////////////


gulp.task('styles:scss', function () {
    return gulp.src(SOURCES.scss)
        .pipe(scss())
        .pipe(gulp.dest(CSS_DIR));
});


gulp.task('styles:minify', ['styles:scss'], function () {
    gulp.src(SOURCES.css)
        .pipe(cssmin({keepSpecialComments: 1}))
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest(CSS_DIR));
});


gulp.task('scripts:concat', ['scripts:templates'], function() {
    return gulp.src(SOURCES.js)
        .pipe(order([
            'templates.js',
            'app.js',
            'routes.js',
            'services.js',
            '**/*.js',
            '**/**/*.js',
        ]))
        .pipe(concat('app.js'))
        .pipe(gulp.dest(JS_DIR));
});


gulp.task('scripts:templates', function () {
    gulp.src(SOURCES.templates)
        .pipe(html2js('templates.js', {
            adapter: 'angular',
            base: 'templates',
            name: '{{cookiecutter.project_name}}-templates',
        }))
        .pipe(gulp.dest('angular'));
});


gulp.task('scripts:minify', ['scripts:concat'], function () {
    return gulp.src(path.join(JS_DIR, 'app.js'))
        .pipe(uglify().on('error', gutil.log))
        .pipe(gulp.dest(JS_DIR));
});
