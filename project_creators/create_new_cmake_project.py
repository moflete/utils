import os

def create_project_structure(project_name):
    project_dir = os.path.join('.', project_name)
    # Create directories
    os.makedirs(os.path.join(project_dir, 'src/module1/include'), exist_ok=True)
    os.makedirs(os.path.join(project_dir, 'src/module1/src'), exist_ok=True)
    os.makedirs(os.path.join(project_dir, 'src/module2/include'), exist_ok=True)
    os.makedirs(os.path.join(project_dir, 'src/module2/src'), exist_ok=True)
    os.makedirs(os.path.join(project_dir, 'include'), exist_ok=True)
    os.makedirs(os.path.join(project_dir, 'test'), exist_ok=True)

    # Write CMakeLists.txt files
    with open(os.path.join(project_dir, 'CMakeLists.txt'), 'w') as f:
        f.write('''cmake_minimum_required(VERSION 3.10)
project({})
        
# Include directories
include_directories(include)

# Add subdirectories
add_subdirectory(src)
'''.format(project_name))

    with open(os.path.join(project_dir, 'src/module1/CMakeLists.txt'), 'w') as f:
        f.write('''# Define module1 library
add_library(module1
    src/module1.cpp
)

# Include directories
target_include_directories(module1 PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)
''')

    with open(os.path.join(project_dir, 'src/module2/CMakeLists.txt'), 'w') as f:
        f.write('''# Define module2 library
add_library(module2
    src/module2.cpp
)

# Include directories
target_include_directories(module2 PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)
''')

    with open(os.path.join(project_dir, 'include/project.h'), 'w') as f:
        f.write('// project.h content')

    with open(os.path.join(project_dir, 'include/common.h'), 'w') as f:
        f.write('// common.h content')

    with open(os.path.join(project_dir, 'src/main.cpp'), 'w') as f:
        f.write('// main.cpp content')

    with open(os.path.join(project_dir, 'test/CMakeLists.txt'), 'w') as f:
        f.write('''# Set the source files for tests
set(TEST_SOURCES
    module1_test.cpp
    module2_test.cpp
)

# Create a test executable
add_executable({}_tests ${{TEST_SOURCES}})

# Link with project libraries and required libraries for testing
target_link_libraries({}_tests PRIVATE module1 module2)

# Add tests using CTest
enable_testing()
add_test(NAME {}_tests COMMAND {}_tests)
'''.format(project_name, project_name, project_name, project_name))

    with open(os.path.join(project_dir, 'test/module1_test.cpp'), 'w') as f:
        f.write('// module1_test.cpp content')

    with open(os.path.join(project_dir, 'test/module2_test.cpp'), 'w') as f:
        f.write('// module2_test.cpp content')

if __name__ == "__main__":
    project_name = input("Enter the project name: ")
    create_project_structure(project_name)
    print("Project structure created successfully!")
