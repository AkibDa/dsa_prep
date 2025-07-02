#include <iostream>
#include <cmath>

using namespace std;

int main(){
  double result = floor(1.2);
  cout << "The floor of 1.2 is: " << result << endl;
  result = ceil(1.2);
  cout << "The ceil of 1.2 is: " << result << endl;

  float radius;

  cout << "Enter the radius of the circle: ";
  cin >> radius;
  double area = M_PI * radius * radius;
  cout << "The area of the circle is: " << area << endl;

  return 0;
}