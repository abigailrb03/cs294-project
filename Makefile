BUILD_DIR := .build
SRC_DIR := src/project
ARCHIVE_NAME := project.zip

EXCLUDE_PATTERNS := \
	.pytest_cache/* \
	.venv/* \
	instance/* \
    *__pycache__/*

RUFF_CMD := uv run ruff

.PHONY: build clean lint lint-fix format

build:
	# Remove existing build directory
	rm -rf $(BUILD_DIR)

	# Copy the solution code into a starter code directory
	mkdir $(BUILD_DIR)
	cp -r $(SRC_DIR) $(BUILD_DIR)

	# Compile solution files to starter files
	uv run python3 src/compile_starter.py $(SRC_DIR)/daylist/api.py $(BUILD_DIR)/project/daylist/api.py

	# Create starter .zip file
	cd $(BUILD_DIR) && zip -r $(ARCHIVE_NAME) project/* --exclude $(EXCLUDE_PATTERNS)

	@echo "Built starter code and .zip in $(BUILD_DIR)"

clean:
	rm -rf $(BUILD_DIR)

lint:
	$(RUFF_CMD) check

lint-fix:
	$(RUFF_CMD) check --fix

format:
	$(RUFF_CMD) format
