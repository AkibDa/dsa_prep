#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(){
  srand(time(0));

  int dice = rand() % 6 + 1; // Generate a random number between 1 and 6
  cout << "You rolled a " << dice << endl;
  if (dice == 6) {
    cout << "You win!" << endl;
  } else {
    cout << "You lose!" << endl;
  }

  return 0;
}