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

    # Write Makefile files
    with open(os.path.join(project_dir, 'Makefile'), 'w') as f:
        f.write('''CC = gcc
CFLAGS = -Iinclude

.PHONY: all clean test

all: main

main: src/main.o src/module1/module1.o src/module2/module2.o
\t$(CC) $(CFLAGS) -o $@ $^

src/main.o: src/main.c
\t$(CC) $(CFLAGS) -o $@ -c $<

src/module1/module1.o: src/module1/module1.c include/module1.h
\t$(CC) $(CFLAGS) -o $@ -c $<

src/module2/module2.o: src/module2/module2.c include/module2.h
\t$(CC) $(CFLAGS) -o $@ -c $<

test: module1_test module2_test

module1_test: test/module1_test.o src/module1/module1.o
\t$(CC) $(CFLAGS) -o $@ $^

module2_test: test/module2_test.o src/module2/module2.o
\t$(CC) $(CFLAGS) -o $@ $^

test/module1_test.o: test/module1_test.c include/module1.h
\t$(CC) $(CFLAGS) -o $@ -c $<

test/module2_test.o: test/module2_test.c include/module2.h
\t$(CC) $(CFLAGS) -o $@ -c $<

clean:
\trm -f main src/*.o src/module1/*.o src/module2/*.o test/*.o module1_test module2_test
''')

    # Write source files
    with open(os.path.join(project_dir, 'src/main.c'), 'w') as f:
        f.write('// main.c content')

    with open(os.path.join(project_dir, 'src/module1/module1.c'), 'w') as f:
        f.write('// module1.c content')

    with open(os.path.join(project_dir, 'src/module2/module2.c'), 'w') as f:
        f.write('// module2.c content')

    # Write header files
    with open(os.path.join(project_dir, 'include/module1.h'), 'w') as f:
        f.write('// module1.h content')

    with open(os.path.join(project_dir, 'include/module2.h'), 'w') as f:
        f.write('// module2.h content')

    # Write test files
    with open(os.path.join(project_dir, 'test/module1_test.c'), 'w') as f:
        f.write('// module1_test.c content')

    with open(os.path.join(project_dir, 'test/module2_test.c'), 'w') as f:
        f.write('// module2_test.c content')

if __name__ == "__main__":
    project_name = input("Enter the project name: ")
    create_project_structure(project_name)
    print("Project structure created successfully!")
