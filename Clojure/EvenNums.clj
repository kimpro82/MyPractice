; Filtering even numbers
; 2023.09.22

; Define a function to filter even numbers
(defn filter-even [nums]
  ; Use the even? function to filter only even numbers
  (filter even? nums))

; Define the input list of numbers
(def numbers [1 2 3 4 5 6 7 8 9 10])

; Use the filter-even function to filter even numbers
(def even-numbers (filter-even numbers))

; Print the result
(println "Even numbers in the list:")
(println even-numbers)
