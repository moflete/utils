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
        f.write('''cmake_minimum_required(VERSION 3.24)
project({})

# Include directories
include_directories(include)

# Add subdirectories
add_subdirectory(src)
'''.format(project_name))

    with open(os.path.join(project_dir, 'src/CMakeLists.txt'), 'w') as f:
        f.write('''# Include module directories
add_subdirectory(module1)
add_subdirectory(module2)

set(MAIN-SOURCES main.c)
                
add_executable({} ${MAIN-SOURCES})

target_link_libraries({} PRIVATE module1 module2)
''')

    with open(os.path.join(project_dir, 'src/module1/CMakeLists.txt'), 'w') as f:
        f.write('''# Define module1 library
add_library(module1
    src/module1.c
)

# Include directories
target_include_directories(module1 PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)
''')

    with open(os.path.join(project_dir, 'src/module2/CMakeLists.txt'), 'w') as f:
        f.write('''# Define module2 library
add_library(module2
    src/module2.c
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

    with open(os.path.join(project_dir, 'src/main.c'), 'w') as f:
        f.write('''#include <stdio.h>
                
#include "project.h"
#include "common.h"

int main(void) {
    printf("Hello, world!\\n");
    return 0;
}''')


    with open(os.path.join(project_dir, 'test/CMakeLists.txt'), 'w') as f:
        f.write('''# Set the source files for tests
set(TEST_SOURCES
    module1_test.c
    module2_test.c
)

# Create a test executable
add_executable({}_tests ${{TEST_SOURCES}})

# Link with project libraries and required libraries for testing
target_link_libraries({}_tests PRIVATE module1 module2)

# Add tests using CTest
enable_testing()
add_test(NAME {}_tests COMMAND {}_tests)
'''.format(project_name, project_name, project_name, project_name))

    with open(os.path.join(project_dir, 'test/module1_test.c'), 'w') as f:
        f.write('// module1_test.c content')

    with open(os.path.join(project_dir, 'test/module2_test.c'), 'w') as f:
        f.write('// module2_test.c content')

    # Write module source files
    with open(os.path.join(project_dir, 'src/module1/src/module1.c'), 'w') as f:
        f.write('// module1.c content')

    with open(os.path.join(project_dir, 'src/module2/src/module2.c'), 'w') as f:
        f.write('// module2.c content')

    # Write module header files
    with open(os.path.join(project_dir, 'src/module1/include/module1.h'), 'w') as f:
        f.write('// module1.h content')

    with open(os.path.join(project_dir, 'src/module2/include/module2.h'), 'w') as f:
        f.write('// module2.h content')

    # Write conanfile.py
    with open(os.path.join(project_dir, 'conanfile.py'), 'w') as f:
        f.write('''from conan import ConanFile
from conan.tools.cmake import cmake_layout

class MyProjectConan(ConanFile):
    name = "{}"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    requires = []
    generators = "CMakeDeps", "CMakeToolchain"

    def requirements(self):
        self.requires("unity/2.6.0")
        self.requires("log.c/cci.20200620")

    def layout(self):
        cmake_layout(self)
'''.format(project_name))

if __name__ == "__main__":
    project_name = input("Enter the project name: ")
    create_project_structure(project_name)
    print("Project structure created successfully!")
