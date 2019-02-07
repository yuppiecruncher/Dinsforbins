import sqlalchemy
import sqlalchemy.orm
from dins.data.modelbase import SqlAlchemyBase
import dins.data.__all_models

class DbSession:
    factory = None
    engine = None

    @staticmethod
    def global_init(db_file: str):
        if DbSession.factory:
            return

        if not db_file or not  db_file.strip():
            raise Exception("You must specify a data file.")
        conn_str = 'sqlite:///'+db_file

        #connect_args={'check_same_thread':False} --fixed errors for thread handling in sqlite

        engine = sqlalchemy.create_engine(conn_str, connect_args={'check_same_thread':False}, echo=False)
        DbSession.engine = engine
        DbSession.factory = sqlalchemy.orm.sessionmaker(bind=engine)

        SqlAlchemyBase.metadata.create_all(engine)
