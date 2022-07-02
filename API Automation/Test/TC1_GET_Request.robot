*** Settings ***
Library  RequestsLibrary

*** Test Cases ***
TC001:GET REQUEST
    create session  myssion     https://reqres.in
    #http://restapi.demoqa.com/utilities/weather/city/Delhi
    ${response} =  get request  myssion    /api/users/2
    log to console   ${response.status_code}
    log to console   ${response.content}
#    log to console   ${response.headers}
    ${Status} =  convert to string  ${response.status_code}
    should be equal      ${Status}   200
    ${Body} =  convert to string  ${response.content}
    should contain  ${Body}   janet.weaver@reqres.in
