# -*- coding: utf-8 -*-
# pylint: disable=C0301,W0105,W0401,W0614

from tarantool.lts.connection import Connection
from tarantool.lts.const import (
    SOCKET_TIMEOUT,
    RECONNECT_MAX_ATTEMPTS,
    RECONNECT_DELAY
)

from tarantool.lts.schema import (
    Schema,
    RAW,
    STR,
    NUM,
    NUM64
)
from tarantool.lts.error import (
    Error,
    DatabaseError,
    NetworkError,
    NetworkWarning,
    RetryWarning
)


def connect(host="localhost", port=33013, schema=None, return_tuple=True):
    '''\
    Create a connection to the Tarantool server.

    :param str host: Server hostname or IP-address
    :param int port: Server port
    :param schema: Data schema (see Developer guide
        and :class:`~tarantool.lts.schema.Schema`)
    :type schema: :class:`~tarantool.lts.schema.Schema` or dict
    :param bool return_tuple: Return tuple by default, in update/delete/insert operations.

    :rtype: :class:`~tarantool.lts.connection.Connection`
    :raise: `NetworkError`
    '''

    return Connection(host, port,
                      socket_timeout=SOCKET_TIMEOUT,
                      reconnect_max_attempts=RECONNECT_MAX_ATTEMPTS,
                      reconnect_delay=RECONNECT_DELAY,
                      connect_now=True,
                      schema=schema,
                      return_tuple=return_tuple)

__all__ = ['connect', 'Connection', 'Schema', 'Error', 'DatabaseError',
           'NetworkError', 'NetworkWarning', 'RetryWarning', 'RAW', 'STR',
           'NUM', 'NUM64']