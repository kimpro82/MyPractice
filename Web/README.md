# [My Web Practice]

HTML, CSS and JavaScript


### List

- [Bootstrap : Magic Stick (2022.01.28)](#bootstrap--magic-stick-20220128)
- [Script Tag's Location (2022.01.02)](#script-tags-location-20220102)
- [Colorful Show (2020.03.04)](#colorful-show-20200304)
- [Ganzi (2017.04.03)](#ganzi-20170403)


## [Bootstrap : Magic Stick (2022.01.28)](#list)
- A practice of **Bootstrap** (5.1.3) : use `container-fluid` `mx` `my` `row` `col`
- Originally I was going to apply **grid**, but to fail.

![Bootstrap : Magic Stick](Images/BootstrapMagicStick.gif)

#### BootstrapMagicStick.html
```html
……
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
……
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

![Script tag in the Head](Images/ScriptInHTML_Head.PNG)

#### ScriptInHTML_Head.html
```html
……
    <head>

        <meta charset="EUC-KR">
        <title>Script in the Head</title>
        <link rel="stylesheet" href="ScriptInHTML.css">
        <script>document.getElementsByTagName('p')[0].style.color = "red"</script>

    </head>
……
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

![Script tag in the Bottom of the Body](Images/ScriptInHTML_BodyEnd.PNG)

#### ScriptInHTML_BodyEnd.html
```html
……
    <body>

        <p>Be the reads!</p>
        <script>document.getElementsByTagName('p')[0].style.color = "red"</script>

    </body>
……
```

### Case 3. Script tag with `defer` option

![Script tag in the External .js file](Images/ScriptInExternalJS.PNG)

#### ScriptWithDefer.html
```html
……
    <head>

        ……
        <script defer src="ScriptInExternalJS.js"></script>
        <!-- don't forget "defer" ! -->

    </head>
……
```
#### ScriptWithDefer.js
```js
document.getElementsByTagName('p')[0].style.color = "red"
```


## [Colorful Show (2020.03.04)](#list)
This is a colorful 'Show'.

![Colorful Show](Images/ColorfulShow.gif)

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

![Ganzi](Images/Ganzi.gif)

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
