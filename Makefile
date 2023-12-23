# Setup the Python Virtual Environment and source it
.PHONY: setup-venv

setup-venv:
	@echo "Setting up virtual environment..."
	@bash "scripts/setup_venv.sh"
	@echo "Virtual environment setup complete."


# Targets for creating new microservices
new-fastapi-%: setup-venv
	. .venv/bin/activate && python scripts/copy_fastapi_template.py "$*" -f

new-expressjs-%: setup-venv
	. .venv/bin/activate && python scripts/copy_expressjs_template.py "$*" -f

