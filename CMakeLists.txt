cmake_minimum_required(VERSION 3.29)
project(testpython)

set(CMAKE_CXX_STANDARD 26)

# Include the local pybind11 directory
add_subdirectory(pybind11)

# Define the module
add_library(testpython MODULE src/bindings.cpp)

# Link with pybind11 and Python
target_link_libraries(testpython PRIVATE pybind11::module)

# Set output properties
set_target_properties(testpython PROPERTIES
        PREFIX "")