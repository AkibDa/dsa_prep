#include <iostream>

int main() {
  const int pi = 3.14;

  std::cout << "The value of pi is: " << pi << std::endl;
  // Uncommenting the next line will cause a compilation error
  // pi = 3.14159; // Error: cannot assign to variable 'pi' with const-qualified type 'const int'
  std::cout << "Attempting to change pi will result in an error." << std::endl;
  
  return 0;
}