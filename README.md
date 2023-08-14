# LinkedIn Job Scraper with Automated Email Functionality
<img align="right" width="100" height="100" src="https://user-images.githubusercontent.com/111251492/225376166-b814df59-814b-448e-b85d-90f3a7ee4ac6.png">
By Anand Kumar

## Features
* **Fast Scrapping** : Quickly extracts job data from LinkedIn
* **Advanced Job description filtering** : Scans each job description, filters out jobs which doesn't matches your year of experience.
* **Adjustability to slow network** : Auto optimization to slow internet connection with a single user input.
* **Reduced bot action detection** :  Mitigates the risk of being detected as a bot during data scraping.
* **Automated emailing functionality of scrapped data** : Sends scrapped data to designated email addresses automatically.

# Instructions
After you have downloaded the project files. Follow the insctructions below to setup your machine to make code functional.
## Downloading/Installing dependencies 
Of course you need [Python](https://www.python.org) and an IDE like [VSCode](https://code.visualstudio.com), [PyCharm](https://www.jetbrains.com/pycharm) etc. installed on your machine. Along with it you need to install/download some other packages on your machine which are mentioned below.

> Install Selenium Python

Install Selenium python on your machine using command line/terminal. For any installation help please read [Selenium Python Documentation](https://pypi.org/project/selenium/)


> Download Selenium Webdriver

The code is written for automation of Chrome browser, however the code can be used to automate Edge Browser, Firefox and Safari as well by modifying the code line 38 of main.py file `driver = webdriver.Chrome(options=browser_options)` according to the browser of choice.

If you do not want to change any code then first [Download Chrome](https://www.google.com/chrome) on you system then follow instruction below.
Go to settings in chrome > then go to about chrome
Now note the build version of your chrome

<p align="center">
  <img src="https://user-images.githubusercontent.com/111251492/225451710-6cde0e57-71a0-42aa-a0a0-8d5f663a6ecd.png">
</p>

For example say build version is 111.0.5563.65. Then visit [selenium webdriver page for chrome](https://chromedriver.chromium.org/downloads) From their download the latest version of zip file of webdriver for your operating system whose start version is same as your Chrome build version (in this case 111). Then unzip the folder open it then copy the path location of the folder on your local machine. For Example "C:\Users\Anand\Downloads\webdriver". Paste this location within quotes of line 37 of main.py file `os.environ['PATH'] += r'C:\Users\Anand\Downloads\webdriver'`


> Install Pandas

Install the Pandas library on your machine using command line/terminal. For any installation help please read [Pandas Documentation](https://pypi.org/project/pandas)

## Email Account Setup

Note that you need to have two mail ids for this functionality so in case you don't have two mail accounts then create it.Open the mail_system.py file in your IDE and in line 7 enter the email id which you want to use as sender within quotes.

For eg. `user_mail = 'yourmailid@goeshere.com'` and in line 9 provide the mail id within quotes on which you want to receive the Scrapped Data. For eg. `recipient = 'receivingmailid@goeshere.com'`

> Setting passcode of sender's mail

The mail functionality is supported by the SMTP (Simple Mail Transfer Protocol) library which is in-built in Python latest versions. You cannot use your mail id password for this process as the popular mail services like Google Mail, Yahoo Mail blocks this action due to security reasons. So you need to create app password to use this. Please visit on the links below to know how to setup app passwords.
+ [For Gmail](https://support.google.com/accounts/answer/185833?hl=en)
+ [For Yahoo Mail](https://help.yahoo.com/kb/generate-manage-third-party-passwords-sln15241.html)
+ [For Outlook](https://support.microsoft.com/en-us/account-billing/using-app-passwords-with-apps-that-don-t-support-two-step-verification-5896ed9b-4263-e681-128a-a6f2979a7944)

After you have created the app password. Enter the password in line 8 of mail_system.py file within quotes.

For eg. `passcode = 'yourapppasscode'`


###### Your machine is ready now!!!

Simply open the whole Job scraper folder in your IDE and run the main.py file to start LinkedIn Job Scraper. After entering the required input in the console, the browser will automatically begin scraping job listings based on the specified criteria. The browser closes automatically after the code completes running successfully.

> `How to comment or uncomment any line?` : Simply click on the line that you want to comment or uncomment and with Ctrl/⌘ pressed on keyboard click forward slash key '/' on the keyboard.
 
## Do's and Don'ts
> Do's

+ You can use your machine during the process.
+ You can keep the browser and IDE in background.

> Don'ts

+ Do not click on any element of the webpage as it can lead to termination of the code.
+ Do not use console during the process.
+ Do not turn off internet or close the automated browser session.
+ To prevent any unexpected action against your LinkedIn account, please do not have your browser logged in to LinkedIn which you are going to automate. Care to logout before running the scraper.
