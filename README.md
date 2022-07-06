# eno-delete
 Automatically deletes Capital One Eno virtual cards for when you've made a couple too many. 
 Now supports keywords so you can delete only one site's cards.

 Warning: Program will delete ALL virtual cards if "keyword" is left blank.

 Note: Your Capital One session will expire after some time, so you may have to restart and log in again.


 How to use:
 1. Install python3 and chromedriver.exe for your current browser version (chrome://settings/help)

 a. https://www.python.org/downloads/ (Make sure to check "Add to PATH")

 b. https://chromedriver.chromium.org/downloads (Put in your PATH at "C:/Users/youruser")

 2. Install selenium with "pip install selenium" in command line
 3. Change "s" variable to the path of your chromedriver.exe
 4. Change "keyword" variable to site you want to delete. Leave blank to delete all cards.
 5. Run, login, and hit enter in the command line once done
 6. Go do something else