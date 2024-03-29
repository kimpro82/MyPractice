// 2022.09.06

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