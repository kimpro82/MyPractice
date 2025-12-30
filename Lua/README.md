# [My Lua Practice](../README.md#my-lua-practice)


### **\<References>**

- [www.lua.org](https://www.lua.org/)
- [JDoodle / Online Lua Compiler](https://www.jdoodle.com/execute-lua-online)


### How to Set Up and Run Lua in Bash

- Install
  ```bash
  sudo apt update
  sudo apt install -y lua5.4
  ```

- Run
  ```bash
  lua your_script.lua
  ```


### **\<List>**

- [Multiplication Table (2025.12.30)](#multiplication-table-20251230)


## [Multiplication Table (2025.12.30)](#list)

- This script prints a 9x9 multiplication table in a 3-column block format.
- It demonstrates nested loops, string formatting, and Lua's generic for loops.

### Code and Results
<details>
  <summary>Code : multiplication_table.lua</summary>

  ```lua
  --- Generates and prints the multiplication table
  local function printMultiplicationTable()
      -- Outer loop: Controls the starting point of each block (1, 4, 7)
      for blockStart = 1, 9, 3 do
          -- Middle loop: Controls the multiplier (1 to 9) for each row in the block
          for multiplier = 1, 9 do
              local rowBuffer = ""

              -- Inner loop: Iterates through the 3 specific dan (columns) in the current block
              for dan = blockStart, blockStart + 2 do
                  local result = dan * multiplier

                  -- Format: "dan * multiplier = result" 
                  -- %d: integer, %2d: integer with 2-character width for alignment
                  local entry = string.format("%d * %d = %2d", dan, multiplier, result)

                  -- Append formatted string with spacing between columns
                  rowBuffer = rowBuffer .. entry .. "    "
              end

              print(rowBuffer)
          end

          -- Print a newline between blocks for better readability
          print("")
      end
  end

  -- Execute the function
  printMultiplicationTable()
  ```
</details>
<details open="">
  <summary>Results</summary>

  ```txt
  1 * 1 =  1    2 * 1 =  2    3 * 1 =  3    
  1 * 2 =  2    2 * 2 =  4    3 * 2 =  6    
  1 * 3 =  3    2 * 3 =  6    3 * 3 =  9    
  …… 
  1 * 9 =  9    2 * 9 = 18    3 * 9 = 27    

  4 * 1 =  4    5 * 1 =  5    6 * 1 =  6    
  4 * 2 =  8    5 * 2 = 10    6 * 2 = 12    
  4 * 3 = 12    5 * 3 = 15    6 * 3 = 18    
  ……
  4 * 9 = 36    5 * 9 = 45    6 * 9 = 54    

  7 * 1 =  7    8 * 1 =  8    9 * 1 =  9    
  7 * 2 = 14    8 * 2 = 16    9 * 2 = 18    
  7 * 3 = 21    8 * 3 = 24    9 * 3 = 27    
  ……
  7 * 9 = 63    8 * 9 = 72    9 * 9 = 81    
  ```
</details>
