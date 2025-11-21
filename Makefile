BUILD_DIR := .build
BUILD_PROJ_DIR := $(BUILD_DIR)/project
SRC_DIR := src/project
ARCHIVE_NAME := project.zip
RUFF_CMD := uv run ruff

.PHONY: build clean lint lint-fix format

build:
	# Remove existing build directory
	rm -rf $(BUILD_DIR)

	# Copy the solution code into a starter code directory
	mkdir $(BUILD_DIR)
	cp -r $(SRC_DIR) $(BUILD_DIR)

	# Remove directories we don't want to include in the starter code zip
	rm -rf $(BUILD_PROJ_DIR)/.pytest_cache
	rm -rf $(BUILD_PROJ_DIR)/.venv
	rm -rf $(BUILD_PROJ_DIR)/instance
	rm -rf $(BUILD_PROJ_DIR)/daylist/__pycache__
	rm -rf $(BUILD_PROJ_DIR)/tests/__pycache__

	# Compile solution files to starter files
	uv run python3 src/compile_starter.py $(SRC_DIR)/daylist/api.py $(BUILD_PROJ_DIR)/daylist/api.py
	uv run python3 src/compile_starter.py $(SRC_DIR)/daylist/dao.py $(BUILD_PROJ_DIR)/daylist/dao.py

	# Create starter .zip file
	cd $(BUILD_DIR) && zip -r $(ARCHIVE_NAME) project/

	@echo "Built starter code and .zip in $(BUILD_DIR)"

clean:
	rm -rf $(BUILD_DIR)

lint:
	$(RUFF_CMD) check

lint-fix:
	$(RUFF_CMD) check --fix

format:
	$(RUFF_CMD) format
