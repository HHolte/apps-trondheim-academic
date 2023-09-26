import pytest


@pytest.fixture
def fixture_demo():
    print('\nBefore')

    yield 'Result'

    print('\nAfter\n\n')


def test_example(fixture_demo):
    print(f'This is what I got: {fixture_demo}')

# 1. Skriv en fixture som fungerer
# 2. Parameteriser testen
# 3. Parameteriser fixturen i stedet!
# 4. Refaktorer og skriv om code.py så den tar inn en databasekobling
# 5. Lag en test som kjører database funksjonen og rydder opp etterpå
# 6. Gjør det med en fixture i stedet. Kanskje bruk en annen fixture først?
# 7. Parameteriser fixturen og gjør det to ganger med ulike filer?

@pytest.fixture(params=["p1", "p2"],)
def fixture_demo_2(fixture_demo, request):
    yield request.param

@pytest.mark.parametrize(
    "print_statement",
    [
        ("Hello"),
        ("World"),
        ("Bye")
    ]
)
def test_demo_2(fixture_demo_2, print_statement):
    print(fixture_demo_2, print_statement)

