// Copyright 2017 Siyuan Tang sytang7@bu.edu
// Copyright 2017 Pei Jia leojia@bu.edu
// Copyright 2017 Jiali Ge ivydany@bu.edu

#include <ctype.h>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstring>
#include <fstream>
#include <iostream>
#include <list>
#include <stack>
#include <string>
#include <unordered_set>
#include <vector>
using std::string;
using std::cout;
using std::cin;
using std::endl;
using std::vector;
using std::unordered_set;
using std::list;
using std::stack;
using std::ifstream;
using std::swap;

static const char GRID_USED = '-';

bool stringCompare(const vector<string> &left, const vector<string> &right) {
  for (int i = 0; i < left.size(); i ++) {
    if (left[i] < right[i])
      return true;
    else if (left[i] > right[i])
      return false;
  }
}

template<class T> struct Hash;
template<> struct Hash<vector<string>> {
  size_t operator()(const vector<string>& v) const {
    size_t hash = 0;
    for (const string& s : v)
      hash += std::hash<string>()(s);
    return hash;
  }
};

struct Point {
  int x, y;
  Point(int _x, int _y) : x(_x), y(_y) {}
  bool operator==(const Point& p) const {
    return x == p.x && y == p.y;
  }
};

struct Path {
  list<Point> points;
  string word;
  Path(const Point& p, char c) {
    insert(p, c);
  }

  Path(const Path& path, const Point& p, char c) :
    points(path.points), word(path.word) {
    insert(p, c);
  }

  bool contains(const Point& p) const {
    return find(points.begin(), points.end(), p) != points.end();
  }

  void insert(const Point& p, char c) {
    points.push_back(p);
    word += c;
  }

  size_t size() const {
    return points.size();
  }
};

int readDict(const string& fname, unordered_set<string>&
             partialDictionary, unordered_set<string>& dictionary) {
  ifstream file(fname);
  if (!file.is_open())
    return 0;

  string currentWord, line;
  while (getline(file, line)) {
    for (int i = 0; i < line.size(); i++) {
      currentWord += tolower(line[i]);
      partialDictionary.insert(currentWord);
    }

    dictionary.insert(currentWord);
    currentWord = "";
  }

  return 1;
}

void adjustGrid(vector<vector<char>>& grid, const Path& path) {
  for (const Point& p : path.points)
    grid[p.x][p.y] = GRID_USED;

  for (int i = 0; i < grid.size(); i++) {
    for (int j = 0; j < grid.size() - 1; j++) {
      if (isalpha(grid[j][i]) && grid[j + 1][i] == GRID_USED) {
        swap(grid[j][i], grid[j + 1][i]);
        j = -1;
      }
    }
  }
}

void findPossibilities(int targetLengthIndex, const vector<int>&
                       wordLengths, vector<vector<char>> grid,
                       const vector<string>& list,
                       const unordered_set<string>& partialDictionary,
                       const unordered_set<string>&
                       dictionary, vector<string> currentWords,
                       unordered_set<vector<string>,
                       Hash<vector<string>>>& foundWords) {
  if (currentWords.size() == wordLengths.size()) {
    foundWords.insert(currentWords);
    return;
  }

  stack<Path> st;
  for (int i = 0; i < grid.size(); i++)
    for (int j = 0; j < grid.size(); j++)
      if (grid[i][j] != GRID_USED)
        st.push(Path(Point(i, j), grid[i][j]));

  while (!st.empty()) {
    Path cur = st.top();
    st.pop();
    if (cur.size() == wordLengths[targetLengthIndex]) {
      int flag = 0;
      if ((list[targetLengthIndex].front() == '+' ||
           cur.word.front() == list[targetLengthIndex].front()) &&
          list[targetLengthIndex].back() == '+' ||
          cur.word.back() == list[targetLengthIndex].back())
        flag = 1;
      if (dictionary.count(cur.word) > 0 && flag == 1) {
        vector<vector<char>> newGrid(grid);
        vector<string> newCurrentWords(currentWords);
        adjustGrid(newGrid, cur);
        newCurrentWords.push_back(cur.word);
        findPossibilities(targetLengthIndex + 1, wordLengths,
                          newGrid, list, partialDictionary, dictionary,
                          newCurrentWords, foundWords);
      }
      continue;
    }

    if (partialDictionary.count(cur.word) > 0) {
      for (int i = -1; i <= 1; i++) {
        for (int j = -1; j <= 1; j++) {
          const Point& loc = cur.points.back();
          if (loc.x + i >= 0 && loc.x + i < grid.size() &&
              loc.y + j >= 0 && loc.y + j < grid.size() &&
              grid[loc.x + i][loc.y + j] != GRID_USED &&
              !cur.contains(Point(loc.x + i, loc.y + j)))
            st.push(Path(cur, Point(loc.x + i, loc.y + j),
                         grid[loc.x + i][loc.y + j]));
        }
      }
    }
  }
}

int main(int argc, char **argv) {
  string dict_path = argv[1];
  string dict_path_backup = argv[2];

  unordered_set<string> partialDictionary, dictionary;
  unordered_set<string> partialDictionary_b, dictionary_b;
  if (!readDict(dict_path, partialDictionary, dictionary) ||
      !readDict(dict_path_backup, partialDictionary_b, dictionary_b)) {
    return 1;
  }

  char buffer[1000];
  string puzzle = "";
  string tmp;
  int count;
  while (fgets(buffer, 1000, stdin) != NULL) {
    tmp = string(buffer);
    if (tmp.back() == '\n')
      tmp.pop_back();
    if (tmp.find("*") == string::npos) {
      puzzle += tmp;
    } else {
      count = 0;
      vector<int> wordLengths;
      vector<string> list;
      string exist = "";
      for (int i = 0; i < tmp.size(); i++) {
        if (tmp.at(i) != ' ') {
          if (isalpha(tmp.at(i)))
            exist += tmp[i];
          else
            exist += '+';
          count++;
        } else {
          wordLengths.push_back(count);
          list.push_back(exist);
          exist = "";
          count = 0;
        }
      }
      wordLengths.push_back(count);
      list.push_back(exist);

      int dim;
      dim = sqrt(puzzle.length());

      vector<vector<char>> grid(dim, vector<char>(dim));
      int k = 0;
      for (int i = 0; i < dim; i++) {
        for (int j = 0; j < dim; j++) {
          grid[i][j] = puzzle[k];
          k++;
          grid[i][j] = tolower(grid[i][j]);
        }
      }
      unordered_set<vector<string>, Hash<vector<string>>> foundWords;
      findPossibilities(0, wordLengths, grid, list, partialDictionary,
                        dictionary, vector<string>(), foundWords);
      if (foundWords.empty())
        findPossibilities(0, wordLengths, grid, list, partialDictionary_b,
                          dictionary_b, vector<string>(), foundWords);

      vector<vector<string>> foundWordsV;
      for (unordered_set<vector<string>, Hash<vector<string>>>::iterator
           it = foundWords.begin(); it != foundWords.end(); ++it) {
        vector<string> elem;
        for (const string& word : *it) {
          elem.push_back(word);
        }
        foundWordsV.push_back(elem);
      }
      sort(foundWordsV.begin(), foundWordsV.end(), stringCompare);


      for (vector<vector<string>>::iterator it =
             foundWordsV.begin(); it != foundWordsV.end(); ++it) {
        string res = "";
        for (const string& word : *it) {
          res = res + word + " ";
        }
        res.pop_back();
        cout << res;
        if (it != foundWordsV.end() && res != "")
          cout << endl;
      }
      cout << "." << endl;
      puzzle = "";
    }
  }
}
