from pyramid.config import Configurator
from dins.data.db_session import DbSession
import os


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_chameleon')
        config.include('.routes')
        init_db(config)
        config.scan()
    return config.make_wsgi_app()

def init_db(_):
    db_file = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            'db',
            'dins.sqlite'
        )
    )
    DbSession.global_init(db_file)
