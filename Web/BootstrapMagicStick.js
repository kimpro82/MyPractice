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