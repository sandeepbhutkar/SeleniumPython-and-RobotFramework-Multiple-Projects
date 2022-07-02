*** Settings ***
 Library    XML

*** Variables ***

*** Keywords ***

*** Test Cases ***


TC001: Get the count of root element

    ${xml_obj} =  parse xml     Data/menu.xml
    ${count} =  get element count  ${xml_obj}  ./
    log to console  count of root element is : ${count}

TC002:What is name of root element
    ${xml_obj} =  parse xml     Data/menu.xml
    should be equal  ${xml_obj.tag}  breakfast_menu
    log to console   ${xml_obj.tag}


TC003:How many ‘food’ elements are present?
    ${xml_obj} =  parse xml     D:/Python/menu.xml
    ${count} =  get element count  ${xml_obj}  .//food
    log to console  number of ‘food’ elements present are : ${count}

TC004:Check first food item ‘Name’
    ${xml_obj} =  parse xml     D:/Python/menu.xml
    ${name}=  get element text    ${xml_obj}  .//food[1]/name
    should be equal     ${name}    Belgian Waffles

TC005:Check first food item ‘Price’
    ${xml_obj} =  parse xml     D:/Python/menu.xml
    ${price}=  get element text    ${xml_obj}  .//food[1]/price
    should be equal     ${price}    $5.95

TC006:Check first food item ‘Calories’
    ${xml_obj} =  parse xml     D:/Python/menu.xml
    ${cal}=  get element text    ${xml_obj}  .//food[1]/calories
    should be equal     ${cal}    650

TC007:Add values in xml

    ${xml_obj}=  parse xml     Data/menu.xml
    add element   ${xml_obj}   <food></food>
    add element   ${xml_obj}   <name>French Fry</name>     xpath=food[7]
    add element   ${xml_obj}   <price>5.45</price>     xpath=food[7]
    add element   ${xml_obj}   <description>French Fryadd something</description>     xpath=food[7]
    add element   ${xml_obj}   <calories>150</calories>     xpath=food[7]
    save xml   ${xml_obj}     Data/menu.xml

TC008: Varify if value got added
    element should exist      Data/menu.xml   food[7]



