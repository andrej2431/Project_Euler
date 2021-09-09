#include "main_header.h"

int problem41() {
    std::vector<int> numbers = {1, 2, 3};
    int operations = 6;
    int result = -1;
    for (int i = 4; i < 10; i++) {
        numbers.push_back(i);
        operations *= i;
        for (int j = 0; j < operations; j++) {
            if (is_prime(vec_to_int(numbers)))
                result = vec_to_int(numbers);
            std::next_permutation(numbers.begin(), numbers.end());

        }
    }
    return result;
};

int problem42() {

    std::fstream file;
    file.open("words.txt", std::ios::in);

    std::string line;
    file >> line;
    std::stringstream words(line);

    std::string parsed;
    int counter = 0;

    std::set<int> triangle_numbers = generate_triangles(10000);
    while (std::getline(words, parsed, ',')) {
        if (is_triangle_word(parsed.substr(1, parsed.size() - 2), triangle_numbers))
            counter++;
    }


    return counter;


}

bool is_pandigital_prime_divisible(long number) {
    vector<std::pair<int, int>> zipped = {{17, 1},
                                          {13, 10},
                                          {11, 100},
                                          {7,  1000},
                                          {5,  10000},
                                          {3,  100000},
                                          {2,  1000000}};
    for (auto duo : zipped) {
        int prime = duo.first, mod = duo.second;
        long temp = (number % (mod * 1000) - number % mod)/mod;
        if (temp % prime != 0)
            return false;
    }
    return true;
}

long long problem43() {
    std::vector<int> digits = {0,1,2,3,4,5,6,7,8,9};

    long long operation_count = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10;


    long long result = 0;

    for (long long i = 0; i < operation_count; i++) {
        if (is_pandigital_prime_divisible(vec_to_long(digits))) {
            result += vec_to_long(digits);
        }


        std::next_permutation(digits.begin(), digits.end());
    }
    return result;
}

int problem44(){
    std::set<int> pentagonal_numbers = generate_pentagons(10000);
    long result = 99999999999;
    for (int num1 : pentagonal_numbers){
        for (int num2 : pentagonal_numbers){
            if(pentagonal_numbers.find(num1+num2)!=pentagonal_numbers.end()){

                if (pentagonal_numbers.find(std::abs(num1-num2))!=pentagonal_numbers.end()){
                    std::cout << num1 << " " << num2<<"\n";
                    result = std::min(result,(long) std::abs(num1-num2));
                }

            }


        }
    }
    return result;
}