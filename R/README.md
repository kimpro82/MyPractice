# [My R Practice]
- Generating Array and Variables by for Loop.R (2019.12.06)
- Grade_Cancel_Effect.R (2019.07.19)
- CF_Affection.R (2019.05.25)
- Plotting_Fibonacci Tornado.R (2017.05.07)
- Plotting_RGB.R (2017.04.14)

## Generating Array and Variables by for Loop.R (2019.12.06)
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
![generating variable names](https://github.com/kimpro82/My-Practice/blob/master/images/R%2020191206%202.%20generating%20variable%20names.PNG)

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
![generating variable names with considering sort](https://github.com/kimpro82/My-Practice/blob/master/images/R%2020191206%202.1%20generating%20variable%20names%20with%20considering%20sort.PNG)


## Grade_Cancel_Effect.R (2019.07.19)
try simulating grade cancel effect for my sister
1) generate grade data (because my sister's real GPA can't be opened.ㅋㅋ)
2) plot

```R
# 1. generating grade data
# 1.1 grade (4.3 Scale)
g0 <- 1:4
gp <- g0 + 0.3
gm <- g0 - 0.3
g <- sort(c(g0, gp, gm))
g
```
> 0.7 1.0 1.3 1.7 2.0 2.3 2.7 3.0 3.3 3.7 4.0 4.3

```R
# 1.2 more compact
g <- sort(c(1:4, 1:4+0.3, 1:4-0.3))
g
```
> 0.7 1.0 1.3 1.7 2.0 2.3 2.7 3.0 3.3 3.7 4.0 4.3

```R
# 1.3 test simply matching by slicing
g[9]
g[10]
g[9.5]
g[9.152346]
g[9.876312] # It works but calls values smaller (biased)
```
> 3.3  
> 3.7  
> 3.3  
> 3.3  
> 3.3

```R
# 1.4 generate random grade data
set.seed(307)
평점 <- g[rnorm(30, 9.5, 1.5)]
str(평점)
```
> num [1:30] 3.7 3 2.3 2.3 NA 3 3.7 3.3 3 3.3 ...

```R
# 2. plot
len <- length(sort(평점))
windows(width=15, height=8)
  par(mfrow=c(1,2)) 
    hist(평점)
    plot(평점~rank(평점, ties.method="first"),
      xlab = "회색선 : 현재 누적 평점, 빨강선 : 하위 2개 과목 수강취소시 평점, 파랑선 : 하위 5개 과목 수강취소시 평점",
      ylab = "",
      col = c(rep(2,2), rep(4,3), rep(1,len-2-3))[rank(평점, ties.method="first")]
    )
      abline(h=mean((평점), na.rm=TRUE), col="gray")
      abline(h=mean(sort(평점)[3:len]), col="red")
      abline(h=mean(sort(평점)[6:len]), col="blue")
```

