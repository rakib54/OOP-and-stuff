#include <bits/stdc++.h>
using namespace std;

int main () {
  string s = "abccbaacz";
  unordered_map<char,int> umap;
  
  for(auto c:s){
    umap[c]++;
    for (auto m:umap){
      if(m.second == 2){
        cout<<m.first<<endl;
        return 0;
      }
    }
  }

  // for (int i = 0; i < s.size(); i++) {
  //        cout<<umap[s[i]]<<endl;
  //     }


  return 0;
}