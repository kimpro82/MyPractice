// 2022.09.06

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