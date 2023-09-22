# [My Clojure Practice](../README.md#my-clojure-practice)

want to get closer to ~~high salary~~ *Clojure* and *Functional Programming*


### \<List>

- [Filtering Even Numbers (2023.09.22)](#filtering-even-numbers-20230922)


## [Filtering Even Numbers (2023.09.22)](#list)

- This was my first *Clojure* code, but not even a warm-up. I need something more legit!
  ```clojure
  (println "Hello World!")
  ```
- Written by *ChatGPT*
- Run by *Clojure CLI version 1.11.1.1200* in [replit](https://replit.com/)
- Codes and Output
  <details open="">
    <summary>Codes : EvenNums.clj</summary>

  ```clojure
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
  ```
  </details>
  <details open="">
    <summary>Output</summary>

  ```clojure
  (2 4 6 8 10)
  ```
  </details>
