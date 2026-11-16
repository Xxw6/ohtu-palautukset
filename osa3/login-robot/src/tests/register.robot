*** Settings ***
Resource    resource.robot
Test Setup    Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials    maija    salasana1
    Output Should Contain    New user registered
    Input Login Command
    Input Credentials    maija    salasana1
    Output Should Contain    Logged in

Register With Already Taken Username And Valid Password
    Input Credentials    kalle    toinen123
    Output Should Contain    Username is already taken

Register With Too Short Username And Valid Password
    Input Credentials    ab    salasana1
    Output Should Contain    Username must contain at least 3 letters a-z

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials    ka11e    salasana1
    Output Should Contain    Username must contain at least 3 letters a-z

Register With Valid Username And Too Short Password
    Input Credentials    maija    sala1
    Output Should Contain    Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials    maija    salasana
    Output Should Contain    Password must not contain only letters

*** Keywords ***
Input New Command And Create User
    Create User    kalle    kalle123
    Input New Command