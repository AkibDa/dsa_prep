#include <iostream>

int main(){
  int a = 5;
  int b = 3;

  std::cout << "Before swap: " << std::endl;
  std::cout << "Value of a: " << a << ", b: " << b << std::endl;

  b = a + b; // b now becomes the sum of a and b
  a = b - a; // a now becomes the original value of b
  b = b - a; // b now becomes the original value of a

  std::cout << "After swap: " << std::endl;
  std::cout << "Value of a: " << a << ", b: " << b << std::endl;


  return 0;
}