--- Multiplications Table Generator
--
-- This script prints a 9x9 multiplication table in a 3-column block format.
-- It demonstrates nested loops, string formatting, and Lua's generic for loops.
-- @author kimpro82
-- @date 2025.12.30

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
