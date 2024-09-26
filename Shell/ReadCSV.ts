// JScript practice running via cscript on Windows 2 : Read CSV
// 2024.09.26

const COLUMN_WIDTH: number = 24; // Fixed column width for each cell in the output

// Create FileSystemObject
var fso: any = WScript.CreateObject("Scripting.FileSystemObject");

// Get the command-line arguments
var args: any = WScript.Arguments;

// Check if the CSV file path is provided as an argument
if (args.length < 1) {
    WScript.Echo("Usage: cscript JScript_RunViaCscript.js <csvFileName>");
    WScript.Quit(1);
}

// Get the CSV file name from the argument
var csvFileName: string = args.Item(0);

// Get the current folder where the script is running
var scriptFullPath: string = WScript.ScriptFullName;
var currentFolder: string = fso.GetParentFolderName(scriptFullPath);

// Construct the full path to the CSV file
var csvFilePath: string = fso.BuildPath(currentFolder, csvFileName);

// Check if the file exists
if (fso.FileExists(csvFilePath)) {
    // Open the file for reading
    var csvFile: any = fso.OpenTextFile(csvFilePath, 1); // 1 = ForReading

    // Read the contents of the file
    var csvContent: string = csvFile.ReadAll();

    // Close the file after reading
    csvFile.Close();

    // Split the content into lines
    var lines: string[] = csvContent.split("\r\n");

    // Parse the header
    var headers: string[] = lines[0].split(",");

    /**
     * Manually trims whitespace from both ends of a string.
     * 
     * @param {string} str - The input string to be trimmed.
     * @returns {string} The trimmed string.
     */
    function manualTrim(str: string): string {
        var start: number = 0;
        var end: number = str.length - 1;

        while (start <= end && (str.charAt(start) === ' ' || str.charAt(start) === '\t')) {
            start++;
        }
        while (end >= start && (str.charAt(end) === ' ' || str.charAt(end) === '\t')) {
            end--;
        }

        return str.substring(start, end + 1);
    }

    /**
     * Pads a string to a specified width by appending spaces.
     * 
     * @param {string} str - The string to be padded.
     * @param {number} width - The desired width of the output string.
     * @returns {string} The padded string.
     */
    function padString(str: string, width: number): string {
        str = manualTrim(str); // Trim the string first
        var paddedString: string = str; // Start with the original string
        while (paddedString.length < width) {
            paddedString += " "; // Append spaces until reaching the desired width
        }
        return paddedString; // Return the padded string
    }

    // Output the header separator line
    var separatorLine: string = "";
    for (var i: number = 0; i < headers.length * COLUMN_WIDTH; i++) {
        separatorLine += "-"; // Create line of dashes
    }
    WScript.Echo(separatorLine); // Print the separator line

    // Output headers with fixed width
    var headerOutput: string = "";
    for (var h: number = 0; h < headers.length; h++) {
        headerOutput += padString(headers[h], COLUMN_WIDTH); // Pad each header
    }
    WScript.Echo(headerOutput); // Print headers

    // Output the separator line again after headers
    WScript.Echo(separatorLine); // Print the separator line again

    // Parse each row and output the key-value pairs
    for (var i: number = 1; i < lines.length; i++) {
        var line: string = lines[i];
        var trimmedLine: string = manualTrim(line); // Manually trim the line
        if (trimmedLine !== "") { // Check if the line is not empty
            var row: string[] = trimmedLine.split(","); // Split only non-empty lines
            var record: string = ""; // Use a string to hold key-value pairs
            for (var j: number = 0; j < headers.length; j++) {
                // Create a key-value pair as a string and pad it to fixed width
                record += padString(row[j] ? manualTrim(row[j]) : "N/A", COLUMN_WIDTH); // Pad or use "N/A"
            }
            // Output the record
            WScript.Echo(record); // Output as a single line
        }
    }

    // Output the final separator line at the end of the data
    WScript.Echo(separatorLine); // Print the final separator line
} else {
    WScript.Echo("File not found: " + csvFilePath); // Inform user if the file does not exist
}
