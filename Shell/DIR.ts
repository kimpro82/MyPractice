// JScript practice running via cscript on Windows 1 : DIR
// 2024.09.26


// Define interfaces for better type checking
interface WScriptShell {
    Exec(command: string): WScriptExec;
}

interface WScriptExec {
    StdOut: {
        ReadAll(): string;
    };
}

// Use type assertion to tell TypeScript the type of WScript
const shell: WScriptShell = (WScript as any).CreateObject("WScript.Shell");

// Execute 'dir' command to list files in the current directory
const exec: WScriptExec = shell.Exec("cmd /c dir");

// Read the output from the command
const output: string = exec.StdOut.ReadAll();

// Print the output
(WScript as any).Echo(output);
