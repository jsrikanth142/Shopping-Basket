# Makefile for Shopping Basket project

PYTHON := python
SRC_DIR := basket
TEST_DIR := tests
MAIN := main.py

.PHONY: help install run test lint format clean

help:
	@echo "Makefile commands for Shopping Basket project:"
	@echo "  make install     - Install dependencies"
	@echo "  make run ARGS=\"Apples Milk Bread\"  - Run the application with basket items"
	@echo "  make test        - Run unit tests"
	@echo "  make lint        - Run linters (flake8)"
	@echo "  make format      - Format code (black + isort)"
	@echo "  make clean       - Remove __pycache__ and .pyc files"

install:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

run:
	@echo "Running Shopping Basket with items: $(ARGS)"
	$(PYTHON) $(MAIN) $(ARGS)

test:
	$(PYTHON) -m pytest -v

lint:
	flake8 $(SRC_DIR) $(TEST_DIR) $(MAIN)

format:
	black $(SRC_DIR) $(TEST_DIR) $(MAIN)
	isort $(SRC_DIR) $(TEST_DIR) $(MAIN)

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
