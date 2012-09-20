
all:: all_tests pep

pep::
	pep8 yampress/yampress.py
	pep8 test/__init__.py

all_tests::
	nosetests

json_tests::
	nosetests -x test/auto_test.py

coverage::
	$(RM) -r coverage
	nosetests --with-coverage --cover-html --cover-html-dir=coverage --cover-package=yampress test/auto_test.py

clean:
	find . -name "*~" -exec ${RM} {} \;
	find . -name "*.pyc" -exec ${RM} {} \;
	${RM} tests/auto_test.py
