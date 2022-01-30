# [My Web Practice]

HTML, CSS and JavaScript


### List

- [Bootstrap : Magic Stick (2022.01.28)](/Web#bootstrap--magic-stick-20220128)
- [Script Tag's Location (2022.01.02)](/Web#script-tags-location-20220102)
- [6th Wedding Anniversary (2021.03.07)](/Web#6th-wedding-anniversary-20210307)
- [5th Wedding Anniversary 2 (2020.03.11)](/Web#5th-wedding-anniversary-2-20200311)
- [5th Wedding Anniversary (2020.03.07)](/Web#5th-wedding-anniversary-20200307)
- [Colorful Show (2020.03.04)](/Web#colorful-show-20200304)
- [Ganzi (2017.04.03)](/Web#ganzi-20170403)


## [Bootstrap : Magic Stick (2022.01.28)](#list)
- A practice of **Bootstrap** (5.1.3) : use `container-fluid` `mx` `my` `row` `col`
- Originally I was going to apply **grid**, but to fail.

![Bootstrap : Magic Stick](Image/BootstrapMagicStick.gif)

#### BootstrapMagicStick.html
```html
<!DOCTYPE html>

<html>

    <head>
        <meta charset="UTF-8">
        <title>Magic Stick by Bootstrap</title>
        <link href="./bootstrap5/css/bootstrap.min.css" rel="stylesheet" type="text/css">
        <script defer src="BootstrapMagicStick.js" type="text/javascript"></script>
    </head>

    <body>
        <div class="container-fluid mx-3 my-5">
            <div class="row">
                <div class="col bg-primary text-center">
                    <h1><span id="text">여의봉아 여의봉아</span></h1>
                </div>
            </div>
        </div>
    </body>

</html>
```

#### BootstrapMagicStick.js
```js
var direction = false;
var width = 400;
// console.log(width);

function resize()
{
    // Set direction and text content
    if (width < 450 && direction == false)
    {
        direction = !direction;
        document.getElementById("text").textContent = "길어져라 길어져라";
    }
    else if (width > 1000 && direction == true)
    {
        direction = !direction;
        document.getElementById("text").textContent = "짧아져라 짧아져라";
    }

    // Modify the body's width
    if (direction == true) { document.body.style.width = (Number(width) + 50) + 'px' }
    else  { document.body.style.width = (Number(width) - 50) + 'px'}

    width = document.body.style.width.replace(/[^0-9]/g, "");
    console.log(direction, width);
}

setInterval(resize, 100);
```


## [Script Tag's Location (2022.01.02)](#list)
- A topic suggested from my friend [*Alibaba*](https://github.com/abiriadev)
- Compare the results from where the `script` tag is located
- Arrange `script` tag into the `head` with external `.js` file link and don't forget the option **`defer`**

### Case 1. Script tag in the Head

![Script tag in the Head](Image/ScriptInHTML_Head.PNG)

#### ScriptInHTML_Head.html
```html
<!DOCTYPE html>

<html>

    <head>

        <meta charset="EUC-KR">
        <title>Script in the Head</title>
        <link rel="stylesheet" href="ScriptInHTML.css">
        <script>document.getElementsByTagName('p')[0].style.color = "red"</script>

    </head>

    <body>

        <p>Be the reads!</p>

    </body>

</html>
```
#### ScriptInHTML_Head.css
```css
p {
	text-align: center;
	font-family: Brush Script MT, Georgia, Garamond, Times New Roman, serif;
	/* font reference ☞ https://www.w3schools.com/css/css_font.asp */
    color: blue;
	font-size: 700%;
	margin: 0;
}
```

### Case 2. Script tag in the Bottom of the Body

![Script tag in the Bottom of the Body](Image/ScriptInHTML_BodyEnd.PNG)

#### ScriptInHTML_BodyEnd.html
```html
<!DOCTYPE html>

<html>

    <head>

        <meta charset="EUC-KR">
        <title>Script in the Bottom of the Body</title>
        <link rel="stylesheet" href="ScriptInHTML.css">

    </head>

    <body>

        <p>Be the reads!</p>
        <script>document.getElementsByTagName('p')[0].style.color = "red"</script>

    </body>

</html>
```

### Case 3. Script tag with `defer` option

![Script tag in the External .js file](Image/ScriptInExternalJS.PNG)

#### ScriptWithDefer.html
```html
<!DOCTYPE html>

<html>

    <head>

        <meta charset="EUC-KR">
        <title>Script in the External .js File</title>
        <link rel="stylesheet" href="ScriptInHTML.css">
        <script defer src="ScriptInExternalJS.js"></script>
        <!-- don't forget "defer" ! -->

    </head>

    <body>

        <p>Be the reads!</p>

    </body>

</html>
```
#### ScriptWithDefer.js
```js
document.getElementsByTagName('p')[0].style.color = "red"
```


## [6th Wedding Anniversary (2021.03.07)](#list)
- Annual Update : change images of the heart and number
- Seperate css id `name` to `name1` and `name2` and maintain the texts in a line
- Enhancement of Javascript : use `for` statement

![Wedding Anniversary 6](./Image/WeddingAnniversary6.gif)

#### Mainly changed part of WeddingAnniversary6.html
```html
	<div id='name1' style="display:inline">
		K R
		<div id='heart' style="display:inline">
			<img src="heart2.gif">
		</div>
	</div>
	<div id='name2' style="display:inline">
		E Y
	</div>
```

#### Mainly changed part of WeddingAnniversary6.css
```css
body {
	text-align: center;
}
```

#### WeddingAnniversary6.js
```js
function changeColor() {

	const randNumDec = []; 	// for containing random numbers decimally
	const randNumHex = []; 	// for containing converted numbers hexdecimally
	const cssIdList = ["name1", "name2", "chameleon1", "chameleon2"]; // css id list to change colors

	for (let i = 0; i < 4 ; i++) {
		randNumDec[i] = Math.floor(Math.random() * Math.pow(256, 3)); // generate RGB color (decimal)
		randNumHex[i] = randNumDec[i].toString(16); // turn to the hexdecimal
		document.getElementById(cssIdList[i]).style.color = '#' + randNumHex[i]; // style-color requires #XXXXXX
	}

}

setInterval(changeColor, 500);
```


## [5th Wedding Anniversary 2 (2020.03.11)](#list)
- Enhancement of `vertical-align` between text and image
- No change in `.js` file

![Wedding Anniversary 5 - 2](./Image/WeddingAnniversary5_2.gif)

#### Mainly changed part of WeddingAnniversary5_2.html
```html
	<div id='name'>
		K R
		<div id='heart'>
			<img src="heart.gif">
		</div>
		E Y
	</div>
	<div id='chameleon1'>
		Celebrate Our
		<div id='year'>
			<img src="5.gif">
		</div>
		th
	</div>
```

#### Mainly changed part of WeddingAnniversary5_2.css
```css
#heart {
	display: inline;
}
#heart img {
	width: 80px;
	height: auto;
}

#year {
	display: inline;
}
#year img {
	vertical-align: -20px;
	width: 100px;
	height: auto;
}
```


## [5th Wedding Anniversary (2020.03.07)](#list)
- Application of Colorful Show

![Wedding Anniversary](./Image/WeddingAnniversary5.gif)

#### WeddingAnniversary5.html
```html
<!DOCTYPE html>

<html>

<head>
    <meta charset="EUC-KR">
    <title>Wedding Anniversary 5</title>
    <link rel="stylesheet" href="WeddingAnniversary5.css">
</head>

<body>
    <div id='name'>
        K R <img src="https://thumbs.gfycat.com/ZigzagJauntyHapuku-small.gif"  height="70" width="70"> E Y
    </div>
    <div id='chameleon1'>
        Celebrate Our <img src="https://media.giphy.com/media/jQWTJf2Ch2ANz2DdqU/giphy.gif"  height="80" width="80">th
    </div>
    <div id='chameleon2'>
        Wedding Anniversary
    </div>
    <script src="WeddingAnniversary5.js">
    </script> 
</body>

</html>
```

#### WeddingAnniversary5.css
```css
@charset "EUC-KR";

#name {
    text-align: center;
    font-family: "Times New Roman", Times, serif;
    font-size: 450%;
}

#chameleon1 {
    text-align: center;
    font-family: "Times New Roman", Times, serif;
    font-size: 400%;
}

#chameleon2 {
    text-align: center;
    font-family: "Times New Roman", Times, serif;
    font-size: 400%;
}
```

#### WeddingAnniversary5.js
```js
function changeColor() {
	randNumDec1 = Math.floor(Math.random() * Math.pow(256, 3));
	randNumDec2 = Math.floor(Math.random() * Math.pow(256, 3));
	randNumDec3 = Math.floor(Math.random() * Math.pow(256, 3));
	
	randNumHex1 = randNumDec1.toString(16);
	randNumHex2 = randNumDec2.toString(16);
	randNumHex3 = randNumDec3.toString(16);

	document.getElementById('name').style.color = '#' + randNumHex1;
	document.getElementById('chameleon1').style.color = '#' + randNumHex2;
	document.getElementById('chameleon2').style.color = '#' + randNumHex3;
}

setInterval(changeColor, 500);
```


## [Colorful Show (2020.03.04)](#list)
This is a colorful 'Show'.

![Colorful Show](./Image/ColorfulShow.gif)

#### ColorfulShow.html
```html
<!DOCTYPE html>

<html>

<head>
	<meta charset="EUC-KR">
	<title>Colorful Show</title>
  	<link rel="stylesheet" href="ColorfulShow.css">
</head>

<body>
	<p id='chameleon'>Show</p>
  	<script src="ColorfulShow.js">
		<!--
			<script> can be located in <head> or <body>. 
			But, in this case, we should consider execution sequence.
		-->
		
	</script> 
</body>

</html>
```

#### ColorfulShow.css
```css
@charset "EUC-KR";

#chameleon {
	text-align: center;
	font-family: "Times New Roman", Times, serif;
	font-size: 1000%;
}
```

#### ColorfulShow.js
```javascript
function changeColor() {
	randNumDec = Math.floor(Math.random() * Math.pow(256, 3));
		/*
		 * Math.random() returns a number lower than 1.
	 	 * Math.floor() returns the largest integer less than or equal to a given number.
		 * 256**3 is for the RGB color range between #000000 ~ #FFFFFF.
		 */
	randNumHex = randNumDec.toString(16); /* Convert Decimal to Hexadecimal */

	/* document.write(randNumHex, "<br>"); */
		/* document.write() returns real HTML codes. */
		/* document.write(typeof randColor);
		 * string
		 */

	document.getElementById('chameleon').style.color = '#' + randNumHex;
}

setInterval(changeColor, 1000);
```


## [Ganzi (2017.04.03)](#list)
- A simple Javascript practice

![Ganzi](Image/Ganzi.gif)

```html
<div id ="Zure">Ganzi</div>

<script type="text/javascript">
  
function thunder() {
	var x = document.getElementById("Zure");
	var storm = document.write(x.innerHTML + " Storm");
	Zure.replace(x,storm);
}
setInterval(thunder, 3000);
	
</script>
```
