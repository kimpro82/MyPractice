# My Verilog Practice

*Verilog* & *SystemVerilog*


## \<List>

- [Type Casting (2022.09.06)](#type-casting-20220906)
- [Array Indexing (2022.09.06)](#array-indexing-20220906)


### Note

- My environment ☞ [JDoodle Online VERILOG Compiler IDE](https://www.jdoodle.com/execute-verilog-online/)


## [Type Casting (2022.09.06)](#list)

- It may be *implicit* to cast `reg` to `integer` in *SystemVerilog*

#### `TypeCasting.sv`
```sv
module TypeCasting();

    reg [10*8:0] arr = "1234567890";
    integer i, sum = 0;

    initial begin
        // Output
        for (i = 0; i < 10; i = i + 1) begin
            // test
            // $write("%0d ", arr[(10-i)*8 - 8 +: 8]);              // 49 50 51 52 53 54 55 56 57 48
            // $write("%0d ", arr[(10-i)*8 - 8 +: 8] - 8'd48);      // 1 2 3 4 5 6 7 8 9 0

            sum = sum + arr[(10-i)*8 - 8 +: 8] - 8'd48;             // 8'd48 can be replaced with just 48
        end
        $display();
        $display("%0d", sum);                                       // 45
        $finish;
    end

endmodule
```
> 45


## [Array Indexing (2022.09.06)](#list)

- Practices of array indexing in *SystemVerilog*

#### `ArrayIndexing1.sv`
&nbsp;&nbsp;· deal with basic `integer` type array
```sv
module ArrayIndexing1();

    integer arr[0:10], i;

    initial begin
        // Input sample values into the array
        for (i = 0; i < 10; i = i + 1) begin
                arr[i] = i;
        end
        // Output
        for (i = 0; i < 10; i = i + 1) begin
                $write("%0d ", arr[i]);
        end
        $display();
        $finish;
    end

endmodule
```
> 0 1 2 3 4 5 6 7 8 9 

#### `ArrayIndexing2.sv`
&nbsp;&nbsp;· deal with `reg` type array, that requires **bit slicing**  
&nbsp;&nbsp;· should call the array's indices from back to front because it follows **little endian**  
&nbsp;&nbsp;&nbsp;&nbsp;(The syntax from **bit slicing** × **little endian** seems so crazy …… !)
```sv
module ArrayIndexing2();

    reg [10*8:0] arr = "abcdefghij";
    integer i;

    initial begin
        // Output
        for (i = 0; i < 10; i = i + 1) begin
                $write("%c ", arr[i*8 +: 8]);
        end
        $display();
        // Output 2
        for (i = 0; i < 10; i = i + 1) begin
                $write("%c ", arr[(10-i)*8 - 8 +: 8]);
        end
        $display();
        $finish;
    end

endmodule
```
> j i h g f e d c b a  
> a b c d e f g h i j 