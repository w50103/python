#!/usr/bin/env python3
# -*- coding: utf8 -*-


import logging

import aiomysql
import asyncio

def _log(sql, param =()):
    logging.info('SQL: %s' %sql)

@asyncio.coroutine
def create_pool(loop, **kw):
    logging.info('create databases connection pool...')
    global __pool

    __pool = yield from aiomysql.create_pool(
        host = kw.get('host', '127.0.0.1'),
        port = kw.get('port', 3306),
        user = kw.get('user'),
        password = kw.get('password'),
        db = kw.get('db'),
        charset = kw.get('charset','utf8'),
        autocommit = kw.get('autocommit',True),
        maxsize = kw.get('maxsize',10),
        minsize = kw.get('minsize',1),
        loop = loop
    )


@asyncio.coroutine
def select(sql, args, size=None):
    _log(sql, args)
    global __pool

    asyncio.async
    with __pool.get() as conn:
        asyncio.async
        with conn.cursor(aiomysql.DictCursor) as cur:
            asyncio.await
            cur.execute(sql.replace('?', '%s'),args, args or () )
        if size:
            rs = asyncio.await
            cur.fetchmany(size)

        else:
            rs = asyncio.await
            cur.fetchall()

        logging.info('rows returned: %s' % len(rs))

        return rs

@asyncio.coroutine
def execute(sql, args):
    _log(sql,args)
    with (yield from __pool) as conn:
        try:
            cur = yield from conn.cursor()
            yield  from cur.execute(sql.replace('?', '%s'), args)
            affected = cur.rowcount
            yield from cur.close()
        except BaseException as e:
            raise

        return affected




def create_args_string(num):
    L = []
    for n in range(num):
        L.append('?')

    return ','.join(L)

class Field(object):
    def __init__(self, name, column_type, primary_key, default):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = default

    def __str__(self):
        return '<%s, %s:%s>' % (self.__class__.__name__, self.column_type,self.name)


class StringField(Field):
    def __init__(self, name=None, primary_key=False, default=None, ddl='varchar(100)'):
        super().__init__(name, ddl, primary_key, default)

class BooleanField(Field):
    def __init__(self, name=None, default = False):
        super().__init__(name, 'boolean', False, default)

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')



### end coding

