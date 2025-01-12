# [My C/C++ Practice](../README.md#my-cc-practice)

The final destination of programming


### \<List>

- [Diamond Inheritance Problem and Resolution through Virtual Inheritance (2025.01.06)](#diamond-inheritance-problem-and-resolution-through-virtual-inheritance-20250106)
- [Compression Implementation : Huffman Coding (2024.10.09)](#compression-implementation--huffman-coding-20241009)
- [*K&R C* Style Function Declaration (2023.08.20)](#kr-c-style-function-declaration-20230820)
- [Conditional Compile with `#ifdef` (2022.08.30)](#conditional-compile-with-ifdef-20220830)
- [File I/O (2022.08.27)](#file-io-20220827)
- [GCC Optimization Option Practice (2022.08.16)](#gcc-optimization-option-practice-20220816)
- [`printf()` format test (2022.04.25)](#printf-format-test-20220425)
- [Binary Search 1 (2022.04.19)](#binary-search-1-20220419)
- [Binary Search 0 (2022.02.11)](#binary-search-0-20220211)
- [Increment and Decrement Operators (2022.02.01)](#increment-and-decrement-operators-20220201)
- [Prevent Garbage Value (2022.01.21)](#prevent-garbage-value-20220121)
- [Containers : Deque, Stack and Queue (2021.10.14)](#containers--deque-stack-and-queue-20211014)
- [Template (2021.07.23)](#template-20210723)
- [Stack Overflow (2021.05.18)](#stack-overflow-20210518)
- [Hello World (2021.05.12)](#hello-world-20210512)



## [Diamond Inheritance Problem and Resolution through Virtual Inheritance (2025.01.06)](#list)

- What is Diamond Inheritance?
  - Diamond inheritance occurs when a class inherits from two classes that have a common base class. This can lead to ambiguity and duplication of the base class members in the derived class.
- Brief Code Description
  - This code demonstrates the diamond inheritance problem using a simple class hierarchy. It shows how ambiguity arises in a non-virtual inheritance scenario and how virtual inheritance resolves the issue, allowing unambiguous access to base class members.
- Code and Results
  <details>
    <summary>Code : DiamonInheritance.cpp</summary>

  ```cpp
  #include <iostream>
  using namespace std;
  ```
  ```cpp
  class Food 
  {
  public:
      void eat_deliciously() 
      {
          cout << "Yum yum yum! Delicious!" << endl;
      }
  };
  ```
  ```cpp
  // Problematic diamond inheritance
  class Pizza : public Food 
  {
  public:
      void stretch_cheese() 
      {
          cout << "The cheese stretches so much~" << endl;
      }
  };

  class Pasta : public Food 
  {
  public:
      void slurp_noodles() 
      {
          cout << "Slurp! Sucking in the noodles!" << endl;
      }
  };

  class PizzaPasta : public Pizza, public Pasta 
  {
  };
  ```
  ```cpp
  // Solution using virtual inheritance
  class VPizza : virtual public Food 
  {
  public:
      void stretch_cheese() 
      {
          cout << "The cheese stretches so much~" << endl;
      }
  };

  class VPasta : virtual public Food 
  {
  public:
      void slurp_noodles() 
      {
          cout << "Slurp! Sucking in the noodles!" << endl;
      }
  };

  class VPizzaPasta : public VPizza, public VPasta 
  {
  };
  ```
  ```cpp
  int main() 
  {
      // Problematic diamond inheritance
      PizzaPasta weird_dish;
      weird_dish.stretch_cheese();
      weird_dish.slurp_noodles();
      // weird_dish.eat_deliciously();                        // Compilation error: ambiguous call to eat_deliciously()
      weird_dish.Pizza::eat_deliciously();                    // Resolve ambiguity by specifying the class

      cout << "\n";

      // Solution using virtual inheritance
      VPizzaPasta v_weird_dish;
      v_weird_dish.stretch_cheese();
      v_weird_dish.slurp_noodles();
      v_weird_dish.eat_deliciously();                         // No ambiguity, calls Food::eat_deliciously()

      return 0;
  }
  ```
  </details>
  <details>
    <summary>Results</summary>

  ```txt
  The cheese stretches so much~
  Slurp! Sucking in the noodles!
  Yum yum yum! Delicious!

  The cheese stretches so much~
  Slurp! Sucking in the noodles!
  Yum yum yum! Delicious!
  ```
  </details>


## [Compression Implementation : Huffman Coding (2024.10.09)](#list)

- Successfully compressed and decompressed ASCII text data using Huffman coding method
  - In cases where the data is not large enough and the Huffman code table is included in the compressed file, the size after compression may actually be larger
- Reference ☞ [Huffman coding - Wikipedia](https://en.wikipedia.org/wiki/Huffman_coding)
- Code and Results
  - Code : `Compression_Huffman.cpp`
    <details>
      <summary>More</summary>
      <details>
        <summary>Headers and Constants</summary>

      ```cpp
      #include <iostream>
      #include <fstream>
      #include <queue>
      #include <unordered_map>     // Faster than map (does not maintain order)
      #include <vector>
      #include <string>
      #include <bitset>
      #include <cmath>             // Include cmath for ceil function
      #include <iomanip>           // Include iomanip for std::setprecision
      ```
      ```cpp
      using namespace std;
      ```
      ```cpp
      // Constants for file names
      const string INPUT_FILE             = "Data/octobers_song.txt";
      const string COMPRESSED_TEXT_FILE   = "Data/huffman_compressed.txt";
      const string COMPRESSED_BINARY_FILE = "Data/huffman_compressed.bin";
      const string DECOMPRESSED_FILE      = "Data/huffman_decompressed.txt";
      const string CODE_TABLE_FILE        = "Data/huffman_table.txt";
      ```
      </details>
      <details>
        <summary>struct HuffmanNode</summary>

      ```cpp
      // Node for Huffman Tree
      struct HuffmanNode
      {
          char character;
          int frequency;
          HuffmanNode* left;
          HuffmanNode* right;
          HuffmanNode(char ch, int freq) : character(ch), frequency(freq), left(nullptr), right(nullptr) {}
      };
      ```
      </details>
      <details>
        <summary>struct Compare</summary>

      ```cpp
      // Compare class for priority queue
      struct Compare
      {
          bool operator()(HuffmanNode* left, HuffmanNode* right)
          {
              return left->frequency > right->frequency;
          }
      };
      ```
      </details>
      <details>
        <summary>void generateCodes()</summary>

      ```cpp
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
      ```
      </details>
      <details>
        <summary>HuffmanNode* buildHuffmanTree()</summary>

      ```cpp
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
      ```
      </details>
      <details>
        <summary>string compress()</summary>

      ```cpp
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
      ```
      </details>
      <details>
        <summary>string decompress()</summary>

      ```cpp
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
      ```
      </details>
      <details>
        <summary>string readInputFile()</summary>

      ```cpp
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
      ```
      </details>
      <details>
        <summary>void writeToFile()</summary>

      ```cpp
      // Common function to write data to a file
      void writeToFile(const string& filename, const string& data, bool isBinary = false)
      {
          ofstream file(isBinary ? filename : filename.c_str(), isBinary ? ios::binary : ios::out);
          if (!file.is_open())
          {
              cerr << "Error writing to file: " << filename << endl;
              exit(1);
          }

          if (isBinary)
          {
              // Convert the binary string to bytes and write
              bitset<8> bits;
              for (size_t i = 0; i < data.length(); i += 8)
              {
                  bits = bitset<8>(data.substr(i, 8));
                  file.put(static_cast<char>(bits.to_ulong()));
              }

              // Handle remaining bits
              if (data.length() % 8 != 0)
              {
                  string remainingBits = data.substr(data.length() - (data.length() % 8));
                  bits = bitset<8>(remainingBits);
                  file.put(static_cast<char>(bits.to_ulong()));
              }
          }
          else
          {
              file << data; // Write the string as is
          }

          file.close();
      }
      ```
      </details>
      <details>
        <summary>void writeCodeTable()</summary>

      ```cpp
      // Function to write the Huffman code table
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
      ```
      </details>
      <details>
        <summary>void calculateCompressionRatio()</summary>

      ```cpp
      // Function to calculate compression ratio in percentage
      void calculateCompressionRatio(const string& originalData, const string& compressedData)
      {
          int originalSize = static_cast<int>(originalData.size()); // Original size in bytes
          int compressedSize = static_cast<int>(ceil(compressedData.size() / 8.0)); // Compressed size in bytes
          double compressionRatio = (static_cast<double>(compressedSize) / originalSize) * 100; // Convert to percentage

          cout << "Original size     : " << originalSize << " bytes" << endl;
          cout << "Compressed size   : " << compressedSize << " bytes" << endl;

          // Display rounded compression ratio to two decimal places
          cout << "Compression Ratio : " << round(compressionRatio * 100) / 100 << "%" << endl; // Rounded to 2 decimal places
      }
      ```
      </details>
      <details>
        <summary>int main()</summary>

      ```cpp
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
          writeToFile(COMPRESSED_TEXT_FILE, compressedData);

          // Step 7: Write compressed data to a binary file
          writeToFile(COMPRESSED_BINARY_FILE, compressedData, true);

          // Step 8: Decompress the data
          string decompressedData = decompress(root, compressedData);

          // Step 9: Write decompressed data to a file
          writeToFile(DECOMPRESSED_FILE, decompressedData);

          // Step 10: Calculate and display compression ratio
          calculateCompressionRatio(data, compressedData);

          cout << endl << "Compression and Decompression completed successfully." << endl;
          return 0;
      }
      ```
      </details>
    </details>
  - Sameple Text : `octobers_song.txt`
    <details open="">
      <summary>(Lyrics) "October's Song" from 《The Gang's All Here》 (2022) by Skid Row</summary>

    ```txt
    Mother step to the light that's before you
    Mother change in the seasons I see
    Winter's on the rise
    Autumn still in my eyes
    Reborn as daylight dies
    ……
    ```
    </details>
  - Results
    <details open="">
      <summary>Console Output</summary>

    ```txt
    <Huffman Coding>

    Original size     : 1092 bytes
    Compressed size   : 592 bytes
    Compression Ratio : 54.21%

    Compression and Decompression completed successfully.
    ```
    </details>
    <details open="">
      <summary>Huffman Code Table</summary>

    ```txt
    d: 11010
    f: 1100111
    A: 110011011
    p: 11001100
    r: 110010
    h: 11011
    ……
    ```
    </details>


## [*K&R C* Style Function Declaration (2023.08.20)](#list)

- A comparison between the *K&R* style and *ANSI C* style function declaration methods
- What is *K&R* C? → [[Wikipedia] C (programming language) > History > K&R C](https://en.wikipedia.org/wiki/C_(programming_language)#K&R_C)
  <details>
    <summary>According to ChatGPT</summary>

    > - Pros:
    >   - Conciseness: The K&R style reduces the length of the function declaration, making it more concise.
    >
    > - Cons:
    >   - Readability: Without parameter names, it can be difficult to understand the purpose of each parameter.
    >   - Lack of Type Safety: Since only data types are mentioned, there's no type checking for function arguments.
    >   - Maintenance: If parameter order or types change, you need to update both the declaration and definition.
    >
    > - Conclusion:  
    >   - While the K&R style was used in early C development due to limitations of the time, the ANSI C style has become the recommended practice. It improves code readability, provides better type safety, and enhances maintainability. The ANSI C style also aligns with modern coding standards and best practices, making it the preferred choice for most developers today.
  </details>
- Example
  <details open="">
    <summary>Code : KnrFunctionSyntax.c</summary>

  ```c
  int add(a, b)                           // K&R 스타일 함수 선언: 매개변수 이름을 생략하고 데이터 타입만 표시
      int a, b;                           // 실제 매개변수 이름과 데이터 타입은 별도로 기술
  {
      return a + b;
  }
  ```
  ```c
  int add2(int a, int b)                  // ANSI C 스타일 함수 선언: 매개변수와 데이터 타입을 함께 명시
  {
      return a + b;
  }
  ```
  ```c
  int main()
  {
      int result = add(5, 3);              // K&R 스타일 함수 호출
      int result2 = add2(5, 3);            // ANSI C 스타일 함수 호출

      printf("Result  (K&R) : %d\n", result);
      printf("Result2 (ANSI): %d\n", result2);

      return 0;
  }
  ```
  </details>
  <details open="">
    <summary>Output</summary>

  Surprisingly, the *K&R* style code has been compiled successfully even in recent compilation environments. The above code was compiled using MinGW.org GCC-6.3.0-1 and executed without any issues.
  ```c
  Result  (K&R) : 8
  Result2 (ANSI): 8
  ```
  </details>


## [Conditional Compile with `#ifdef` (2022.08.30)](#list)

- Can determine where to compile or not with the preprocessors `#ifdef` ~ `#endif`
- It seems very useful! I love it!
- References :
  - 조건부 컴파일 (TCP School) http://www.tcpschool.com/c/c_compile_condCompile
  - 조건부 컴파일 (C언어 / Wikidocs) https://wikidocs.net/13348
  - (C/C++) 조건부 컴파일로 디버깅용 출력 한방에 없애기 (BOJ) https://www.acmicpc.net/blog/view/110
- ※ When the macro `fileio` is on, *Ahnlab V3 Lite* recognizes `a.exe` as a malware!

  <details>
    <summary>Code : ConditionalCompile.c</summary>

  ```c
  int main()
  {
      char txt[] = "I am your father.\n";

      #ifdef fileio
          char fileName[] = "ConditionalCompile.txt";

          FILE* pf = fopen(fileName, "w");       // w : make a new empty file
          fprintf(pf, txt);
          fclose(pf);

          printf("%s has been generated.\n", fileName);
      #else
          printf("%s", txt);
      #endif

      return 0;
  }
  ```
  </details>
  <details open="">
    <summary>Code : ConditionalCompile.cpp</summary>

  ```cpp
  #include <iostream>
  #include <fstream>
  #define endl '\n'

  using namespace std;
  ```
  ```cpp
  int main()
  {
      string txt = "I am your father.";

      #ifdef fileio
          ofstream ofs;
          string fileName = "ConditionalCompile.txt";
          ofs.open(fileName, ios::out);           // ios::out : make a new empty file
          ofs << txt << endl;
          ofs.close();
          cout << fileName << " has been generated." << endl;
      #else
          cout << txt << endl;
      #endif

      return 0;
  }
  ```
  </details>
  <details>
    <summary>Commands : ConditionalCompile_c.bat</summary>

  The couple of files have the same results.
  ```bat
  :: #ifdef fileio
  gcc -Dfileio conditionalcompile.c
  a

  :: #else
  gcc conditionalcompile.c
  a
  ```
  > ConditionalCompile.txt has been generated.  
  > I am your father.
  </details>
  <details open="">
    <summary>Commands : ConditionalCompile_cpp.bat</summary>

  ```bat
  :: #ifdef fileio
  g++ -Dfileio conditionalcompile.cpp
  a

  :: #else
  g++ conditionalcompile.cpp
  a
  ```
  > ConditionalCompile.txt has been generated.  
  > I am your father.
  </details>
  <details open="">
    <summary>Results : ConditionalCompile.txt</summary>

  ```txt
  I am your father.

  ```
  </details>


## [File I/O (2022.08.27)](#list)

- A practice of file input/ouput in **C/C++**
- Further discussion : how to read *Korean* string from external file

  <details>
    <summary>Code : FileIO.c</summary>

  ```c
  int main()
  {
      // Write file
      FILE* pf1 = fopen("FileIO.txt", "w");       // w : make a new empty file
      fprintf(pf1, "My wife is crazy.\n");
      fprintf(pf1, "Really crazy.\n");
      fclose(pf1);

      // Read file
      FILE* pf2 = fopen("FileIO.txt", "r");       // r : read-only
      char txt[__INT16_MAX__];
      fread(txt, 1, __INT16_MAX__, pf2);
      printf("%s", txt);
      fclose(pf2);

      return 0;
  }
  ```
  </details>
  <details open="">
    <summary>Code : FileIO.cpp</summary>

  ```cpp
  #include <iostream>
  #include <fstream>
  #define endl '\n'

  using namespace std;
  ```
  ```cpp
  int main()
  {
      // Write file
      ofstream ofs;
      ofs.open("FileIO.txt", ios::out);           // ios::out : make a new empty file
      ofs << "My wife is crazy." << endl;
      ofs << "Really crazy." << endl;
      ofs.close();

      // Read file
      ifstream ifs;
      string line;
      ifs.open("FileIO.txt", ios::in);            // ios::in : read-only
      while(getline(ifs, line)) cout << line << endl;
      ifs.close();

      return 0;
  }
  ```
  </details>
  <details open="">
    <summary>Results : FileIO.txt</summary>

  ```txt
  My wife is crazy.
  Really crazy.

  ```
  </details>


## [GCC Optimization Option Practice (2022.08.16)](#list)

- Generate many assembly(`.s`) files with various optimization options in `GCC`
- But I've just realized that I'm not ready yet to read their assembly code ……
- However, I've found at least that the generally known properties of the optimization options are not fixed absolutely.  
  (For example, `Os` is known as smaller code size but it sometimes returns rather larger one.)
- References :  
  · https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html  
  · https://wiki.kldp.org/wiki.php/GccOptimizationOptions  
  · https://www.rapidtables.com/code/linux/gcc/gcc-o.html

  <details open="">
    <summary>Code : OptimizePractice.c</summary>

  ```c
  void operate(int i, int* p)
  {
      if (i % 2 != 0) (*p)++;
  }
  ```
  ```c
  int main()
  {
      int num = 0;
      int* p = &num;

      for (int i = 0; i < 10; i++) operate(i, p);

      printf("%d\n", num);

      return 0;
  }
  ```
  > 5
  </details>
  <details>
    <summary>Code : OptimizePractice.bat (Old)</summary>

  ```batch
  gcc -O0 -S OptimizePractice.c -o OptimizePractice_O0.s
  gcc -O1 -S OptimizePractice.c -o OptimizePractice_O1.s
  gcc -O2 -S OptimizePractice.c -o OptimizePractice_O2.s
  gcc -O3 -S OptimizePractice.c -o OptimizePractice_O3.s
  gcc -Os -S OptimizePractice.c -o OptimizePractice_Os.s
  gcc -Ofast -S OptimizePractice.c -o OptimizePractice_Ofast.s
  ```
  </details>
  <details open="">
    <summary>Code : OptimizePractice.bat (New)</summary>

  ```batch
  @echo off

  set name=OptimizePractice
  set options=O0 O1 O2 O3 Os Ofast
  @REM There should be no space on the both side of "="

  for %%i in (%options%) do (
      @REM echo %%i
      gcc -%%i -S %name%.c -o %name%_%%i.s
  )
  ```
  </details>

## [`printf()` format test (2022.04.25)](#list)

- I wrote the below code in [*GCJ 2022 Round 1B*](https://github.com/kimpro82/MyCodingContest/tree/master/Google/CodeJam/2022%20Round%201B#google-code-jam-2022---round-1b) - [*Controlled Inflation*](https://github.com/kimpro82/MyCodingContest/tree/master/Google/CodeJam/2022%20Round%201B#controlled-inflation-14pts-21pts), but there's some struggle with `printf()`'s format `%d` `%ld` `%lld`.  
  (All the variables are declared as *long long* type.)
  ```cpp
  // test
  // printf("min : %lld, max : %lld, dist : %lld, sum1 : %lld, sum2 : %lld\n", min, max, dist, sum1, sum2);
  ```
- I will never miss the criminal!

  <details open="">
    <summary>Code : printf.c & printf.cpp</summary>

  The code except each of the headers are the same.
  ```c
  int main()
  {
      char text[] = "%d %ld %lld\n";
      printf(text, __SCHAR_MAX__, __SCHAR_MAX__, __SCHAR_MAX__);
      printf(text, __INT8_MAX__, __INT8_MAX__, __INT8_MAX__);
      printf(text, __SHRT_MAX__, __SHRT_MAX__, __SHRT_MAX__);
      printf(text, __INT16_MAX__, __INT16_MAX__, __INT16_MAX__);
      printf(text, __INT_MAX__, __INT_MAX__, __INT_MAX__);
      printf(text, __LONG_MAX__, __LONG_MAX__, __LONG_MAX__);
      printf(text, __INT32_MAX__, __INT32_MAX__, __INT32_MAX__);
      printf(text, __LONG_LONG_MAX__, __LONG_LONG_MAX__, __LONG_LONG_MAX__);
      printf(text, __INT64_MAX__, __INT64_MAX__, __INT64_MAX__);

      return 0;
  }
  ```
  </details>
  <details open="">
    <summary>Results</summary>

  ```
  127 127 8458399796925825151
  127 127 8458399796925825151
  32767 32767 8458399796925857791
  32767 32767 8458399796925857791
  2147483647 2147483647 8458399799073308671
  2147483647 2147483647 8458399799073308671
  2147483647 2147483647 8458399799073308671
  -1 2147483647 9223372036854775807
  -1 2147483647 9223372036854775807
  ```
  </details>

- Implications
  - `%d` and `%ld` don't make trouble with reading `char` or `short`, but `%lld` is something special.
  - Make sure `int` == `long` == `int32` in the current standard environment
  - **-1** seems interesting. `__LONG_LONG_MAX__`(== `__INT64_MAX__`) is `0 111 …… 1111`, but `%d` reads only partial digits from it.  
    And the partial number `1 111 …… 1111` indicates -1 as [2's complement](https://en.wikipedia.org/wiki/Two%27s_complement).


## [Binary Search 1 (2022.04.19)](#list)

- I tried this code with [Binary Search 0 (2022.02.11)](#binary-search-0-20220211) about the same time,  
  but couldn't find why the traversal results are wrong.
- There was a crazy mistake …… It stole my two months!

  <details>
    <summary>Code : BinarySearch.c</summary>

  ```c
  #include <stdio.h>
  #include <stdlib.h>                             // malloc()
  ```
  ```c
  typedef struct _tNode                           // It makes using struct easier to declare it with typedef
  {
      int value;
      struct _tNode* left;                        // Node* left : why does it not work?
      struct _tNode* right;                       // should be declared as a pointer
  } Node;
  ```
  ```c
  Node* insert(Node* root, int value)             // The location of '*' doesn't matter
  {
      if (root == NULL)
      {
          Node* root = malloc(sizeof(Node));      // malloc : instead of `new` in C++
          root->value = value;
          root->left = NULL;
          root->right = NULL;

          return root;
      }
      else
      {
          if (root->value > value) root->left = insert(root->left, value);
          else root->right = insert(root->right, value);
      }

      return root;
  }

  Node* delete(Node* root, int value) 
  {
      if (root == NULL) return root;

      if (root->value > value) root->left = delete(root->left, value);
      else if (root->value < value) root->right = delete(root->right, value);
      else
      {
          // ing~~~
      }

      return root;
  }
  ```
  `delete()` is still imcomplete.
  ```c
  void preOrder(Node* root)
  {
      if (root == NULL) return;

      printf("%d ", root->value);
      preOrder(root->left);
      preOrder(root->right);
  }

  void inOrder(Node* root)
  {
      if (root == NULL) return;

      inOrder(root->left);
      printf("%d ", root->value);
      inOrder(root->right);
  }

  void postOrder(Node* root)
  {
      if (root == NULL) return;

      postOrder(root->left);
      postOrder(root->right);
      printf("%d ", root->value);
  }
  ```
  I wrote all the inside function names as `preOrder()` …… crazy~~~
  ```c
  int main()
  {
      Node* root = NULL;

      int arr[6] = {6, 3, 4, 7, 13, 10};
      int len = sizeof(arr) / sizeof(int);
      for (int i = 0; i < len; i++) root = insert(root, arr[i]);

      printf("Preorder traversal : ");
      preOrder(root);
      putchar('\n');

      printf("Inorder traversal : ");
      inOrder(root);
      putchar('\n');

      printf("Postorder traversal : ");
      postOrder(root);
      putchar('\n');

      return 0;
  }
  ```
  </details>
  <details open="">
    <summary>Results</summary>

  ```
  Preorder traversal : 6 3 4 7 13 10
  Inorder traversal : 3 4 6 7 10 13
  Postorder traversal : 4 3 10 13 7 6
  ```
  </details>


## [Binary Search 0 (2022.02.11)](#list)

- hope `binary_search()` in *C++* would be a free lunch ……  
  but it just returns only `true` or `false` depending on the element's presence.
- Of course, this function seems very **powerful** for sorted data.

  <details open="">
    <summary>Code : BinarySearch.cpp</summary>

  ```cpp
  #include <iostream>
  #include <vector>
  #include <algorithm>
  ```
  ```cpp
  int main()
  {
      vector<int> vec = {2, 4, 6, 8, 10, 12};                     // should be sorted
      vector<int> vec2 = {3, 6, 9, 12};

      for (auto v : vec2)
      {
          // binary_search() : a function to just return true or false if the value exists
          bool ans = binary_search(vec.begin(), vec.end(), v);
          cout << v << ' ' << ans << endl;
      }

      return 0;
  }
  ```
  </details>
  <details open="">
    <summary>Results</summary>

  ```
  3 0
  6 1
  9 0
  12 1
  ```
  </details>


## [Increment and Decrement Operators (2022.02.01)](#list)

- Some extreme(?) experiments about `++` and `--` operators

  <details open="">
    <summary>Code : IncDecOperator.c</summary>

  ```c
  int main()
  {
      int a = 1, b = 1, c = 1, d = 1, e = 1, f = 1;

      a++;
      --b;
      // no problem

      c = ++c;
      d = d++;
      // gcc - no problem
      // clang - warning: multiple unsequenced modifications to 'c' [-Wunsequenced]

      // e = ++e--;
      // ++e--;
      // f++--++;
      // f++++++;
      // gcc - error: lvalue required as increment operand
      // clang - error: expression is not assignable

      printf("Good-bye %d %d %d %d\n", a, b, c, d);

      return 0;
  }
  ```
  </details>
  <details>
    <summary>Results</summary>

  ```
  Good-bye 2 0 2 1
  ```
  </details>


## [Prevent Garbage Value (2022.01.21)](#list)

- The way to prevent variable declaration from garbage value

  <details open="">
    <summary>Code : PreventGarbageValue.cpp</summary>

  ```cpp
  int main()
  {
      int garbage;
      int noGarbage{};

      cout << garbage << endl;
      cout << noGarbage << endl;

      return 0;
  }
  ```
  </details>
  <details open="">
    <summary>Results</summary>

  ```
  2686816
  0
  ```
  </details>


## [Containers : Deque, Stack and Queue (2021.10.14)](#list)

- `STL` Practice : Container `Deque` and its adaptors `Stack` and `Queue`
  - Especially `Deque` is something greater than `vector` and `list`
  - `Prior Queue` that is also one of the container adaptor from Deque and consists of `heap` will be continued ……
- Reference ☞ [코딩 테스트를 위한 자료 구조와 알고리즘 with C++ (길벗, 2020)](https://github.com/gilbutITbook/080239)

  <details>
    <summary>Code : Containers_Deque.cpp</summary>

  ```cpp
  #include <deque>
  ```
  ```cpp
  void print(deque<int> deq)
  {
      for (auto it = deq.begin(); it != deq.end(); it++) cout << *it << ' ';
      cout << endl;
  }
  ```
  ```cpp
  int main()
  {
      deque<int> deq {1, 2, 3, 4, 5};
      print(deq);

      deq.push_front(0);
      print(deq);

      deq.push_back(6);
      print(deq);

      deq.insert(deq.begin() + 2, 10);
      print(deq);

      deq.pop_back();
      print(deq);

      deq.pop_front();
      print(deq);

      deq.erase(deq.begin() + 1);
      print(deq);

      deq.erase(deq.begin() + 3, deq.end());
      print(deq);

      // emplace()?
      // emplace_front()?
      // emplace_back()?

      return 0;
  }
  ```
  > 1 2 3 4 5  
  > 0 1 2 3 4 5  
  > 0 1 2 3 4 5 6  
  > 0 1 10 2 3 4 5 6  
  > 0 1 10 2 3 4 5  
  > 1 10 2 3 4 5  
  > 1 2 3 4 5  
  > 1 2 3  
  </details>
  <details>
    <summary>Code : Containers_Stack.cpp</summary>

  ```cpp
  #include <stack>
  ```
  ```cpp
  void print(stack<int> stk)
  {
      if (stk.empty()) cout << "The stack is empty." << endl;
      else
      {
          while (!stk.empty())
          {
              cout << stk.top() << ' ';
              stk.pop();
          }
          cout << endl;
      }
  }
  ```
  ```cpp
  int main()
  {
      stack<int> stk ({1, 2, 3});     // check the different way to declare with initial elements from deque and so on
      print(stk);

      stk.push(4);
      print(stk);

      stk.push(5);
      print(stk);

      stk.pop();
      stk.pop();
      print(stk);

      stk.pop();
      stk.pop();
      stk.pop();
      print(stk);

      // Any other methods?

      return 0;
  }
  ```
  > 3 2 1  
  > 4 3 2 1  
  > 5 4 3 2 1  
  > 3 2 1  
  > The stack is empty.
  </details>
  <details>
    <summary>Code : Containers_Queue.cpp</summary>

  ```cpp
  #include <queue>
  ```
  ```cpp
  void print(queue<int> q)
  {
      if (q.empty()) cout << "The que is empty." << endl;
      else
      {
          while (!q.empty())
          {
              cout << q.front() << ' ';
              q.pop();
          }
          cout << endl;
      }
  }
  ```
  ```cpp
  int main()
  {
      queue<int> q ({1, 2, 3});   // don't forget ()!
      print(q);

      q.push(4);
      print(q);

      q.push(5);
      print(q);

      q.pop();
      q.pop();
      print(q);

      q.pop();
      q.pop();
      q.pop();
      print(q);

      return 0;
  }
  ```
  > 1 2 3  
  > 1 2 3 4  
  > 1 2 3 4 5  
  > 3 4 5  
  > The que is empty.
  </details>


## [Template (2021.07.23)](#list)

- Significantly advanced code using **template** from the previous `StackOverflow.cpp`
- I am so proud!

  <details>
    <summary>Code : Template.cpp</summary>

  ```cpp
  template <class T>
  // void next (T a) cout << a++ << endl;       // can't write in a line without {}
  void next (T a)
  {
      if (typeid(a) == typeid((char) 'a') || typeid(a) == typeid((unsigned char) 'a'))
      {
          cout << typeid(a).name() << " : " << (int) a << " + 1 = " << (int) ++a << " (converted to ASCII value)" << endl;    
      } else
      {
          cout << typeid(a).name() << " : " << a << " + 1 = " << ++a << endl;
      }
      // there will be more alternatives like type_info and so on ……
  }
  ```
  ```cpp
  int main()
  {
      next((char) CHAR_MAX);
      next((unsigned char) UCHAR_MAX);
      next((short) SHRT_MAX);
      next((unsigned short) USHRT_MAX);
      next((int) INT_MAX);
      next((unsigned int) UINT_MAX);
      next((bool) 1);                     // warning: use of an operand of type 'bool' in 'operator++' is deprecated

      return 0;
  }
  ```
  </details>
  <details open="">
    <summary>Results</summary>

  > c : 127 + 1 = -128 (converted to ASCII value)  
  > h : 255 + 1 = 0 (converted to ASCII value)  
  > s : 32767 + 1 = -32768  
  > t : 65535 + 1 = 0  
  > i : 2147483647 + 1 = -2147483648  
  > j : 4294967295 + 1 = 0  
  > b : 1 + 1 = 1
  </details>


## [Stack Overflow (2021.05.18)](#list)

- "Let's conquer the **stack overflow** problem!"
- …… a stupid conquerer who didn't know **template** and **generic function** said.
- Can he learn them or still stay in beginner's swamps? To be continued …… 

  <details>
    <summary>Code : StackOverflow.cpp</summary>

  ```cpp
  #include <iostream>

  using namespace std;

  int main()
  {
      // char : -128 to 127 (-2^7 to 2^7 - 1)
      char chr1 = 126;
      char chr2 = chr1 + 1;
      char chr3 = chr2 + 1;
      cout << "char (" << sizeof(char) << ") : " << (short)chr1 << " + 1 = " << (short)chr2 << endl;          // 127
      cout << "char (" << sizeof(char) << ") : " << (short)chr2 << " + 1 = " << (short)chr3 << endl << endl;  // -128

      // unsigned char : 0 to 255 (0 to 2^8 - 1)
      unsigned char uChr1 = 254;
      unsigned char uChr2 = uChr1 + 1;
      unsigned char uChr3 = uChr2 + 1;
      cout << "unsigned char (" << sizeof(unsigned char) << ") : " << (short)uChr1 << " + 1 = " << (short)uChr2 << endl;          // 255
      cout << "unsigned char (" << sizeof(unsigned char) << ") : " << (short)uChr2 << " + 1 = " << (short)uChr3  << endl << endl; // 0

      // short : -32768 to 32767 (-2^15 to 2^15 - 1)
      short shrt1 = 32766;
      short shrt2 = shrt1 + 1;
      short shrt3 = shrt2 + 1;
      cout << "short (" << sizeof(short) << ") : " << shrt1 << " + 1 = " << shrt2 << endl;            // 32767
      cout << "short (" << sizeof(short) << ") : " << shrt2 << " + 1 = " << shrt3 << endl << endl;    // -32768

      // unsigned short : 0 to 65535 (0 to 2^16-1)
      unsigned short uShrt1 = 65534;
      unsigned short uShrt2 = uShrt1 + 1;
      unsigned short uShrt3 = uShrt2 + 1;
      cout << "unsigned short (" << sizeof(unsigned short) << ") : " << uShrt1 << " + 1 = " << uShrt2 << endl;            // 65535
      cout << "unsigned short (" << sizeof(unsigned short) << ") : " << uShrt2 << " + 1 = " << uShrt3 << endl << endl;    // 0

      // int : -214748368 to 214748367 (-2^31 to 2^31 - 1)
      int int1 = 2147483646;
      int int2 = int1 + 1;
      int int3 = int2 + 1;
      cout << "int (" << sizeof(int) << ") : " << int1 << " + 1 = " << int2 << endl;          // 2147483647
      cout << "int (" << sizeof(int) << ") : " << int2 << " + 1 = " << int3 << endl << endl;  // -2147483648
      
      // unsigned int : 0 to 4294967295 (0 to 2^32 -1)
      unsigned int uIint1 = 4294967294;
      unsigned int uIint2 = uIint1 + 1;
      unsigned int uIint3 = uIint2 + 1;
      cout << "unsigned int (" << sizeof(unsigned int) << ") : " << uIint1 << " + 1 = " << uIint2 << endl;            // 4294967295
      cout << "unsigned int (" << sizeof(unsigned int) << ") : " << uIint2 << " + 1 = " << uIint3 << endl << endl;    // 0

      // bool : 0 to 1
      bool bl1 = false;
      bool bl2 = bl1 + 1;
      bool bl3 = bl2 + 1;
      cout << "bool (" << sizeof(bool) << ") : " << bl1 << " + 1 = " << bl2 << endl;          // 1
      cout << "bool (" << sizeof(bool) << ") : " << bl2 << " + 1 = " << (bool)(bl3) << endl;  // 1

      return 0;
  }
  ```
  </details>
  <details open="">
    <summary>Results</summary>

  > char (1) : 126 + 1 = 127  
  > char (1) : 127 + 1 = -128  
  >  
  > unsigned char (1) : 254 + 1 = 255  
  > unsigned char (1) : 255 + 1 = 0  
  >  
  > short (2) : 32766 + 1 = 32767  
  > short (2) : 32767 + 1 = -32768  
  >  
  > unsigned short (2) : 65534 + 1 = 65535  
  > unsigned short (2) : 65535 + 1 = 0  
  >  
  > int (4) : 2147483646 + 1 = 2147483647  
  > int (4) : 2147483647 + 1 = -2147483648  
  >  
  > unsigned int (4) : 4294967294 + 1 = 4294967295  
  > unsigned int (4) : 4294967295 + 1 = 0  
  >  
  > bool (1) : 0 + 1 = 1  
  > bool (1) : 1 + 1 = 1
  </details>


## [Hello World (2021.05.12)](#list)

- My first run of **`C`/`C++`** code in **Visual Studio Code**
  - Environmental setting was harder than coding
  - Find how to **complie** and **run** in cosole (rather easier than VS Code menu)
  - `gcc` (for `C`) and `g++` (for `C++`) seem not so different to each other

  <details>
    <summary>Code : IamYourFather_c.c</summary>

  ```c
  #include <stdio.h>
  #include <windows.h>    // for using system()

  int main()
  {
      printf("I am your father.\n");
      // system("pause");
      return 0;
  }
  ```
  </details>
  <details>
    <summary>Command Lines to Run IamYourFather_c.c</summary>

  ```
  gcc --help
  gcc -S IamYourFather_c.c
  gcc IamYourFather_c.c -o IamYourFather_c.exe
  ```
  ```
  .\IamYourFather_c
  ```
  > I am your father.
  </details>
  <details open="">
    <summary>Code : IamYourFather_cpp.cpp</summary>

  ```cpp
  #include <iostream>

  using namespace std;

  int main()
  {
      cout << "I am your father." << endl;
      // system("pause");
      return 0;
  }
  ```
  </details>
  <details open="">
    <summary>Command Lines to Run IamYourFather_cpp.cpp</summary>

  ```
  g++ --help
  g++ -S IamYourFather_cpp.cpp
  g++ IamYourFather_cpp.cpp -o IamYourFather_cpp.exe
  ```
  ```
  .\IamYourFather_cpp
  ```
  > I am your father.
  </details>
