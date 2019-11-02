import functools
import json
import os
import sqlite3


connections = {}  # connections[ 'file.db' ] = connection


def read_db( url, sql=None, table=None, where=None, params=None, cls=None, *args, **kwargs ):
    # connection
    connection = connections.get( url, None )

    if connection is None:
        connection = sqlite3.connect( url )
        connections[ url ] = connection

    # table
    if table is None:
        filename, file_extension = os.path.splitext( os.path.basename( url ) )
        table = filename

    # sql
    if sql is None:
        sql = f"SELECT * FROM {table}"

    if where is not None:
        sql = f"{sql} WHERE {where}"

    #
    if params is None:
        params = args

    # execute
    cursor = connection.cursor()
    query_result = cursor.execute( sql, params )

    # convert result to object | list | dict | ...
    if cls is None:
        result = query_result

    elif cls is tuple:
        result = query_result

    elif cls is list:
        result = query_result

    elif cls is dict:
        def convert_to_dict( fields, row ):
            return dict( zip( fields, row ) )

        fields = [ x[0] for x in query_result.description ]
        fn = functools.partial( convert_to_dict, fields )

        result = map( fn, query_result )

    else: # cls is class
        def convert_to_cls( cls, fields, row ):
            # str -> str
            #     -> []
            #     -> {}
            # int -> int
            # nul -> str
            #     -> []
            #     -> {}
            #     -> int
            # depends of cls.attr type

            o = cls()

            for field, value in zip( fields, row ):
                a = getattr( o, field )

                if value is None:
                    pass
                else:
                    if isinstance( a, list ):
                        setattr( o, field, json.loads( value ) )

                    elif isinstance( a, dict ):
                        setattr( o, field, json.loads( value ) )

                    else:
                        setattr( o, field, value )

            return o

        fields = [ x[0] for x in query_result.description ]
        fn = functools.partial( convert_to_cls, cls, fields )

        result = map( fn, query_result )

    return result
