// src/bindings.cpp
#include <pybind11/pybind11.h>
#include "example.cpp"  // Include the header or source file for the C++ functions

namespace py = pybind11;

PYBIND11_MODULE(testpythonnibata, m) {
    m.def("greet", &greet, "A function that greets the user",py::arg("name"));
}
