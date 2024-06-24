cmake_minimum_required(VERSION 3.29)
project(testpython)

set(CMAKE_CXX_STANDARD 11)

# Include pybind11 using the local submodule
add_subdirectory(pybind11)

# Find Python
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)

# Add include directory for pybind11
include_directories(pybind11/include)

# Define the module
pybind11_add_module(testpython src/bindings.cpp)

# Link with Python
target_link_libraries(testpython PRIVATE Python3::Python)

# Set output properties
set_target_properties(testpython PROPERTIES
        PREFIX "")

# Additional setup for Windows
if (WIN32)
    # Use gcc as the compiler
    set(CMAKE_C_COMPILER gcc)
    set(CMAKE_CXX_COMPILER g++)
    set_target_properties(testpython PROPERTIES SUFFIX ".pyd")
endif()
