import os

def create_project_structure(project_name):
    # Create project directory
    os.makedirs(project_name)

    # Create README.md
    with open(os.path.join(project_name, 'README.md'), 'w') as f:
        f.write('# ' + project_name + '\n\n')

    # Create setup.py
    with open(os.path.join(project_name, 'setup.py'), 'w') as f:
        f.write('# setup.py file content goes here\n')

    # Create requirements.txt
    with open(os.path.join(project_name, 'requirements.txt'), 'w') as f:
        f.write('# requirements.txt file content goes here\n')

    # Create docs directory and files
    os.makedirs(os.path.join(project_name, 'docs'))
    with open(os.path.join(project_name, 'docs', 'index.md'), 'w') as f:
        f.write('# Documentation\n\n')
    with open(os.path.join(project_name, 'docs', 'conf.py'), 'w') as f:
        f.write('# conf.py file content goes here\n')

    # Create src directory and files
    src_path = os.path.join(project_name, 'src')
    os.makedirs(src_path)
    with open(os.path.join(src_path, '__init__.py'), 'w'):
        pass
    for module in ['module1', 'module2', 'common']:
        module_path = os.path.join(src_path, module)
        os.makedirs(module_path)
        with open(os.path.join(module_path, '__init__.py'), 'w'):
            pass
        with open(os.path.join(module_path, module + '.py'), 'w') as f:
            f.write(f'# {module}.py file content goes here\n')
        if module != 'common':
            with open(os.path.join(module_path, 'utils.py'), 'w') as f:
                f.write(f'# utils.py file content goes here\n')

    # Create tests directory and files
    tests_path = os.path.join(project_name, 'tests')
    os.makedirs(tests_path)
    with open(os.path.join(tests_path, '__init__.py'), 'w'):
        pass
    for test_file in ['test_module1.py', 'test_module2.py', 'test_common.py']:
        with open(os.path.join(tests_path, test_file), 'w') as f:
            f.write(f'# {test_file} file content goes here\n')

if __name__ == "__main__":
    project_name = input("Enter project name: ")
    create_project_structure(project_name)
    print(f"Project '{project_name}' created successfully.")
