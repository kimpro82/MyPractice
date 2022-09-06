// 2022.09.06

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