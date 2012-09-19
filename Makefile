
all:: all_tests

all_tests::
	nosetests

json_tests::
	nosetests -x tests/auto_test.py

clean:
	find . -name "*~" -exec ${RM} {} \;
	find . -name "*.pyc" -exec ${RM} {} \;
	${RM} tests/auto_test.py