cmake_minimum_required(VERSION 3.20)
project(Project_Euler)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(Project_Euler
        helpful.cpp
        main.cpp
        main_header.h
        problems41_75.cpp
        cmake-build-debug/words.txt
        )
