#QA Assignment _Python _Hanish Shetty

###Instructions for installing the project

1. Install Python 3.9.

2. Make sure that the path to pip is added in the environment variable of the system

3. Clone/Download the project

4. You can change the Username and Email you wish from the *Constants/user_info.py* file

5. Navigate to the Project folder through terminal/command line

6. Run the following commands to download the dependencies used in the project

        pip install pytest pytest-html pytest-bdd selenium
   
7. After installing the above dependencies, run the below command:
    
        pytest --html report.html
   
8. If you wish to run a single scenario, you can do it by putting a tag on the scenario: **@signup**
    
        pytest --html report.html -k "signup"
   
9. After running the test, you can find the report in the **report.html** file

10. For Functional testing and Usability Testing scenarios refer, ***Manual-Submissions*** folder