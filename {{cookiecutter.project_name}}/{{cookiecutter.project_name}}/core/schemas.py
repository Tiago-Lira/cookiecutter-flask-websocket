# -*- coding: utf-8 -*-

from marshmallow import Schema
from marshmallow import fields
from marshmallow import post_load
from marshmallow_mongoengine import ModelSchema

from {{cookiecutter.project_name}}.core.documents import Example


class QueryMixin(object):

    def query(self, **kwargs):
        if self.many:
            return self.Meta.model.objects.filter(**kwargs)
        else:
            return self.Meta.model.objects.filter(**kwargs).first()


class ExampleSchema(QueryMixin, ModelSchema):

    class Meta:
        fields = ('name',)