![Grade_Cancel_Effect](https://github.com/kimpro82/My-Practice/blob/master/images/2019-07-18%20Grade_Cancel_Effect.png)


```R
# 2.1 values
mean(평점) # NA. na.rm=TRUE 넣어줘야 함
mean(평점, na.rm=TRUE)
mean(sort(평점)[6:len])
mean(sort(평점)[9:len])    
```
> NA  
> 3.293103  
> 3.45  
> 3.514286


## CF_Affection.R (2019.05.25)
For my friend JW Park who wants to measure the affection of TV CF  
It demands simply CF time schedule and target frequency(ex. app download time), not heavy tracker.

```R
# Affection Measurement of TV CFs
# For my frend, JW Park

# 1. Generating Sample Data
n1 = 24*60  # 24 hours * 60 minutes
n2 = 18*60  # not used - suppose 18:00pm is the peak with normal dist.
cf.time = c(6, 12, 18) # suppose cf is played at 6:00, 12:00 and 18:00)
jwp = c("This is", "for my friend", "JW Park") # suprise!

# 1-1. set an uniform dist. frequency of app download
sample.data = runif(10000, 0, n1)/60

# 1-2. add the frequency just after cf
for (i in 1:length(cf.time)) {
  sample.data = c(sample.data, rlnorm(1000, 0, 1) + cf.time[i])
  }
# It can be more plausible with your wit

# 1-3. adjust time ex) 25:00 → 01:00
for (i in 1:length(sample.data)) {
  if (sample.data[i] >= 24) {
    sample.data[i] = sample.data[i] %% 24
  }
}

# 2. plot histogram for comparing before and after ad.
windows(width=12, height=5)
par(mfrow=c(1,3)) 
for (i in 1:length(cf.time)) {
  hist(sample.data, 
       main = jwp[i],
       xlim = range(cf.time[i]-1.5, cf.time[i]+1.5),
       xlab = c("ad at ", cf.time[i]),
       breaks=n1)
}
```

![CF Affection Measurement](https://github.com/kimpro82/My-Practice/blob/master/images/CF_Affection_Measurement_20190525.png)


## Plotting_Fibonacci Tornado.R (2017.05.07)
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

![Fibonacci Tornado](https://github.com/kimpro82/My_Practice/blob/master/images/2017-05-07%2003%3B04%3B10%20Fibonacci%20Tornado.PNG)

#### Bonus. Seeing it's Aproximate to the Golden Ratio.

```R
fibonacci.ratio <- c()

for (k in 1:n) {
  fibonacci.ratio[k] = series[k+1]/series[k]
}

windows(width=10, height=5)
par(mfrow=c(1,2))
plot(fibonacci.ratio[1:12],  type="l",
     main="Aproxmate to the Golden Ratio")
abline(h=1.618, col="red", lty=3)
plot(log(series[1:12]), type="l", 
     main="Natural Logarithm of Fibonacci Series")
```

![Fibonacci Series - Golden Ratio](https://github.com/kimpro82/My_Practice/blob/master/images/2017-05-07%2003%3B03%3B02%20Fibonacci%20Series%20-%20Golden%20Ratio.PNG)


## Plotting_RGB.R (2017.04.14)
- showing RGB color data' distribution by several methods in R
- using `plot3d()`, converting on coordinate plane
- generating RGB data with a sigmoid function

```R
## Install required library packages (only at first)
install.packages("rgl")

## Loading required libraries
library(rgl)
```

#### Generate sample data by Uniform dist.
```R
colors <- matrix(c(runif(3000)), ncol=3)
tail(colors)

plot3d(colors, col=rgb(colors))
```

![RGB_Plotting_2](https://github.com/kimpro82/My_Practice/blob/master/images/2017-04-15%2001%3B33%3B17%20RGB_Plotting_2.PNG)

#### Using Sigmoid function
Reference : https://en.wikipedia.org/wiki/Sigmoid_function
```R
R <- rnorm(1000, 64, 50)
G <- rnorm(1000, 128, 50)
B <- rnorm(1000, 192, 50)

colors <- (tanh(cbind(R,G,B)/255)+1)/2
summary(colors)

plot3d(colors, col=rgb(colors))
```

![RGB_Plotting_5](https://github.com/kimpro82/My_Practice/blob/master/images/2017-04-15%2001%3B59%3B29%20RGB_Plotting_5.PNG)

#### Using Sigmoid function 2 (Plotting on coordinate plane)
Reference : https://github.com/THEjoezack/ColorMine/blob/master/ColorMine/ColorSpaces/Conversions/YxyConverter.cs

```R
R2 = R/(R+G+B)
G2 = G/(R+G+B)
B2 = B/(R+G+B)

colors <- (tanh(cbind(R2,G2,B2))+1)/2
summary(colors)

par(mfrow=c(1,3))
plot(colors[,1], colors[,2], col=rgb(colors))
plot(colors[,2], colors[,3], col=rgb(colors))
plot(colors[,3], colors[,1], col=rgb(colors))
```

![RGB_Plotting_6](https://github.com/kimpro82/My_Practice/blob/master/images/2017-04-15%2002%3B04%3B13%20RGB_Plotting_6.PNG)
