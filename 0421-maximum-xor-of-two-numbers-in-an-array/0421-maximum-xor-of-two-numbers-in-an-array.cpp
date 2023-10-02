#include <vector>
#include <algorithm>

struct TrieNode {
    TrieNode* children[2];
    TrieNode() {
        children[0] = children[1] = nullptr;
    }
};

class Trie {
public:
    Trie() {
        root = new TrieNode();
    }

    int insert(int num, int maxLen) {
        TrieNode* node = root;
        TrieNode* check = root;
        int xorVal = 0;
        for (int i = maxLen; i >= 0; --i) {
            int bit = (num >> i) & 1;
            if (!node->children[bit]) {
                node->children[bit] = new TrieNode();
            }
            node = node->children[bit];
            if (check->children[1 - bit]) {
                xorVal |= (1 << i);
                check = check->children[1 - bit];
            }
            else {
                check = check->children[bit];
            }
        }
        return xorVal;
    }

private:
    TrieNode* root;
};

class Solution {
public:
    int findMaximumXOR(std::vector<int>& nums) {
        Trie trie;
        int max_xor = 0;
        int maxLen = 0;
        for (int num : nums) {
            maxLen = std::max(maxLen, getMaxBitLength(num));
        }
        for (int num : nums) {
            max_xor = std::max(max_xor, trie.insert(num, maxLen));
        }
        return max_xor;
    }

private:
    int getMaxBitLength(int num) {
        int maxLen = 0;
        while (num > 0) {
            num >>= 1;
            maxLen++;
        }
        return maxLen;
    }
};