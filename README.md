# Amazon Price Tracker using Python, Selenium and AWS EC2  
 This automated Price Tracker for amazon product is built using Python. It allows Tracking price changes and sending email alerts once the desired price is reached 
 ![priceTracker](https://user-images.githubusercontent.com/54501663/163172724-473bb607-6654-4ea2-a630-6d5be4cd3a4b.png)

## Steps 
- getting the link from Amazon website and locating elements: product name and price
- Fetching the element using selenium syntax  [See documentation](https://selenium-python.readthedocs.io/locating-elements.html)
- Checking if the price meets the budget
- Sending an e-mail alert using smtplib 

## Requirements and Setup  
### Chromedriver 

[Download and installation](https://chromedriver.chromium.org/getting-started)

### 
### Virtual Environment Setup 
```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```
### Requirements Installation 

```bash
pip install -r requirements.txt
```
### Runnig Price Tracker Script 
```bash
python3 scraper.py
```
## Scheduling our task with AWS and Cronjob: 
The goal is to trigger the script (the price tracker) daily 
### Launching an EC2 instance and connecting to it 

[Please refer to this documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)

### Accessing the EC2 instance 
Open your local terminal, go to the directory where your private key is stored and run the following command : 
```bash
ssh -i /path/my-key-pair.pem ec2-user@my-instance-public-dns-nae
```
### Installing tools on our instance
#### Python & pip 
```bash
sudo yum install python37
curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --user
```

#### Chrome Driver & chrome 
```bash
cd/tmp/
wget https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriverchromedriver --version

```
```bash 
curl https://intoli.com/install-google-chrome.sh | bash
sudo mv /usr/bin/google-chrome-stable /usr/bin/google-chrome
google-chrome --version && which google-chrome
```
#### Selenium 
```bash
pip3 install selenium
```
### Moving our script to EC2 instance 
```bash
scp -i /path/my-key-pair.pem python_file.py ec2-user@my-instance-public-dns-nae:~
```
### scheduling with Crontab 
#### Connect to EC2 and edit crontab file 
```bash
crontab -e
```
#### Adding cron expression 
The syntax to run the script every day at 8 am is: 
```bash 
0 8 * * *  python3 /path_file/file_name.py
```
[Check this crontab guide](https://phoenixnap.com/kb/set-up-cron-job-linux)

