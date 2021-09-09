#include "main_header.h"

void print_vec(const std::vector<int>& numbers){
    for (int elem : numbers){
        std::cout << elem << " ";
    }
    std::cout<< "\n";
}

bool is_prime(int number){
    int i = 2;
    while (i*i <= number){
        if (number%i == 0)
            return false;
        ++i;
    }
    return true;
}

std::set<int> generate_triangles(int n){
    std::set<int> numbers;
    for (int i = 1; i<n;i++){
        numbers.insert(i*(i+1)/2);

    }

    return numbers;
}

std::set<int> generate_pentagons(int n){
    std::set<int> numbers;
    for(int i = 1; i<n;i++){
        numbers.insert( i*(3*i-1)/2);
    }
    return numbers;
}

bool is_triangle_word(const std::string& word, const std::set<int>& triangle_numbers){
    int total = 0;

    for (char character: word){
        total+= (int) character - 64;
    }
    if(triangle_numbers.find(total)==triangle_numbers.end())
        return false;
    return true;


}

int vec_to_int(const std::vector<int>& digits){
    int number = 0;
    for (int elem : digits){
        number*=10;
        number += elem;
    }
    return number;
}

long vec_to_long(const std::vector<int>& digits){
    long number = 0;
    for (int elem : digits){
        number*=10;
        number += elem;
    }
    return number;
}
