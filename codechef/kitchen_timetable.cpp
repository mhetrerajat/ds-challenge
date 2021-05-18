// Kitchen Timetable : https://www.codechef.com/problems/KTTABLE

#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char const *argv[]) {
  int T, N, temp;
  vector<int> countList;

  cin >> T;

  while (T) {
    int count=0;
    vector<int> A,B;

    cin >> N;

    for (int i = 0; i < N; i++) {
      cin >> temp;
      A.push_back(temp);
    }

    for (int i = 0; i < N; i++) {
      cin >> temp;
      B.push_back(temp);
    }

    for (int i = 0; i < N; i++) {
      if(i==0){
          if(A.front() >= B.front()){
            count += 1;
            //cout << A.front() << B.front() << count << endl;
          }
      }else{
          if(A.at(i)-A.at(i-1) >= B.at(i)){
            count += 1;
            //cout << A.at(i)-A.at(i-1) << B.at(i) << count << endl;
          }
      }
    }

    countList.push_back(count);
    T--;
  }

  for (int i = 0; i < countList.size(); i++) {
    cout << countList.at(i) << endl;
  }

  return 0;
}
