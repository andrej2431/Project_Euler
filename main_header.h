#pragma once
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <set>

using std::set;
using std::vector;
using std::string;
using std::cout;

int problem41();
int problem42();
long long problem43();
int problem44();

void print_vec(const std::vector<int>&);
bool is_prime(int);
std::set<int> generate_triangles(int);
std::set<int> generate_pentagons(int);
bool is_triangle_word(const std::string&, const std::set<int>&);
int vec_to_int(const std::vector<int>&);
long vec_to_long(const std::vector<int>&);
