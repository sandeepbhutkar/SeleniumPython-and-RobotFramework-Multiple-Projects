*** Settings ***


*** Variables ***
#list variable - hold multiple value
 @{myvariable} =  one  two  three  four

*** Keywords ***


*** Test Cases ***
TC001 List Variables_Global
    [Tags]   list
    log to console   @{myvariable}[0]
    log to console   @{myvariable}[1]
    log to console   @{myvariable}[2]

TC002 List Variables_Local
#variables will work within this TC only
    [Tags]  list_local
    ${local_variable} =  create list  one  2  sandeep  somethingelse
    log to console  ${local_variable}[0]
    log to console  ${local_variable}[1]
    log to console  ${local_variable}[2]
    log to console  ${local_variable}[3]

TC001 explore loops
	[Tags]  loops
	FOR   ${i}  IN  @{MyVariable}
	log to console  ${i}
	END