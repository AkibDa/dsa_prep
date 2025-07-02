#include <iostream>

using namespace std;

int main(){
  /*
    Type  |  Bytes  |  Range  
    --------------------------------
    char  |    1    |  -128 to 127
    int   |    4    |  -2 to 2
    float |    4    |  -3.4E38 to 3.4E38
    short |    2    |  -32K to 32K
    long  |    8    |  -2^63 to 2^63
    double|    8    |  -1.7E308 to 1.7E308
    bool  |    1    |  true or false
  long long |    8    |  -2^63 to 2^63
  */

  double price = 99.99;
  float interestRate = 3.67f;
  long fileSize = 90000L;
  char letter = 'a';
  bool isValid = false;
  auto count = 1000; // auto deduces type based on initializer

  int number {1.2};
  cout << number; // This will output 1, as the float is truncated to an int

  return 0;
}