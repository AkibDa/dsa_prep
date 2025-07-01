#include <iostream>

int main() {

  int x = 10;
  int y = 3;
  float z = x / y; 

  std::cout << "Value of z: " << z << std::endl;

  int a = x++;

  std::cout << "Value of a: " << a << std::endl;
  std::cout << "Value of x after increment: " << x << std::endl;

  int b = ++x;
  
  std::cout << "Value of b: " << b << std::endl;
  std::cout << "Value of x after pre-increment: " << x << std::endl;

  return 0;
}