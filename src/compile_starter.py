"""
Compiles an input .py file into a starter .py file. Example usage:

# Make sure you are in the `project` directory
cd project

# Copy the solution code into a starter code directory
cp -R flask_app/ flask_app_starter/

# Compile solution file to starter file
python3 compile_starter.py flask_app/api.py flask_app_starter/api.py
"""

import argparse
import re

def strip_solutions_line_by_line(input_file_path, output_file_path):
    """
    Reads a .py file line by line. When a '# BEGIN SOLUTION' marker is found,
    it extracts the prompt and inserts it, then skips lines until '# END SOLUTION'.
    """

    # Regex to extract the prompt content from the BEGIN SOLUTION line
    # It looks for: # BEGIN SOLUTION PROMPT=" (Group 1: the content inside the quotes) "
    PROMPT_PATTERN = re.compile(r'# BEGIN SOLUTION PROMPT="(.*?)"')

    output_lines = []
    in_solution_block = False

    try:
        with open(input_file_path, 'r', encoding='utf-8') as infile:
            for line in infile:

                # Check for the BEGIN SOLUTION marker
                if line.strip().startswith('# BEGIN SOLUTION'):
                    in_solution_block = True
                    match = PROMPT_PATTERN.search(line)

                    if match:
                        # Extract the prompt content
                        prompt_text = match.group(1).strip()

                        # Use the extracted prompt as the replacement line
                        # We add proper indentation by inspecting the original prompt's position
                        indentation = line.split('#')[0]
                        prompt = f"{indentation}{prompt_text}\n"

                        # Add the prompt
                        output_lines.append(prompt)

                # Check for the END SOLUTION marker
                elif line.strip().startswith('# END SOLUTION'):
                    if in_solution_block:
                        in_solution_block = False

                # If we are inside a solution block, skip the line (it's solution code)
                elif in_solution_block:
                    continue

                # If we are outside any solution block, keep the line
                else:
                    output_lines.append(line)

    except FileNotFoundError:
        print(f"Error: Input file not found at '{input_file_path}'")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    # Write the results to the output file
    try:
        with open(output_file_path, 'w', encoding='utf-8') as outfile:
            outfile.writelines(output_lines)
        print(f"Successfully stripped solutions (replacing with prompts) and saved to '{output_file_path}'")
    except IOError:
        print(f"Error: Could not write to output file at '{output_file_path}'")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Strip solutions from a .py file and replace them with the PROMPT content."
    )

    parser.add_argument(
        "input",
        type=str,
        help="Path to the input .py file with solutions."
    )

    parser.add_argument(
        "output",
        type=str,
        help="Path for the new .py file without solutions."
    )

    args = parser.parse_args()

    strip_solutions_line_by_line(args.input, args.output)
