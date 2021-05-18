// https://www.hackerrank.com/challenges/c-tutorial-stringstream?h_r=next-challenge&h_v=zen

#include <iostream>
#include <sstream>
#include <vector>
using namespace std;


vector<int> parseInts(string str) {
   stringstream ss(str);
   vector<int> integers;

   while(ss.good()){
     string substr;
     getline(ss, substr, ',');
     integers.push_back(stoi(substr));
   }

   return integers;
}


int main(int argc, char const *argv[]) {
  string input;
  cin >> input;

  vector<int> integers = parseInts(input);

  for (int i = 0; i < integers.size(); i++) {
    cout << integers.at(i) << endl;
  }
  return 0;
}
