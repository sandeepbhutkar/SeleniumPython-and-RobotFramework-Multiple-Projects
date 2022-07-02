*** Settings ***
 Library    XML

*** Test Cases ***
TC001:
    ${XML} =   parse xml  D:/Python/example.xml
    #{root} =   parse xml   ${XML}
    Should Be Equal	${xml.tag}	example

    {first} =  Get Element	${root}	first
#    Should Be Equal	${first.text}	text
#    Dictionary Should Contain Key	${first.attrib}	id
#    Element Text Should Be	${first}	text
#    Element Attribute Should Be	${first}	id	1
#    Element Attribute Should Be	${root}	id	1	xpath=first
#    Element Attribute Should Be	${XML}	id	1	xpath=first