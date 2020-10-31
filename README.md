# Pytest Test Suite
1. Install [pipenv](https://pipenv.readthedocs.io/en/latest/). 
```shell
pip install pipenv
```

2. Clone this repo for the code and change directory into the folder.

```shell
git clone https://github.com/tanyinghui/tdd-python.git

cd tdd-python/
```

3. After that, install [pytest](https://docs.pytest.org/en/stable/).
```shell
pipenv install --dev pytest
```

4. Run the test:
```shell
pipenv run pytest
```

## Steps
1. Write a test, watch it fail
2. Write just enough code to pass the test
3. Improve code without changing its behavior
4. Repeat 1-3

## TDD Rules
1. **Start with a test**: only start writing production code when your automated test has failed.
2. **Baby steps**: Only 1 failing test at a time
3. **Baby tests**: Write small test only.
4. **Keep your code DRY**: Write enough production code to make the failing test pass. No extra code.
5. **Baby steps**: Implement simplest algorithm first, then generate it later when you identify some patterns.
6. Refactor your codes.
7. Refactor your tests too!
8. Don't refactr when your tests are failing. Make tests pass first.


## References:
[1] https://github.com/davified/clean-code-ml
[2] https://github.com/JuniorDevSingapore/coding_dojo
[3] https://refactoring.guru/refactoring 