# -*- coding: utf-8 -*-
from __future__ import absolute_import


class DummyConnection(object):
    """
    Dummy connection, used in representation and stringification of instances
    """

    def quote_identifier(self, identifier):
        """
        Dummy connection does not quote identifiers
        """
        if hasattr(identifier, '_as_sql'):
            sql, args = identifier._as_sql(self, {})
            assert not len(args), 'Identifier cannot contain query parameters'
            return sql
        return identifier

    # Function names quoted as generic identifiers
    quote_function_name = quote_identifier

    def operator_to_sql(self, op, left, right=None, context=None):
        """
        Dummy connection overrides no operators
        """
        return NotImplemented

dummy_connection = DummyConnection()


class DummyContext(object):
    """
    Dummy context, used in representation and stringification of instances
    """

    def __getitem__(self, name):
        return DummyVariable(name)

dummy_context = DummyContext()


class DummyVariable(object):
    """
    Dummy variable, renders itself as literal '$name'
    """

    def __init__(self, name):
        self.name = name

    def _as_sql(self, connection, context):
        return u'${name}'.format(name=self.name), ()