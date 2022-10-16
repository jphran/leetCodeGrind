//
// Created by thera on 10/15/22.
//

#ifndef LEETCODEGRIND_ENCODEANDDECODESTRINGS_H
#define LEETCODEGRIND_ENCODEANDDECODESTRINGS_H

#include <string>
#include <vector>

using namespace std;

class Codec {
private:
    int SIZE_OF_CHUNK = 3;
public:

    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        string encodedString{};
        for (auto s : strs) {
            string chunkSize = to_string(s.size());
            while (chunkSize.size() < SIZE_OF_CHUNK) {
                chunkSize.insert(0, 1, '0');
            }
            encodedString += chunkSize + s;
        }
        return encodedString;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        vector<string> decodedStrings{};
        int chunkSize{};
        while (s.size() > 0) {
            chunkSize = stoi(s.substr(0, SIZE_OF_CHUNK));
            decodedStrings.push_back(s.substr(SIZE_OF_CHUNK, chunkSize));
            s = s.substr(SIZE_OF_CHUNK + chunkSize, s.size());
        }
        return decodedStrings;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(strs));

#endif//LEETCODEGRIND_ENCODEANDDECODESTRINGS_H
