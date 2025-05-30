.PHONY: run clean

run:
	python3 -m venv .venv && \
	. .venv/bin/activate && \
	pip install -r requirements.txt && \
	python3 update_docs.py && \
	python3 update_navigation.py && \
	pytest ../test/test_metadata.py

clean:
	rm -rf docs