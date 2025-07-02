#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(){

  srand(time(0)); // Seed the random number generator

  int number = rand() % 10;

  cout << "Random number: " << number << endl;

  return 0;
}