(function (angular) {

    'use strict';

    var template_base = '../angular/views/';

    angular.module('{{cookiecutter.project_name}}').config([
        '$stateProvider',
        '$locationProvider',
        '$urlRouterProvider',

        function ($stateProvider, $locationProvider, $urlRouterProvider) {

            // Default url redirect
            $urlRouterProvider.otherwise('/');

            // Removing "#" from URL
            $locationProvider.html5Mode({
                enabled: true,
                requireBase: false,
            });

            // Mapping routes
            $stateProvider

                .state('index', {
                    url: '/',
                    templateUrl: template_base + 'index.html',
                    controller: 'IndexCtrl',
                    controllerAs: 'vm',
                });

        }]).run(function(amMoment) {
            amMoment.changeLocale('pt-br');
        });

})(angular);
