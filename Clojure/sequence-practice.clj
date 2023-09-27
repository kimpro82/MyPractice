;;; Sequence Processing (`->>` `reduce` `apply`) Practice
;;; 2023.09.26

(ns sequence-practice.ns
  (:require [clojure.string :as str]))

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

(def num-sequence (range 1 11))
(def str-sequence ["Live" "for" "your" "smile" "and" "die" "for" "your" "kiss"])

(defn -main
  "Main function to demonstrate sequence processing."
  []
  (println (odd-sum num-sequence))
  (println (even-sum num-sequence))
  (println (concatenate str-sequence)))

(-main)
