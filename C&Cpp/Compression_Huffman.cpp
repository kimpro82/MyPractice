// Huffman coding
// 2024.10.09

#include <iostream>
#include <fstream>
#include <queue>
#include <unordered_map>     // Faster than map (does not maintain order)
#include <vector>
#include <string>
#include <bitset>
#include <cmath>             // Include cmath for ceil function
#include <iomanip>           // Include iomanip for std::setprecision

using namespace std;

// Constants for file names
const string INPUT_FILE             = "Data/octobers_song.txt";
const string COMPRESSED_TEXT_FILE   = "Data/huffman_compressed.txt"; // Save compressed data as text
const string COMPRESSED_BINARY_FILE = "Data/huffman_compressed.bin"; // Save compressed data as binary
const string DECOMPRESSED_FILE      = "Data/huffman_decompressed.txt";
const string CODE_TABLE_FILE        = "Data/huffman_table.txt";

// Node for Huffman Tree
struct HuffmanNode
{
    char character;
    int frequency;
    HuffmanNode* left;
    HuffmanNode* right;
    HuffmanNode(char ch, int freq) : character(ch), frequency(freq), left(nullptr), right(nullptr) {}
};

// Compare class for priority queue
struct Compare
{
    bool operator()(HuffmanNode* left, HuffmanNode* right)
    {
        return left->frequency > right->frequency;
    }
};

// Function to generate Huffman Codes
void generateCodes(HuffmanNode* root, string code, unordered_map<char, string>& huffmanCode)
{
    if (!root) return;
    if (!root->left && !root->right)
    {
        huffmanCode[root->character] = code;
    }
    generateCodes(root->left, code + "0", huffmanCode);
    generateCodes(root->right, code + "1", huffmanCode);
}

// Function to build Huffman Tree and generate codes
HuffmanNode* buildHuffmanTree(const unordered_map<char, int>& freqMap, unordered_map<char, string>& huffmanCode)
{
    priority_queue<HuffmanNode*, vector<HuffmanNode*>, Compare> pq;
    for (auto pair : freqMap)
    {
        pq.push(new HuffmanNode(pair.first, pair.second));
    }

    while (pq.size() != 1)
    {
        HuffmanNode* left = pq.top(); pq.pop();
        HuffmanNode* right = pq.top(); pq.pop();
        HuffmanNode* sum = new HuffmanNode('\0', left->frequency + right->frequency);
        sum->left = left;
        sum->right = right;
        pq.push(sum);
    }

    HuffmanNode* root = pq.top();
    generateCodes(root, "", huffmanCode);
    return root;
}

// Function to compress data
string compress(const string& data, const unordered_map<char, string>& huffmanCode)
{
    string compressedData;
    for (char ch : data)
    {
        compressedData += huffmanCode.at(ch);
    }
    return compressedData;
}

// Function to decompress data
string decompress(HuffmanNode* root, const string& compressedData)
{
    string decompressedData;
    HuffmanNode* current = root;
    for (char bit : compressedData)
    {
        if (bit == '0') current = current->left;
        else current = current->right;

        if (!current->left && !current->right)
        {
            decompressedData += current->character;
            current = root;
        }
    }
    return decompressedData;
}

// Function to read input data from a file
string readInputFile(const string& filename)
{
    ifstream file(filename);
    if (!file.is_open())
    {
        cerr << "Error opening file: " << filename << endl;
        exit(1);
    }

    string data, line;
    while (getline(file, line))
    {
        data += line + '\n';
    }
    file.close();
    return data;
}

// Function to write data to a file
void writeToFile(const string& filename, const string& data)
{
    ofstream file(filename);
    if (!file.is_open())
    {
        cerr << "Error writing to file: " << filename << endl;
        exit(1);
    }
    file << data;
    file.close();
}

// Function to write Huffman code table to a file
void writeCodeTable(const string& filename, const unordered_map<char, string>& huffmanCode)
{
    ofstream file(filename);
    if (!file.is_open())
    {
        cerr << "Error writing to file: " << filename << endl;
        exit(1);
    }
    for (auto pair : huffmanCode)
    {
        file << pair.first << ": " << pair.second << endl;
    }
    file.close();
}

// Function to write compressed data as binary
void writeCompressedBinary(const string& filename, const string& compressedData)
{
    ofstream file(filename, ios::binary);
    if (!file.is_open())
    {
        cerr << "Error writing to binary file: " << filename << endl;
        exit(1);
    }

    // Convert the binary string to bytes and write
    bitset<8> bits;
    for (size_t i = 0; i < compressedData.length(); i += 8)
    {
        bits = bitset<8>(compressedData.substr(i, 8));
        file.put(static_cast<char>(bits.to_ulong()));
    }

    // Handle remaining bits
    if (compressedData.length() % 8 != 0)
    {
        string remainingBits = compressedData.substr(compressedData.length() - (compressedData.length() % 8));
        bits = bitset<8>(remainingBits);
        file.put(static_cast<char>(bits.to_ulong()));
    }

    file.close();
}

// Function to write compressed data as text
void writeCompressedText(const string& filename, const string& compressedData)
{
    ofstream file(filename);
    if (!file.is_open())
    {
        cerr << "Error writing to text file: " << filename << endl;
        exit(1);
    }
    file << compressedData; // Write the binary string as is
    file.close();
}

// Function to calculate compression ratio in percentage
void calculateCompressionRatio(const string& originalData, const string& compressedData)
{
    double originalSize = static_cast<double>(originalData.size()); // Original size in bytes
    double compressedSize = static_cast<double>(ceil(compressedData.size() / 8.0)); // Compressed size in bytes
    double compressionRatio = (compressedSize / originalSize) * 100; // Convert to percentage

    cout << "Original size     : " << static_cast<int>(originalSize) << " bytes" << endl;
    cout << "Compressed size   : " << static_cast<int>(compressedSize) << " bytes" << endl;

    // Display rounded compression ratio to two decimal places
    cout << "Compression Ratio : " << round(compressionRatio * 100) / 100 << "%" << endl; // Rounded to 2 decimal places
}

int main()
{
    cout << "<Huffman Coding>" << endl << endl;

    // Step 1: Read input data from file
    string data = readInputFile(INPUT_FILE);

    // Step 2: Count frequency of each character
    unordered_map<char, int> freqMap;
    for (char ch : data)
    {
        freqMap[ch]++;
    }

    // Step 3: Build Huffman Tree and generate code table
    unordered_map<char, string> huffmanCode;
    HuffmanNode* root = buildHuffmanTree(freqMap, huffmanCode);

    // Step 4: Write Huffman code table to a file
    writeCodeTable(CODE_TABLE_FILE, huffmanCode);

    // Step 5: Compress the input data
    string compressedData = compress(data, huffmanCode);

    // Step 6: Write compressed data to a text file
    writeCompressedText(COMPRESSED_TEXT_FILE, compressedData);

    // Step 7: Write compressed data to a binary file
    writeCompressedBinary(COMPRESSED_BINARY_FILE, compressedData);

    // Step 8: Decompress the data
    string decompressedData = decompress(root, compressedData);

    // Step 9: Write decompressed data to a file
    writeToFile(DECOMPRESSED_FILE, decompressedData);

    // Step 10: Calculate and display compression ratio
    calculateCompressionRatio(data, compressedData);

    cout << endl << "Compression and Decompression completed successfully." << endl;
    return 0;
}
