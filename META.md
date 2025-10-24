# Meta

This is documentation for instructors and course staff.

## Compiling starter code for students

```sh
# Make sure you are in the `project` directory
cd project

# Copy the solution code into a starter code directory
cp -R flask_app/ flask_app_starter/

# Compile solution files to starter files, for example:
python3 compile_starter.py flask_app/api.py flask_app_starter/api.py

# Make sure you are in the root directory of the repo
cd ..

# Create the starter .zip file
make archive

# Remove the zip file and start from scratch if you want
make clean
```
