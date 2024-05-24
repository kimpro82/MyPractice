#!/bin/bash

#######################################
# helloWorld "echo"
# 2024.05.23
#
# Example:
#     Function call: hello_world "echo"
#######################################

helloWorld() {
    # Retrieves the current function name and calls the given function dynamically.
    #
    # Arguments:
    #     funcName (str): The name of the function to call.
    # Returns:
    #     None
    local funcName=$1
    local currentFuncName="${FUNCNAME[0]}"

    # Invokes the function with the given name and passes the current function name as an argument.
    "$funcName" "$currentFuncName"
}

# Call the helloWorld function.
helloWorld "echo"
