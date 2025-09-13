import os
import re

def validate_mdc_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Check for front-matter (metadata)
    if not content.startswith('---\n'):
        return False, f"Missing front-matter in {filepath}"

    # Check for description, globs, alwaysApply in front-matter
    if not re.search(r'description:', content) or \
       not re.search(r'globs:', content) or \
       not re.search(r'alwaysApply:', content):
        return False, f"Missing required metadata (description, globs, alwaysApply) in {filepath}"

    # Check file size (max 500 lines for MDC files)
    lines = content.split('\n')
    if len(lines) > 500:
        return False, f"File {filepath} exceeds 500 lines."

    # Check for mandatory sections (example, adjust as needed)
    if not re.search(r'# Architectural Compliance & Quality Gates', content) and \
       not re.search(r'# MDC Compliance Checklist', content):
        return False, f"Missing mandatory sections in {filepath}"

    # Check for hardcoded sensitive values (example, extend as needed)
    if re.search(r'API_KEY = "[a-zA-Z0-9]+"', content) or \
       re.search(r'PASSWORD = "[a-zA-Z0-9]+"', content):
        return False, f"Potential hardcoded sensitive value in {filepath}"

    return True, ""

def main():
    mdc_files = []
    for root, _, files in os.walk('languages'):
        for file in files:
            if file.endswith('.mdc'):
                mdc_files.append(os.path.join(root, file))
    for root, _, files in os.walk('devops'):
        for file in files:
            if file.endswith('.mdc'):
                mdc_files.append(os.path.join(root, file))
    for root, _, files in os.walk('templates'):
        for file in files:
            if file.endswith('.mdc'):
                mdc_files.append(os.path.join(root, file))
    for root, _, files in os.walk('personas'):
        for file in files:
            if file.endswith('.mdc'):
                mdc_files.append(os.path.join(root, file))

    all_passed = True
    for mdc_file in mdc_files:
        passed, message = validate_mdc_file(mdc_file)
        if not passed:
            print(f"Validation failed for {mdc_file}: {message}")
            all_passed = False
        else:
            print(f"Validation passed for {mdc_file}")

    if not all_passed:
        print("MDC validation failed. Please fix the issues.")
        exit(1)
    else:
        print("All MDC files passed validation.")

if __name__ == '__main__':
    main()


