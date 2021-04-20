//Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.
//
// Created by jfrancis on 4/19/21.
//

#ifndef LEETCODEGRIND_SETMATRIXZEROES_H
#define LEETCODEGRIND_SETMATRIXZEROES_H

#include <vector>
#include <set>

class Solution {
public:
    void setZeroes(std::vector<std::vector<int>>& matrix) {
        int numRow = matrix.size();
        int numCol = matrix[0].size();

        //find zero
        std::set<int> rowIndices;
        std::set<int> colIndices;
        for(int row = 0; row < numRow; ++row) {
            for(int col = 0; col < numCol; ++col) {
                if(matrix[row][col] == 0) {
                    rowIndices.emplace(row);
                    colIndices.emplace(col);
                }
            }
        }

        //set zeros
        for(auto rowIdx : rowIndices)
            matrix[rowIdx] = std::vector<int>(numCol, 0);

        for(auto colIdx : colIndices)
            for(int row = 0; row < numRow; ++row) {
                matrix[row][colIdx] = 0;
            }
    }
};

#endif //LEETCODEGRIND_SETMATRIXZEROES_H
