# [My Web Practice]
HTML, CSS and JavaScript

- 6th Wedding Anniversary (2021.03.07)
- 5th Wedding Anniversary 2 (2020.03.11)
- 5th Wedding Anniversary (2020.03.07)
- Colorful Show (2020.03.04)
- Ganzi.html (2017.04.03)


## 6th Wedding Anniversary (2021.03.11)
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


## 5th Wedding Anniversary 2 (2020.03.11)
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


## 5th Wedding Anniversary (2020.03.07)
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


## Colorful Show (2020.03.04)
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


## Ganzi.html (2017.04.03)
- A simple Javascript practice

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
