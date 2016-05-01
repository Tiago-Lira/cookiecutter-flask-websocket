
run:
	@python runserver.py

kill:
	@sudo fuser -k 8000/tcp

celery:
	@celery -A {{cookiecutter.project_name}}:celery worker -l DEBUG

test: test.debug clean

coverage: coverage.debug clean

test.debug:
	@py.test -s

test.scalable:
	@py.test -n 2

coverage.debug:
	@py.test -s --cov-report=html --no-cov-on-fail
	@gnome-open coverage_report/index.html

coverage.scalable:
	@py.test --cov-report=html --no-cov-on-fail -n 2
	@gnome-open coverage_report/index.html

clean:
	@find . -name '.coverage' -exec rm -f {} +
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.coverage' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +
	@find . -name '*__pycache__' -exec rm -fr {} +
	@find . -name '.cache' -exec rm -fr {} +
	@find . -name '.eggs' -exec rm -fr {} +
	@find . -name '*.egg-info' -exec rm -fr {} +
	@find . -name 'coverage_report' -exec rm -fr {} +
