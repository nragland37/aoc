#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int main(int argc, char* argv[]) {
    string input = "input01.txt";

    // display input01.txt
    while 
    if (argc > 1) {
        input = argv[1];
    }

    string line;
    fstream file(input);
    int x = 0;
    int d = 0;
    while (getline(file, line)) {
        if (line[0] == 'f') {
            x += stoi(line.substr(7, line.size() - 7));
        } else if (line[0] == 'd') {
            d += stoi(line.substr(4, line.size() - 4));
        } else if (line[0] == 'u') {
            d -= stoi(line.substr(2, line.size() - 2));
        }
    }
    cout << x * d << '\n';
    return 0;
}

// what is argc and argv?

// argc is the number of arguments passed to the program
// argv is an array of strings containing the arguments

// what is the difference between argv[0] and argv[1]?

// argv[0] is the name of the program
// argv[1] is the first argument passed to the program
