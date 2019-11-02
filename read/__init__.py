from .read import read_str
from .read import read_class


#def Read( url, readers=None, encoding='UTF-8', streaming=False, caching=False, *args, **kwargs ):
def Read( url, *args, **kwargs ):
    """
    Read data source. See examples below.

    Args:
        url:
        readers:
        encoding:
        streaming:
        caching:

    Returns:
        Range

    ::

        # 1
        Read( 'dump.xml.bz2' )

        # 2
        Read( 'dump.xml' )

        # 3
        Read( 'dump.txt' )

        # 4
        Read( 'dump.ini' )

        # 5
        Read( 'dump.json' )

        # 6
        Read( 'dump.json.bz2' )

        # 7
        Read( 'http://api.ixioo.com/PKS_Match' )

        # 8
        Read( 'words.db' )

        # 9
        Read( 'words.sqlite' )

        # 10
        Read( 'words.db', table="words" )

        # 11
        Read( 'words.db', table="words", where="LabelName = ? ", "Cat" )

        # 12
        Read( 'words.db', sql="SELECT * FROM words WHERE LabelName = ? ", "Cat" )
        Read( 'words.db', sql="SELECT * FROM words WHERE LabelName = ? ", params=["Cat"] )

        # 13
        Read( 'words.db', table="words", cls=WordItem )

        # 14
        class WordItem:
            _database = 'words.db'
            _table = 'words'

            def __init( self ):
                self.PK = ""
                self.LabelName = ""

        Read( WordItem )

        # 15
        Read( WordItem, sql="SELECT * FROM words WHERE LabelName = ? ", "Cat" )

        # 16
        DBWORDS = 'words.db'
        Read( DBWORDS, "SELECT * FROM words WHERE LabelName = ? ", "Cat" )

        # 17
        for w in Read( DBWORDS ):
            print( w )

        # 18
        Read( DBWORDS ).map( ... ).write( DBWORDS )

        # 19
        Read( "SELECT * FROM words WHERE LabelName = ? ", "Cat" ).as_object( WordItem )
        Read( "SELECT * FROM words WHERE LabelName = ? ", "Cat" ).as_dict()
        Read( "SELECT * FROM words WHERE LabelName = ? ", "Cat" ).as_list()
        Read( "SELECT * FROM words WHERE LabelName = ? ", "Cat" ).as_tuple()

    """
    if isinstance( url, str ):
        return read_str( url, *args, **kwargs )

    elif isinstance( url, object ):
        return read_class( url, *args, **kwargs )
