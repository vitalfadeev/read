import importlib
import io
import os
from urllib.parse import urlparse

from read.range import Range


def read_str_other( url, readers=None, encoding='UTF-8', streaming=False, caching=False, *args, **kwargs ):
    parsed = urlparse( url )
    scheme = parsed.scheme
    path = parsed.path

    # '' -> file
    if scheme == '':
        scheme = 'file'

    # package = '.readers.scheme'
    # scheme_module = importlib.import_module( scheme, package )
    #
    # with scheme_module.Reader() as scheme_reader:
    #     return scheme_reader

    classes = get_reader_class( url )

    f = io.FileIO( path )

    wf = wrap( f, url, classes )

    return Range( wf )


def wrap( f, url, classes ):
    if classes:
        cls = classes[0]

        wf = cls( f, url )

        return wrap( wf, url, classes[1:] )

    else:
        return f


def get_reader_class( url ):
    classes = []

    # next
    filename, file_extension = os.path.splitext( url )

    if file_extension:
        # find reader
        package = 'read.read.str.readers'
        reader_module_name = file_extension[1:] # remove dot. '.xml' -> 'xml'
        module = importlib.import_module( f"{package}.{reader_module_name}" )

        cls = module.Reader
        classes.append( cls )

        # recursive
        if filename:
            classes.extend( get_reader_class( filename ) )

    return classes
