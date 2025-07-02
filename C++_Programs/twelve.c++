#include <iostream>

using namespace std;

int main(){
  float temp;

  cout << "Enter temperature in Fahrenheit: ";
  cin >> temp;

  float cel = (temp - 32) * 5 / 9;
  cout << "Temperature in Celsius: " << cel << endl;

  return 0;
}