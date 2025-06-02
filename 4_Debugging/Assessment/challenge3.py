import itertools
import os
import sqlite3
import time
import unittest
from collections import defaultdict

from faker import Faker
from rich.console import Console
from rich.prompt import Confirm, Prompt
from rich.table import Table

###############################################################################
# Database generation code.
fake = Faker()


def create_db(filename='databases/db.sqlite3'):
    dbconn = sqlite3.connect(filename)
    cursor = dbconn.cursor()
    schema = [
        '''
            CREATE TABLE Record (
                ID          INTEGER PRIMARY KEY AUTOINCREMENT,
                Copy        TEXT        NOT NULL
            );
        ''',
        '''
            CREATE TABLE Tag (
                ID          INTEGER PRIMARY KEY AUTOINCREMENT,
                RecordID    INTEGER NOT NULL,
                Copy        TEXT NOT NULL, 
                FOREIGN KEY(RecordID) REFERENCES Record(ID)
            );
        '''
    ]


    with dbconn:
        # Create the database schema.
        for statement in schema:
            cursor.execute(statement)
        
        # Populate the database.
        cursor.executemany('INSERT INTO Record (Copy) VALUES (?);', [
            [fake.text()] for _ in range(100)
        ])
        
        tags = 'private public local'.split()
        cursor.executemany('INSERT INTO Tag (RecordID, Copy) VALUES (?, ?);', [
            [i, tags[i % 3]] for i in range(30)
        ])

        dbconn.commit()

# End DB generation
###############################################################################

class Record:
    def __init__(self, data, tags):
        self.data = data
        self.tags = tags

    def __repr__(self):
        return f'Record: {self.data} Tags: {self.tags}'


class Filter:
    def __init__(self, tag):
        self.tag = tag

    def found(self, record: Record):
        return self.tag in record.tags

    def not_found(self, record: Record):
        return not self.tag in record.tags

    def __repr__(self):
        return self.tag


def get_data(database):
    with sqlite3.connect(database) as dbconn:
        cursor = dbconn.cursor()
        cursor.execute('SELECT r.ID, r.Copy, t.Copy FROM Record as r INNER JOIN Tag as t on r.ID = t.RecordID ORDER BY r.ID;') 
        result = cursor.fetchall()
        records = defaultdict(list)
        
        for _id, grouping in itertools.groupby(result, key=lambda r: r[0]):
            for _, content, tag in grouping:
                records[content].append(tag)

        return [Record(content, tag) for content, tag in records.items()]


def build_filters(*filter_strings, filters: list[Filter]=[]) -> list[Filter]:
    for _filter in filter_strings:
        filters.append(Filter(_filter))
    return filters


def filter_data(records: list[Record], is_admin=False, exclusion_filters: list[str] = []) -> list[Record]:
    if not is_admin:
        exclusion_filters.append('private')

    for record in records:
        if any(f.found(record) for f in build_filters(*exclusion_filters)):
            continue
        yield record


def render():
    console = Console()
    while True:
        table = Table(title='Records', show_lines=True)
        table.add_column("Content", justify="left", style="cyan")
        table.add_column("Tags", justify="left", style="yellow")
        # Should private records be included in the results?
        admin = Confirm.ask('Show private records?')
        # Define any tags to be excluded.
        console.print('Exclude records by tag. Options: (private, public, local)')
        tags = Prompt.ask('Enter a comma separated list of tags to exclude: ')
        # normalize the tags.
        tags = tags.split(',')
        tags = [tag.strip() for tag in tags if tag]
        
        data = get_data('databases/db.sqlite3')
        data = filter_data(data, is_admin=admin, exclusion_filters=tags)
        
        for record in data:
            table.add_row(record.data, ' | '.join(record.tags))

        console.print(table)
        time.sleep(2.0)

def main():
    if not os.path.exists('./databases'):
        os.makedirs('./databases')
    
    if not os.path.exists('./databases/db.sqlite3'):
        create_db()
    
    render()

###############################################################################
#
# Application unit tests.  
# 
###############################################################################
class TestApplication(unittest.TestCase):

    def test_1_include_private_data(self):
        data = get_data('databases/db.sqlite3')
        data = filter_data(data, is_admin=True)
        assert any('private' in r.tags for r in data)


    def test_2_exclude_private_data(self):
        data = get_data('databases/db.sqlite3')
        data = filter_data(data, is_admin=False)
        assert any('private' not in r.tags for r in data)


    def test_3_multiple_exclusions(self):
        for is_admin in (True, False):
            data = get_data('databases/db.sqlite3')
            data = filter_data(data, is_admin=is_admin, exclusion_filters='local public'.split())
            if is_admin:
                assert all('private' in r.tags for r in data) 
            else:
                assert not list(data)

    def test_4_toggle_admin(self):
        for is_admin in (True, False, True):
            data = list(filter_data(get_data('databases/db.sqlite3'), is_admin=is_admin))
            if is_admin:
                if data:
                    assert any('private' in r.tags for r in data)
            else:
                if data:
                    assert any('private' not in r.tags for r in data)


if __name__ == '__main__':
    print(unittest.main(verbosity=1))
