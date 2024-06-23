cmake_minimum_required(VERSION 3.14)
project(testpython)

# Include pybind11 using the local submodule
add_subdirectory(pybind11)

# Find Python
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)

# Define the module
add_library(testpython MODULE src/bindings.cpp)

# Link with pybind11 and Python
target_link_libraries(testpython PRIVATE pybind11::module Python3::Python)

# Set output properties
set_target_properties(testpython PROPERTIES
        PREFIX ""
        SUFFIX "${Python3_EXT_SUFFIX}"
)