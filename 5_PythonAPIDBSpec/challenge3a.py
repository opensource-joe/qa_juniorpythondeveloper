###############################################################################
# SQLAlchemy Core - API v2
###############################################################################
import sqlalchemy
from sqlalchemy import create_engine, text

# Complete the following function.
def post_count_for_user(engine: sqlalchemy.engine.Engine, reference: str) -> int:
    ''' post_count_for_user returns the value of the postcount column for the row containing the specified reference.

        1.) Establish a connection to the database using the provided engine. 
        2.) Select the postcount column where the reference argument matches the reference column.
        3.) Return the selected result as an int.

        Database Schema:
            CREATE TABLE user (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                full_name TEXT, 
                reference TEXT,
                postcount INTEGER
            );

        Example Data:
            { "full_name": "a", "reference": "@a", "postcount": 2_000 },
            { "full_name": "b", "reference": "@b", "postcount": 1_000 }
        
        Example function usage:
        >>> engine = create_engine("sqlite+pysqlite:///:memory:", future=True)
        >>> post_count_for_user(engine, '@a')
        2000
    '''
    with engine.connect() as conn:
        result = conn.execute(text("SELECT postcount FROM user WHERE reference = :ref"), {"ref": reference})
        row = result.fetchone()
        return int(row[0]) if row else 0


###############################################################################
# SQLAlchemy ORM - API v2
###############################################################################
from sqlalchemy import (Column, ForeignKey, Integer, String, create_engine, select)
from sqlalchemy.orm import Session, declarative_base, relationship

def declarative_base_repr(self):
    ''' A helper function used to generate a __repr__ used to create an instance of the given model. 

        This is included to make caveman (print-based) debugging easier.

        Examples:

        • User(locator=1, full_name='a', reference='@a')
        • Post(locator=1, content='o', user_locator=1)
    '''
    kwargs = ', '.join(
        [f'{col.name}={getattr(self, col.name)!r}' for col in self.__table__.columns]
    )
    return f'{self.__class__.__name__}({kwargs})' 


###############################################################################
Base = declarative_base()
# Use the declarative_base_repr function as the __repr__ for all subclasses.
Base.__repr__ = declarative_base_repr
###############################################################################
class User(Base):
    __tablename__ = 'user'

    locator     = Column(Integer, primary_key=True)
    full_name   = Column(String(60))
    reference   = Column(String(60), unique=True)
    posts       = relationship('Post', back_populates='user')

class Post(Base):
    __tablename__ = 'post'

    locator         = Column(Integer, primary_key=True)
    content         = Column(String)
    user_locator    = Column(Integer, ForeignKey("user.locator"), nullable=False)
    user            = relationship('User', back_populates='posts')

###############################################################################
# Complete the following function.
def add_orm_user(engine: sqlalchemy.engine.Engine, full_name: str, reference: str, posts: list[str]) -> int:
    ''' add_orm_user adds a User record to the database and returns the User.locator.

        1.) Establish a connection to the database using the provided engine. 
        2.) Create a User record using the provided arguments and persist the changes. 
        3.) Return the newly created user's locator as an int.

        Example function usage:
        >>> engine = create_engine("sqlite+pysqlite:///:memory:", future=True)
        >>> Base.metadata.create_all(engine) 
        >>> add_orm_user(engine, 'a', '@a', 'x y z'.split())
        1

    '''
    with Session(engine) as session:
        user = User(full_name=full_name, reference=reference)
        session.add(user)
        session.flush()  # Assigns locator
        for content in posts:
            post = Post(content=content, user_locator=user.locator)
            session.add(post)
        session.commit()
        return user.locator


# Complete the following function.
def posts_for_user(engine: sqlalchemy.engine.Engine, reference: str) -> list[Post]:
    ''' posts_for_user returns all Post records for a given user.

        1.) Establish a connection to the database using the provided engine. 
        2.) Select all Post objects related to the user with the provided reference.
        3.) Return the selected result as a list of Post objects.

        Example function usage:
        >>> engine = create_engine("sqlite+pysqlite:///:memory:", future=True)
        >>> Base.metadata.create_all(engine)
        >>> add_orm_user(engine, 'z', '@z', 'a b c'.split())
        1
        >>> posts_for_user(engine, '@z')
        [Post(locator=1, content='a', user_locator=1), Post(locator=2, content='b', user_locator=1), Post(locator=3, content='c', user_locator=1)]

    '''
    with Session(engine) as session:
        user = session.execute(select(User).where(User.reference == reference)).scalar_one_or_none()
        if not user:
            return []
        posts = session.execute(select(Post).where(Post.user_locator == user.locator)).scalars().all()
        return posts


def test_engine():
    ''' Returns a SQLAlchemy engine used to establish a database connection to a pre-created database file. 
        Use this engine to assist while developing, if needed.

        Example:

        >>> engine = test_engine()
        >>> print(posts_for_user(engine, '@a'))

    '''
    engine = create_engine("sqlite+pysqlite:///debug_databases/orm.sqlite3", future=True)
    Base.metadata.create_all(engine)
    return engine


if __name__ == '__main__':
    engine = test_engine()
    # Optional debug code here...
    # Example: 
    # print(posts_for_user(engine, '@def'))