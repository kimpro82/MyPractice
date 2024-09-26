// JScript practice running via cscript on Windows 1 : DIR
// 2024.09.26
// Use type assertion to tell TypeScript the type of WScript
var shell = WScript.CreateObject("WScript.Shell");
// Execute 'dir' command to list files in the current directory
var exec = shell.Exec("cmd /c dir");
// Read the output from the command
var output = exec.StdOut.ReadAll();
// Print the output
WScript.Echo(output);
