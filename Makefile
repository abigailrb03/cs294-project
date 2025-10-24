ARCHIVE_NAME := spotify-starter.zip

# Define the specific files and directories you want to include in the zip
# Separate items with a space. Use 'folder/' for directories.
FILES_TO_ARCHIVE := \
    README.md \
    project/flask_app_starter/ \
    project/tests/ \
	requirements.txt \
	home.png

EXCLUDE_PATTERNS := \
    *__pycache__/* \
    *.pytest_cache/*

.PHONY: archive clean

# The archive target: creates the zip file with the specified contents
archive:
	@echo "Zipping selected files and folders into $(ARCHIVE_NAME)..."
	# The -r flag is used for recursive zipping of directories
	zip -r $(ARCHIVE_NAME) $(FILES_TO_ARCHIVE) -x $(EXCLUDE_PATTERNS)
	@echo "Archive created successfully: $(ARCHIVE_NAME)"

# A clean target to remove the generated archive
clean:
	@echo "Cleaning up $(ARCHIVE_NAME)..."
	rm -f $(ARCHIVE_NAME)
	@echo "Removed file: $(ARCHIVE_NAME)"
