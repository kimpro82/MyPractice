# [\[My R Practice\]](../README.md#my-r-practice)


## List

- [`List` Practice in R (2022.11.22)](#list-in-r-20221122)
- [`Shiny` - 1st Trial (2022.05.04)](#shiny---1st-trial-20220504)
- [Scatter Points in a Circle (2021.08.16)](#scatter-points-in-a-circle-20210816)
- [Permutations and Combinations (2021.04.05)](#permutations-and-combinations-20210405)
- [Generating Array and Variables by for Loop (2019.12.06)](#generating-array-and-variables-by-for-loop-20191206)
- [Fibonacci Tornado (2017.05.07)](#fibonacci-tornado-20170507)


## [`List` Practice in R (2022.11.22)](#list)

- It's not the linked list, but the data strurture that consists of key & value!

#### `List.r`

  <details>
    <summary>0. Set a sample data</summary>

  ```R
  Chuhan <- list(
      "ruler" = "Liu Bei",
      "general" = c("Guan Yu", "Zhang Fei"),
      "advisor" = "Zhuge Liang"
  )
  Chuhan
  ```

  ```
  $ruler
  [1] "Liu Bei"

  $general
  [1] "Guan Yu"   "Zhang Fei"

  $advisor
  [1] "Zhuge Liang"
  ```
  </details>

  <details>
    <summary>1. Read by key</summary>

  ```R
  Chuhan["ruler"]
  Chuhan[1]                                       # the same with Chuhan["ruler"]
  Chuhan[[1]]

  Chuhan[2]
  Chuhan[2][1]
  Chuhan[[2]][1]

  print(Chuhan[[2]][1])
  cat(Chuhan[[2]][1])
  ```

  ```
  $ruler
  [1] "Liu Bei"

  $ruler
  [1] "Liu Bei"

  [1] "Liu Bei"

  $general
  [1] "Guan Yu"   "Zhang Fei"

  $general
  [1] "Guan Yu"   "Zhang Fei"

  [1] "Guan Yu"

  [1] "Guan Yu"

  Guan Yu
  ```
  </details>

  <details>
    <summary>2. Read by value</summary>

  ```R
  match("Zhuge Liang", Chuhan)                    # get the index of the value
  Chuhan[match("Zhuge Liang", Chuhan)]            # the key & value from the index
  names(Chuhan[match("Zhuge Liang", Chuhan)])     # read only the key
  ```

  ```
  [1] 3

  $advisor
  [1] "Zhuge Liang"

  [1] "advisor"
  ```
  </details>


## [`Shiny` - 1st Trial (2022.05.04)](#list)

- Hello Shiny
- Reference ☞ https://shiny.rstudio.com/tutorial/written-tutorial/lesson1/

```r
if (!requireNamespace("shiny")) install.packages("shiny")
library("shiny")

runExample("01_hello")
```

![Hello Shiny](Images/Shiny_20220505_RunExample.PNG)


## [Scatter Points in a Circle (2021.08.16)](#list)
\* Scatter points in a circle in various ways  
\* using `plotrix`

#### 0. Call "plotrix" library (install if not exist)
  <details>
    <summary>Codes</summary>

  ```R
  if(!requireNamespace("plotrix")) install.packages("plotrix")
  library("plotrix")
  ```
  </details>

#### 1. Monte Carlo method 1
  <details>
    <summary>Codes</summary>

  ```R
  r     = 10
  n     = 30000
  ```
  ```R
  rr    = runif(n, 0, r)                    # rr    : randomly sampled radius
  rrad  = runif(n, 0, 2 * pi)               # rrad  : randomly sampled radian

  x     = rr * cos(rrad)                    # yes, I am a math genius!
  y     = rr * sin(rrad)
  ```
  ```R
  windows(width = 7, height = 7)
  plot(x, y, pch = '.', col = "red",
    main = "1. Monte Carlo method 1")
  abline(v = -round(r*1.3):round(r*1.3), h = -r:r, col = "gray")
  draw.circle(0, 0, r)                      # not exact drawing, crazy
  ```
  </details>

  <img src="Images/Scatter_20210816_1_Monte_Carlo_method_1.png" width="500" height="500" alt = "1. Monte Carlo method 1">

#### 1.1 Fit the circle on the coordinates
  <details>
    <summary>Codes</summary>

  ```R
  windows(width = 7, height = 7)
  plot(x, y, pch = '.', col = "red", asp = 1, # modify asp(aspect ratio) option as 1
    main = "1.1 Monte Carlo method (with modified asp ratio)")
  abline(v = -round(r*1.3):round(r*1.3), h = -r:r, col = "gray")
  draw.circle(0, 0, r)
  ```
  </details>

  <img src="Images/Scatter_20210816_1_1_Fit_the_circle_on_the_coordinates.png" width="500" height="500" alt = "1.1 Fit the circle on the coordinates">

#### 2. Monte Carlo method 2 (disperse the crowded central population)
  <details>
    <summary>Codes</summary>

  ```R
  x   = c(); y = c()
  cnt = 0
  ```
  ```R
  while (cnt < n)                           # insert points only in the circle
  {
    temp = runif(2, -r, r)
    if (temp[1]^2 + temp[2]^2 < r^2)
    {
      x   = c(x, temp[1])
      y   = c(y, temp[2])
      cnt = cnt + 1                         # I miss ++ operator ……
    }
  }
  ```
  ```R
  windows(width = 7, height = 7)
  plot(x, y, pch = '.', col = "red", asp = 1,
    main = "2. Monte Carlo method 2 (disperse the crowded central pop.)")
  abline(v = -round(r*1.3):round(r*1.3), h = -r:r, col = "gray")
  draw.circle(0, 0, r)
  ```
  </details>

  <img src="Images/Scatter_20210816_2_Monte_Carlo_method_2.png" width="500" height="500" alt = "2. Monte Carlo method 2 (disperse the crowded central population)">

#### 3. Points with lattice spacing
  <details>
    <summary>Codes</summary>

  ```R
  x         = c(); y = c()
  area      = pi * r^2
  interval  = sqrt(area / n)
  num       = as.integer(floor(2 * r / interval))
  temp      = c(-r, -r)
  ```
  ```R
  for (i in 1:num)
  {
    temp[1] = temp[1] + interval

    for (j in 1:num)
    {
      temp[2] = temp[2] + interval

      if (temp[1]^2 + temp[2]^2 < r^2)
      {
        x = c(x, temp[1])
        y = c(y, temp[2])
      }
    }

    temp[2] = -r
  }
  ```
  ```R
  length(x); length(y)
  ```
  > [1] 29988  
  > [1] 29988
  ```R
  windows(width = 7, height = 7)
  plot(x, y, pch = '.', col = "red", asp = 1,
    main = "3. Points with lattice spacing")
  abline(v = -round(r*1.3):round(r*1.3), h = -r:r, col = "gray")
  draw.circle(0, 0, r)
  ```
  </details>

<img src="Images/Scatter_20210816_3_Points_with_lattice_spacing.png" width="500" height="500" alt = "3. Points with lattice spacing">

#### 3.1 Points with lattice spacing including outside the circle
  <details>
    <summary>Codes</summary>

  ```R
  x     = c(); y = c(); xyCol = c()
  temp  = c(-r, -r)
  ```
  ```R
  for (i in 1:num)
  {
    temp[1] = temp[1] + interval
    
    for (j in 1:num)
    {
      temp[2] = temp[2] + interval

      x = c(x, temp[1])
      y = c(y, temp[2])

      if (temp[1]^2 + temp[2]^2 < r^2) xyCol = c(xyCol,"red")
      else xyCol = c(xyCol,"blue")
    }

    temp[2] = -r
  }
  ```
  ```R
  length(x); length(y)
  ```
  > [1] 38025  
  > [1] 38025
  ```R
  length(xyCol); length(xyCol[xyCol=="red"]); length(xyCol[xyCol=="blue"])
  ```
  > [1] 38025  
  > [1] 29988  
  > [1] 8037
  ```R
  windows(width = 7, height = 7)
  plot(x, y, pch = '.', col = xyCol, asp = 1,
    main = "3.1 Points with lattice spacing 2")
  abline(v = -round(r*1.3):round(r*1.3), h = -r:r, col = "gray")
  draw.circle(0, 0, r)
  ```
  </details>

<img src="Images/Scatter_20210816_3_1_Points_with_lattice_spacing_2.png" width="500" height="500" alt = "3.1 Points with lattice spacing including outside the circle">


## [Permutations and Combinations (2021.04.05)](#list)
\* get permutations and combinations  
\* using `gtools`

  <details>
    <summary>Factorial</summary>

  ```R
  factorial(4)    # 4! = 4 * 3 * 2 * 1
  ```
  > [1] 24
  </details>

  <details>
    <summary>Permutation</summary>

  ```R
  # loading gtools library
  if (!requireNamespace("gtools")) {
      install.packages('gtools')
  }
  library(gtools)                             # for using permutations() and combinations()
  ```
  ```R
  # ?permutations
  # permutations(n, r, v=1:n, set=TRUE, repeats.allowed=FALSE)
  # n                 Size of the source vector
  # r                 Size of the target vectors
  # v                 Source vector. Defaults to 1:n
  # set               Logical flag indicating whether duplicates should be removed from the source vector v. Defaults to TRUE.
  # repeats.allowed   Logical flag indicating whether the constructed vectors may include duplicated values. Defaults to FALSE.
  ```
  ```R
  balls <- c("Red", "Yellow", "Blue")
  ```
  ```R
  permutations(3, 2, v = balls, repeats.allowed = TRUE)  # 3Π2
  ```
  > [1,] "Blue"   "Blue"  
  > [2,] "Blue"   "Red"  
  > [3,] "Blue"   "Yellow"  
  > [4,] "Red"    "Blue"  
  > [5,] "Red"    "Red"  
  > [6,] "Red"    "Yellow"  
  > [7,] "Yellow" "Blue"  
  > [8,] "Yellow" "Red"  
  > [9,] "Yellow" "Yellow"
  ```R
  permutations(3, 2, v = balls, repeats.allowed = FALSE) # 3P2
  permutations(3, 2, v = balls)
  ```
  > [1,] "Blue"   "Red"  
  > [2,] "Blue"   "Yellow"  
  > [3,] "Red"    "Blue"  
  > [4,] "Red"    "Yellow"  
  > [5,] "Yellow" "Blue"  
  > [6,] "Yellow" "Red"
  </details>

  <details>
    <summary>Combination</summary>

  ```R
  combn(balls, 2)
  ```
  > [1,] "Red"    "Red"  "Yellow"  
  > [2,] "Yellow" "Blue" "Blue"
  ```R
  combinations(3, 2, v = balls, repeats.allowed = TRUE)  # 3H2
  ```
  > [1,] "Blue"   "Blue"  
  > [2,] "Blue"   "Red"  
  > [3,] "Blue"   "Yellow"  
  > [4,] "Red"    "Red"  
  > [5,] "Red"    "Yellow"  
  > [6,] "Yellow" "Yellow"
  ```R
  combinations(3, 2, v = balls, repeats.allowed = FALSE) # 3C2
  ```
  > [1,] "Blue" "Red"  
  > [2,] "Blue" "Yellow"  
  > [3,] "Red"  "Yellow"
  </details>

  <details>
    <summary>Number of cases</summary>

  ```R
  prod(4, 2)                                  # 4P2
  choose(4, 2)                                # 4C2
  ```
  > [1] 8  
  > [1] 6
  </details>


## [Generating Array and Variables by for Loop (2019.12.06)](#list)
answer for a question at chatting room  
\* R array-related data structure is actually defined as vector, matrix and array about each dimension's array.  
\* I call it just 'array' by common mathematical notion here, but it is different from R's strict data structure definition.  

```R
# 1. generating array by for loop
mylist = c()

for (i in 1:10) {
  mylist[i] = i
}

mylist
```
>  [1]  1  2  3  4  5  6  7  8  9 10

```R
# 1.1 generating array more efficiently
mylist2 = c(1:10)

mylist2
```
>  [1]  1  2  3  4  5  6  7  8  9 10

```R
# 2. generating variable names
for (i in 1:10) { 
  name <- paste("mylist_", i, sep = "")
  assign(name, c())
}

```
![generating variable names](Images/Generating_variable_names_20191206_2.png)

```R
# 2.1 generating variable names with considering sort
for (i in 1:10) { 
  if (i < 10) {
    name <- paste("mylist_0", i, sep = "")
  } else {
    name <- paste("mylist_", i, sep = "")
  }
  assign(name, c())
}
```
![generating variable names with considering sort](Images/Generating_variable_names_20191206_2_1.png)

```R
# 2.1.1 code improvement trial of 2.1

name_head_original = "mylist_"

for (i in 1:10) { 
  if (i < 10) {
    name_head = paste(name_head_original, "0", sep = "")
  } else {
    name_head = name_head_original
  }
  name <- paste(name_head, i, sep = "")
  assign(name, c())
}
```
![code improvement trial of 2.1](Images/Generating_variable_names_20191206_2_1_1.PNG)  
Hmm …… is it too much?  
It can be more clearly effective when *n* is larger, but now seems not yet.  


## [Fibonacci Tornado (2017.05.07)](#list)
generating Fibonacci Series and Fibonacci Coordinates by looping

#### 1. Generating Fibonacci Series

```R
series <- c(1,1)
n <- 1000                                     ## defining the length of the series

for (i in 3:n) {
  series[i] <- series[i-2] + series[i-1]
}

head(series)
```

#### 2. Skimming the Movement of Fibonacci Coordinates
```
## The series' flow : (0,0), (1,0), (1,1), (-1,1), (-1,-2), (4,-2), ……

## Each Coordinate's movement :
## 0 : x = 0, y = 0
## 1 : x <- x + 1
## 2 : y <- y + 1
## 3 : x <- x - 2
## 4 : y <- y - 3
## 5 : x <- x + 5
```

There are 4 types of calculation for coordinates' movement.
It seems possible to be realized by looping.

#### 2-1. How sort the types of calculation?
```
## type 1 : %% 4 = 1
## type 2 : %% 4 = 2
## type 3 : %% 4 = 3
## type 4 : %% 4 = 4
```

#### 3. Generating Fibonacci Coordinates by Looping
```R
x <- 0
y <- 0

for (j in 2:n) {
  if (j %% 2 == 1) {
    x[j] <- x[j-1]
    if (j %% 4 == 1) {
      y[j] <- y[j-1] + series[j-1]  ## type 1
    } else {
      y[j] <- y[j-1] - series[j-1]  ## type 3
      }
  }
  else if (j %% 2 == 0) {
    y[j] <- y[j-1]
    if (j %% 4 == 2) {
      x[j] <- x[j-1] + series[j-1]  ## type 2
    } else {
      x[j] <- x[j-1] - series[j-1]  ## type 4
      }
  }
}
```

#### 3-1. Drawing Plot
```R
windows(width=5, height=5)
plot(x[1:12], y[1:12], type="l", 
     main="Fibonacci Tornado")
abline(h=0, v=0, col="gray", lty=3)
```
![Fibonacci Tornado](Images/Fibonacci_20170507_Tornado.PNG)

#### Bonus. Seeing it's Aproximate to the Golden Ratio.

```R
fibonacci.ratio <- c()

for (k in 1:n) {
  fibonacci.ratio[k] = series[k+1]/series[k]
}
```
```R
windows(width=10, height=5)
par(mfrow=c(1,2))
plot(fibonacci.ratio[1:12],  type="l",
     main="Aproxmate to the Golden Ratio")
abline(h=1.618, col="red", lty=3)
plot(log(series[1:12]), type="l", 
     main="Natural Logarithm of Fibonacci Series")
```
![Fibonacci Series - Golden Ratio](Images/Fibonacci_20170507_Series_Golden_Ratio.PNG)