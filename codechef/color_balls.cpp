// Akhil And Colored Balls : https://www.codechef.com/problems/ACBALL

#include <iostream>
#include <string>
using namespace std;

int hamming_distance(string str, string another_str){
  int dist = 0;
  for (int i = 0; i < str.size(); i++) {
    if(str[i] == another_str[i]){
      dist+=1;
    }
  }
  return dist;
}

string findZ(string X, string Y){
  string Z;
  for (int i = 0; i < X.size(); i++) {
    if(X[i] == Y[i]){
      Z += (X[i] == 'W' ? 'B' : 'W');
    }else{
      Z += 'B';
    }
  }

  return Z;
}



int main(int argc, char const *argv[]) {
  int T;
  cin >> T;
  while (T) {
    string answer;
    string X,Y;
    cin >> X;
    cin >> Y;

    answer = findZ(X,Y);

    cout << answer << endl;
    T--;
  }

  return 0;
}
