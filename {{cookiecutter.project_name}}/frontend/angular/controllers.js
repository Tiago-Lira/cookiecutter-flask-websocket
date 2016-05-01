(function (angular) {

    'use strict';

    angular.module('{{cookiecutter.project_name}}')

        .controller('IndexCtrl', [
            'notify',

            function (notify) {

                //////////////////////////////////////////////
                // CONFIG
                //////////////////////////////////////////////

                var self = this;

                notify.config({
                    duration: 4000,
                    startTop: 60,
                    maximumOpen: 1,
                });

                //////////////////////////////////////////////
                // PUBLIC API
                //////////////////////////////////////////////

                self.count = 0;

                self.add = function () {
                    self.count += 1;
                };

                //////////////////////////////////////////////
                // PRIVATE METHODS
                //////////////////////////////////////////////

                function notifyAdd () {
                    notify({
                        message: 'Added one',
                        classes: 'alert-info',
                        duration: 4000,
                    });
                }

            }]);

})(angular);
