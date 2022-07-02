*** Test Cases ***

TC001:For Loop

#    : FOR   ${i}    IN RANGE   ${list}
#      \   log to console   ${i}
#
#
#    : FOR   ${i}    IN   1 2 3 4 5
#      \   log to console   ${i}
#
#
#
#    ${list}   create list  1 2 3 4 5
#    : FOR   ${i}    IN    ${list}
#      \   log to console   ${i}

#    ${list}   create list  1 2 3 4 5 7 8 9
#    : FOR   ${i}    IN    ${list}
#      \   log to console   ${i}
#      \   exit for loop if   ${i}==4

