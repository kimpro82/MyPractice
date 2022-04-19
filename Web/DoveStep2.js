// Declare global variables
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
var x = -1, y = -1, direction = 0, speed = 1, step = 0;
var x0, y0;
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
            x0 = x;
            y0 = y;
            x = Math.round(Math.random() * 560) + 20;
            y = Math.round(Math.random() * 560) + 20;

            // Generate smooth walking trace
            var valid = false;
            var direction0 = direction;
            x0 = x, y0 = y;
            while (valid == false)
            {
                var direction1 = (direction0 + Math.floor(Math.random() * 60) + (360 - 30)) % 360;
                if (direction1 != direction0)
                {
                    speed = Math.min(Math.round(Math.abs(60 / (direction1 - direction0))), 30);
                    // speed = Math.ceil(Math.sqrt((direction1 - direction0 + 360) % 360));
                }
                else { speed = 30; }
                var x1 = x0 + Math.round(Math.cos(direction * Math.PI / 180) * speed);
                var y1 = y0 + Math.round(Math.sin(direction * Math.PI / 180) * speed);
            
                if ((x1 > 20 && x1 < 580) && (y1 > 20 && y1 < 580))
                {
                    direction = direction1;
                    x = x1;
                    y = y1;
                    valid = true;
                }
            }

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
    console.log(step + "th step :", x, y, speed, direction);
}

// Loop by setInterval()
setInterval(randomWalk, interval);
// setInterval(randomWalk, interval / speed);