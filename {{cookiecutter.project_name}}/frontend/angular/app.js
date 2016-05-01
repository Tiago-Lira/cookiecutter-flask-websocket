(function (angular) {

    'use strict';

    angular.module('{{cookiecutter.project_name}}', [
        'ui.router',
        'ngMask',
        'cgNotify',
        'ui.bootstrap',
        'angularMoment',
        '{{cookiecutter.project_name}}-templates',
    ]);

})(angular);
