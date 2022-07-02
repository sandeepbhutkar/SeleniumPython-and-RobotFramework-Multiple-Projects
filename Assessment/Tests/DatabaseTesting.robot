*** Settings ***
Library    DatabaseLibrary

Suite Setup     connect to database     ${dbapiModuleName}  ${dbName}   ${dbUserName}   ${dbPassword}   ${dbHost}   ${dbPort}
Suite Teardown      disconnect from database

*** Variables ***
${dbapiModuleName} =  pymysql
${dbHost} =  127.0.0.1
${dbPort} =  3306
${dbName} =  database1
${dbUserName} =  root
${dbPassword} =  root
*** Keywords ***

*** Test Cases ***
TC001 - Create table
    ${output} =  execute sql string   create table emp1(emp_id integer, first_name varchar(30), last_name varchar(30))
    log to console  ${output} # displays inserted value in console
    should be equal as strings   ${output}   None   # to verify values are inserted correctly.

TC002 - Verify table must exist
    table must exist  emp1

TC003 - Insert

        ${output} =  execute sql string  insert into database1.emp1(emp_id,first_name,last_name) values(5,'Sandeep5','');
        log to console  ${output}
        should be equal as strings   ${output}   None

TC004- insert multiple data from file

        execute sql script  Data/Insert.sql
        log to console  ${output}
        should be equal as strings   ${output}   None

TC005- Update

        ${output} =  execute sql string   update database1.emp1 set last_name="Bhutkar4" where emp_id = 4;
        log to console  ${output}
        should be equal as strings   ${output}   None

TC006 - check if firstname exist in db

       Check If Exists In Database    select * from database1.emp1 where first_name='Sandeep';

TC007 - check for NULL values

    check if not exists in database    select * from database1.emp1 where first_name=NULL;

TC007 - check for Blank values

    check if not exists in database    select * from database1.emp1 where last_name='';

TC008 - row count

    row count is equal to x   select * from database1.emp1;   5

TC009 - retrive table

    ${result} =  query   select * from database1.emp1;
    log many   ${result}

TC010 - DESC

    @{queryResults}	Description	SELECT * FROM database1.emp1;
    Log Many	@{queryResults}

TC011 - verify Row count of two tables
    [Tags]  run
    ${count_emp1} =  row count    select * from database1.emp1;
    log to console  ${count_emp1}
    ${count_emp22} =  row count    select * from database1.emp22;
    log to console  ${count_emp22}
    evaluate  ${count_emp1} == ${count_emp22}