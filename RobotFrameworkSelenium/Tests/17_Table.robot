*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
TC001: Verify Table
    open browser    http://coredogs.com/lesson/web-page-tables.html  chrome
    maximize browser window
    #to get row count
    #xpath://*[@id="node-356"]/div[2]/table/    this is x path
    #tbody and tr (table row)  should be typed manual in cropath selectors and hit enter
    ${RowCount} =  get element count   xpath://*[@id="node-356"]/div[2]/table/tbody/tr
    log to console   ${RowCount}
    # to get colum count
    ${ColumnCount} =  get element count   //*[@id="node-356"]/div[2]/table/tbody/tr[2]/td
    log to console   ${ColumnCount}
    #to get text in column
    ${GetText} =  get text   xpath://*[@id="node-356"]/div[2]/table/tbody/tr[2]/td[1]    # text of 2nd row and 1st column
    log to console   ${GetText}

TC002:verify contents in table
    [tags]  content
    open browser    http://coredogs.com/lesson/web-page-tables.html  chrome
    table row should contain    //*[@id="node-356"]/div[2]/table    2      Kieran   #2nd row should contain Kieran
    table column should contain     //*[@id="node-356"]/div[2]/table   2   Medium    #2nd column
    table cell should contain   //*[@id="node-356"]/div[2]/table   3  3   Sheltie   #3rd row 3rd column
    table header should contain     //*[@id="node-356"]/div[2]/table      	Breed   #header
    close browser
