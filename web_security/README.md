## Experiment on finding vulnurabilities of known websites using ZAP(Zed Attack Proxy)

#### ZAP by OWASP is an easy to use vulnerability finding tool

### installation:

- Java [download](https://javadl.oracle.com/webapps/download/AutoDL?BundleId=238729_478a62b7d4e34b78b671c754eaaf38ab)
- ZAP [download](https://github.com/zaproxy/zaproxy/releases/download/v2.8.0/ZAP_2_8_0_windows.exe)

### Objective:

- Monitoring network calls for a known website
- finding vulnerabilities of the website
- reading about why these happen and ways to mitigate them

---
## Experiment on exploiting XSS vulnerability and mitigation for the same

### Setup:

1. A demo website source code is given at [lab/xss-demo](lab/xss-demo)
2. Run following commands to start backend server for the website
    `$ pip install -r requirements.txt`
    `$ ./xss.py`
3. Open https://localhost:5000/, response should come with a form asking for name and comment
4. All the names and comments are stored at server's database unescaped and user can view all the names and comments till now

### Task1: Inject a code snippet to the server's database which results in an alert popping up every time an user visits the website

### Task2: Update source code to mitigate the vulnerability

Hint: parse the inputs you get from the forms

---
## Demo on exploiting CSRF vulnerability

---
## Experiment on exploiting vulnerabilities on juice-shop

#### Juice-shop by OWASP is a project website with lots of vulnerabilities(from OWASP Top-10) to exploited and learning security concepts while doing

### installation and setup:

1) install node.js - [download](https://nodejs.org/dist/v10.16.0/node-v10.16.0-x64.msi)
2) git clone https://github.com/bkimminich/juice-shop.git
3) cd juice-shop
4) npm install
5) npm start
6) browse to http://localhost:3000

### Task: clear the following [challenges](https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/):

- [finding the scoreboard](https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/score-board.html)
- 1/2/3 star challenges of [injection](https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/injection.html)
- 1/2/3 star challenges of [XSS](https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/xss.html)

*[task solutions](https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/appendix/solutions.html)*

### Objective:

- Learning how to closely and smartly look at code
- Learning how to use browser tools like inspect element, network monitor, console, debugger, etc.
- Exploiting injection vulnerabilities 
- Exploiting XSS vulnerabilities

---
