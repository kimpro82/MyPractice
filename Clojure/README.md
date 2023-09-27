# [My Clojure Practice](../README.md#my-clojure-practice)

want to get closer to [~~high salary~~](https://insights.stackoverflow.com/survey/2021#section-salary-salary-and-experience-by-language) *Clojure* and *Functional Programming*


### \<List>

- [Sequence Processing (`->>` `reduce` `apply`) (2023.09.26)](#sequence-processing---reduce-apply-20230926)
- [Filtering Even Numbers (2023.09.22)](#filtering-even-numbers-20230922)


## [Sequence Processing (`->>` `reduce` `apply`) (2023.09.26)](#list)

- Practice to deal sequences with `->>` `reduce` `apply`
- Run by *Clojure CLI version 1.11.1.1200* in [Replit](https://replit.com/){:target="_blank"}
- Codes and Output
  <details>
    <summary>Codes : sequence-practice.clj</summary>

  ```clojure
  (ns sequence-practice.ns
    (:require [clojure.string :as str]))
  ```
  ```clojure
  (defn odd-sum
    "Calculate the sum of odd numbers in a sequence."
    [numbers]
    (->>
      numbers
      (filter odd?)
      (reduce +)))

  (defn even-sum
    "Calculate the sum of even numbers in a sequence."
    [numbers]
    (reduce +
      (filter even? numbers)))

  (defn concatenate
    "Concatenate multiple strings with spaces in between."
    [& text]
    (apply str/join " " text))
  ```
  ```clojure
  (def num-sequence (range 1 11))
  (def str-sequence ["Live" "for" "your" "smile" "and" "die" "for" "your" "kiss"])
  ```
  ```clojure
  (defn -main
    "Main function to demonstrate sequence processing."
    []
    (println (odd-sum num-sequence))
    (println (even-sum num-sequence))
    (println (concatenate str-sequence)))

  (-main)
  ```
  </details>
  <details open="">
    <summary>Output</summary>

  ```clojure
  25
  30
  Live for your smile and die for your kiss
  ```
  </details>


## [Filtering Even Numbers (2023.09.22)](#list)

- This was my first *Clojure* code, but not even a warm-up. I need something more legit!
  ```clojure
  (println "Hello World!")
  ```
- Written by *ChatGPT*
- Run by *Clojure CLI version 1.11.1.1200* in [Replit](https://replit.com/)
- Codes and Output
  <details>
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
