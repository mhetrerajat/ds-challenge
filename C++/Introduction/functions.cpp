// https://www.hackerrank.com/challenges/c-tutorial-functions?h_r=next-challenge&h_v=zen

#include <iostream>
using namespace std;

int greatest(int a, int b, int c, int d){
  int max = 0;
  max = a>b ? a : b;
  max = c>max ? c : max;
  max = d>max ? d : max;
  return max;
}

int main(){
  int a,b,c,d;
  cin >> a >> b >> c >> d;
  cout << greatest(a,b,c,d) << endl;
  return 0;
}
