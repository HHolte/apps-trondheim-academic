import pytest
import sqlite3
import os
from code_db import write_to_db

@pytest.fixture
def demo_fixture():
    print('\nBefore')

    demo = 'demo'

    yield demo

    print(f'\nAfter {demo}\n\n')

def test_wite_to_db(demo_fixture):
    write_ok = write_to_db()

    assert write_ok

