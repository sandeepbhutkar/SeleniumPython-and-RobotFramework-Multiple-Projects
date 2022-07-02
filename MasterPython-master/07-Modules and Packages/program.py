# lets call function written in module, importing from module
from CreateYourOwnModulesAndPackages import my_func
my_func() # output on console should be : I am in module

# importing from packages

from myMainPackage import someMainScript
from myMainPackage.subPackage import mySubScript

someMainScript.report_main()

mySubScript.sub_report()