// JScript practice running via cscript on Windows 2 : Read CSV
// 2024.09.27


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

// Exit early if the file doesn't exist
if (!fso.FileExists(csvFilePath)) {
    WScript.Echo("File not found: " + csvFilePath);
    WScript.Quit(1);
}

// Function to read CSV content from file
function readCsvFile(filePath: string): string {
    var file = fso.OpenTextFile(filePath, 1); // 1 = ForReading
    var content = file.ReadAll();
    file.Close();
    return content;
}

// Function to manually trim whitespace from both ends of a string
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

// Function to pad a string to a specified width by appending spaces
function padString(str: string, width: number): string {
    str = manualTrim(str); // Trim the string first
    var paddedString: string = str;
    while (paddedString.length < width) {
        paddedString += " "; // Append spaces until reaching the desired width
    }
    return paddedString;
}

// Function to print the separator line
function printSeparatorLine(columns: number) {
    var separatorLine: string = "";
    for (var i = 0; i < columns * COLUMN_WIDTH; i++) {
        separatorLine += "-";
    }
    WScript.Echo(separatorLine);
}

// Function to print headers
function printHeaders(headers: string[]) {
    var headerOutput: string = "";
    for (var h = 0; h < headers.length; h++) {
        headerOutput += padString(headers[h], COLUMN_WIDTH);
    }
    WScript.Echo(headerOutput);
}

// Function to process CSV content
function processCsvContent(csvContent: string) {
    var lines: string[] = csvContent.split("\r\n");
    var headers: string[] = lines[0].split(",");

    printSeparatorLine(headers.length);
    printHeaders(headers);
    printSeparatorLine(headers.length);

    for (var i = 1; i < lines.length; i++) {
        var line: string = lines[i];
        var trimmedLine: string = manualTrim(line);
        if (trimmedLine !== "") {
            var row: string[] = trimmedLine.split(",");
            var record: string = "";
            for (var j = 0; j < headers.length; j++) {
                record += padString(row[j] ? manualTrim(row[j]) : "N/A", COLUMN_WIDTH);
            }
            WScript.Echo(record);
        }
    }

    printSeparatorLine(headers.length);
}

// Main execution flow
var csvContent: string = readCsvFile(csvFilePath);
processCsvContent(csvContent);
