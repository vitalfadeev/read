def read_str( url, *args, **kwargs ):
    url_upper = url.upper()

    if url_upper.startswith( "SELECT "):
        from .str.sql import read_sql
        return read_sql( url, *args, **kwargs )

    elif url_upper.startswith( "HTTP://" ):
        from .str.http import read_http
        return read_http( url, *args, **kwargs )

    elif url_upper.startswith( "HTTPS://" ):
        from .str.http import read_http
        return read_http( url, *args, **kwargs )

    elif url_upper.endswith( ".DB" ):
        from .str.db import read_db
        return read_db( url, *args, **kwargs )

    else:
        from .str.other import read_str_other
        return read_str_other( url, *args, **kwargs )



def read_class( cls, *args, **kwargs ):
    if hasattr( cls, "_database" ):
        database = cls._database
    else:
        database = f"{cls.__name__}.db"

    if hasattr( cls, "_table" ):
        table = cls._table
    elif "table" in kwargs:
        table = kwargs[ "table" ]
    else:
        table = cls.__name__

    #
    from .str.db import read_db
    return read_db( database, table=table, *args, **kwargs )
