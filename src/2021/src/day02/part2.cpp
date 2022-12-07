#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int main() {
    int arr[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

    int size = sizeof(arr) / sizeof(arr[0]);

    int sizeTest = sizeof(arr);

    cout << "size: " << size << endl;
    cout << "sizeTest: " << sizeTest << endl;

    // what is sizeof(arr)?
    // what is sizeof(arr[0])?
    // what is sizeof(arr) / sizeof(arr[0])?

    // sizeof(arr) is the size of the array in bytes
    // sizeof(arr[0]) is the size of the first element in the array in bytes
    // sizeof(arr) / sizeof(arr[0]) is the number of elements in the array

    // how does sizeof(arr) / sizeof(arr[0]) work?

    // the size of the array is divided by the size of the first element in the array
    // the result is the number of elements in the array

    // what is the difference between sizeof(arr) and sizeof(arr[0])?

    return 0;
}