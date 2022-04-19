// Declare global variables
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
var x = -1, y = -1, direction = 0, step = 0;
var interval = 1000;

// Start with a click on the canvas
canvas.onclick = function(event)
{
    x = event.clientX - ctx.canvas.offsetLeft;
    y = event.clientY - ctx.canvas.offsetTop;
    // test
    console.log("click point :", x, y);

    footPrint();
}

// Determine where the next step is located
function randomWalk()
{
    if (x >= 0)
    {
        if (step > 19)
        {
            alert("The dove has archieved " + step + " steps. It became a budda and flied away!");
            return -1;
        }
        else
        {
            x = Math.round(Math.random() * 560) + 20;
            y = Math.round(Math.random() * 560) + 20;
            direction = Math.floor(Math.random() * 360);    // 0 ~ 359

            footPrint();
        }
    }
}

// Figure the foot print in detail
function footPrint()
{
    var angles = [45, 90, 135, 270];
    ctx.beginPath();
    for (let i = 0; i < 4; i++)
    {
        ctx.moveTo(x, y);
        var x2 = x - Math.round(Math.cos(Math.PI * (angles[i] + direction) / 180) * 20);
        var y2 = y - Math.round(Math.sin(Math.PI * (angles[i] + direction) / 180) * 20);
        ctx.lineTo(x2, y2);
    }
    ctx.closePath();
    ctx.stroke();

    step++;

    // test
    console.log(step + "th step :", x, y, direction);
}

// Loop by setInterval()
setInterval(randomWalk, interval);