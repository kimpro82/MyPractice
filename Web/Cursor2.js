// Declare an array of kewords for cursor property
// Reference ☞ https://developer.mozilla.org/en-US/docs/Web/CSS/cursor
var cursorTypes = [
    ["auto", "default", "none"],
    ["context-menu", "help", "pointer", "progress", "wait"],
    ["cell", "crosshair", "text", "vertical-text"],
    ["alias", "copy", "move"],
    ["no-drop", "not-allowed", "grab", "grabbing"],
    ["n-resize", "e-resize", "s-resize", "w-resize"],
    ["ne-resize", "nw-resize", "se-resize", "sw-resize"],
    ["ew-resize", "ns-resize", "nesw-resize", "nwse-resize"],
    ["zoom-in", "zoom-out"]
]

// A function to generate span elements with inner text and cursor style
function genBoxes(cursorTypes)
{
    // Declare an object to indicate the element where new elements will be appended
    var obj = document.getElementById("box")

    // Loop for the array cursorTypes
    for (r in cursorTypes)
    {
        for (el in cursorTypes[r])
        {
            // Test : ok
            // console.log(cursorTypes[r][el])

            // Generate a box with style
            var newBox = document.createElement("span")
            // newBox.className = cursorTypes[r][el]                            // not needed
            newBox.innerText = cursorTypes[r][el]
            newBox.style.cursor = cursorTypes[r][el]

            // Append it
            obj.appendChild(newBox)
        }

        // Line replacement
        var br = document.createElement("br")
        obj.appendChild(br)
    }
}

// Run
genBoxes(cursorTypes)