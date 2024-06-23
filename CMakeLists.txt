cmake_minimum_required(VERSION 3.29)
project(testpython)

set(CMAKE_CXX_STANDARD 26)

# Include pybind11 using the local submodule
add_subdirectory(pybind11)

# Find Python
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)

# Add include directory for pybind11
include_directories(pybind11/include)

# Define the module
add_library(testpython MODULE src/bindings.cpp)

# Link with pybind11 and Python
target_link_libraries(testpython PRIVATE pybind11::module)

# Set output properties
set_target_properties(testpython PROPERTIES
        PREFIX "")

# Additional setup for Windows
if (WIN32)
    # Use Visual Studio generator
    set(CMAKE_GENERATOR "Visual Studio")
endif()