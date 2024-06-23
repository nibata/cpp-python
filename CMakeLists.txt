cmake_minimum_required(VERSION 3.29)
project(testpython)

set(CMAKE_CXX_STANDARD 26)

# Specify the path to the Python interpreter in the Miniconda environment
set (PYTHON_EXECUTABLE "/Users/nbacquet/opt/miniconda3/envs/jupyter/bin/python")

# Include pybind11 from the local directory
add_subdirectory(pybind11)

# Add source files
add_library(testpython MODULE src/bindings.cpp)

# Link pybind11 to the target
target_link_libraries(testpython PRIVATE pybind11::module)

# Set Target Properties
set_target_properties(testpython PROPERTIES
        PREFIX "")

