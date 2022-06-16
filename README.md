# Backend Main
This is an API that contains the main functions. This will be forked into our main backend project.

- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
  - [1. Create Virtual Environment](#1-create-virtual-environment)
  - [2. Install The Packages in `requirement.txt`](#2-install-the-packages-in-requirementtxt)
  - [3. Start The Development by Creating a New App](#3-start-the-development-by-creating-a-new-app)
  - [4. Register the Packages and the Applications](#4-register-the-packages-and-the-applications)
  - [5. Migrate the Database](#5-migrate-the-database)
  - [6. Create a New Initial User](#6-create-a-new-initial-user)
  - [7. Formatting your code using autopep8](#7-formatting-your-code-using-autopep8)
- [Deployment](#deployment)
  - [1. Create `f1-micro` instance](#1-create-f1-micro-instance)
  - [2. Enable swapfile for `f1-micro`](#2-enable-swapfile-for-f1-micro)
  - [3. Install SSL module for our Python 3.7](#3-install-ssl-module-for-our-python-37)
  - [4. Install Python 3.7](#4-install-python-37)
    - [4.1 Update packages list and install necessary packages to build Python 3.7.](#41-update-packages-list-and-install-necessary-packages-to-build-python-37)
    - [4.2 Download Python 3.7 release source code package](#42-download-python-37-release-source-code-package)
    - [4.3 Extract the package](#43-extract-the-package)
    - [4.4 Navigate to Python 3.7 extracted directory](#44-navigate-to-python-37-extracted-directory)
    - [4.5 Run the `configure` Script](#45-run-the-configure-script)
    - [4.6 Start the Python process build](#46-start-the-python-process-build)
    - [4.7 Install Python binaries](#47-install-python-binaries)
  - [5. Prepare and test the API](#5-prepare-and-test-the-api)
    - [5.1 First, we need to clone this repository](#51-first-we-need-to-clone-this-repository)
    - [5.2 Second, Install `default-libmysqlclient-dev`, this is to fix an error when installing `mysqlclient`'s pip package.](#52-second-install-default-libmysqlclient-dev-this-is-to-fix-an-error-when-installing-mysqlclients-pip-package)
    - [5.3 Install `pip` packages by running this command inside cloned repository.](#53-install-pip-packages-by-running-this-command-inside-cloned-repository)
    - [5.4 Install Gunicorn](#54-install-gunicorn)
    - [5.5 add allowed host to your external ip in `_main/settings.py`. In this case, I will use my external ip as allowed host](#55-add-allowed-host-to-your-external-ip-in-_mainsettingspy-in-this-case-i-will-use-my-external-ip-as-allowed-host)
    - [5.5 Create a firewall rule first](#55-create-a-firewall-rule-first)
    - [5.6 Run the server](#56-run-the-server)
  - [6. Run the server in the background process](#6-run-the-server-in-the-background-process)
  - [7. See if the server successfully listen to port 8000](#7-see-if-the-server-successfully-listen-to-port-8000)

## Repository Structure
Here is the overview of the repository's structure.
```
.
├── _main
│   ├── __init__.py
│   ├── __pycache__
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .gitignore
├── LICENSE
├── manage.py
├── README.md
├── requirement.txt
└── <your-apps-directory>
```

## Getting Started
### 1. Create Virtual Environment
Let's start this learn by creating your virtual environment (venv). Please refer to this link to see how to make it: https://gist.github.com/ryumada/c22133988fd1c22a66e4ed1b23eca233

### 2. Install The Packages in `requirement.txt`
```bash
pip install -r requirement.txt
```

### 3. Start The Development by Creating a New App
```bash
django-admin startapp app-name
```

### 4. Register the Packages and the Applications
Register the package you want to use and the application you've created on `settings.py` inside the `_main` directory. Then find the `INSTALLED_APPS` variable and insert the package name as the value.

### 5. Migrate the Database
```bash
python3 manage.py migrate
```

### 6. Create a New Initial User
```bash
python3 manage.py createsuperuser --email admin@example.com --username admin
```

### 7. Formatting your code using autopep8
This is used to follow pep 8 coding standards.
```bash
autopep8 --recursive --in-place --aggressive tokens
```

## Deployment
We are deploying this app into a Google Cloud Engine (GCE). There is some steps need to do for deploying this app into GCE. We use `f1-micro` machine type.

### 1. Create `f1-micro` instance
The first step is you need to create an `f1-micro` instance with **20GB** Standard Persistent Storage. You can create it from GCE console.

### 2. Enable swapfile for `f1-micro`
We need to create swapfile for `f1-micro` instance. This is used to make the program not killed by exhausted small ram that `f1-micro` have.

We need to ssh into our instance first, then type these scripts into the instance shell.

```bash
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

> source: https://redstapler.co/cost-of-hosting-wordpress-website-on-google-cloud/

### 3. Install SSL module for our Python 3.7
Our f1-micro instance is used Debian Linux 11. So, these packages will satisfy SSL module error when installing packages using `pip` package management.

```bash
sudo apt install libssl-dev
sudo apt install libncurses5-dev
sudo apt install libsqlite3-dev
sudo apt install libreadline-dev
sudo apt install libtk8.6
sudo apt install libgdm-dev
sudo apt install libdb4o-cil-dev
sudo apt install libpcap-dev
```

> source: [Rafael Beirigo's answer at Stackoverflow](https://stackoverflow.com/a/49696062/11332583)

### 4. Install Python 3.7
This is the main step for installing Python 3.7. There is some commands that need to execute:

#### 4.1 Update packages list and install necessary packages to build Python 3.7.
```bash
sudo apt update
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev wget libbz2-dev
```

#### 4.2 Download Python 3.7 release source code package
There are two ways to download the package, by using one of these commands:

- using `wget`
```bash
wget https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tgz
```
- or using `curl -O`
```bash
curl -O https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tgz
```

#### 4.3 Extract the package
```bash
tar -xf Python-3.7.9.tgz
```

#### 4.4 Navigate to Python 3.7 extracted directory
```bash
cd Python-3.7.9
```

#### 4.5 Run the `configure` Script
The script will perform a number of checks to make sure all of your dependencies are present in your system.

```bash
./configure
```

If you add the `--enable-optimizations` option, this will make the build process slower. Especially we are using `f1-micro` that have small resources. In my case, the build process needs to run **416 tests** after the build process.

Please use the option if you use more stronger instance. Here is the script example if you use the option:

```bash
./configure --enable-optimizations
```

#### 4.6 Start the Python process build
The build process will take some time to finish. Before you execute this command, you can install `htop` first to monitor your CPU usage that used by this process.

```bash
sudo apt install htop
```

You can activate `htop` in a separated ssh session terminal.

```bash
htop
```

If you're ready, then you can run the build command in the first ssh terminal.

```bash
make
```

We need to run `make` command inside `Python-3.7.9` directory. Because we use `f1-micro` instance which just have 1 CPU core, we don't need `-j` option. The option is used to run the build process using more than 1 CPU core.

Here is the example of the build process command using 4 core CPUs:

```bash
make -j 4
```

#### 4.7 Install Python binaries
Install python binaries by running this command:

```bash
sudo make altinstall
```

if you run `sudo make install`, it will replace default python installation in your system.

- If you run `sudo make altinstall`, you will access your installed python binary like this:
```bash
python3.7
```
- But if you run `sudo make install`:
```bash
python3
```
or
```bash
python
```

> source: https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/

### 5. Prepare and test the API
There is some steps need to do:
#### 5.1 First, we need to clone this repository
```bash
git clone <link-to-this-git-repository>
```

#### 5.2 Second, Install `default-libmysqlclient-dev`, this is to fix an error when installing `mysqlclient`'s pip package.
```bash
sudo apt install default-libmysqlclient-dev
```

> source: https://stackoverflow.com/a/5178698/11332583

#### 5.3 Install `pip` packages by running this command inside cloned repository.
```bash
python3.7 -m pip install -r requirements.txt
```

#### 5.4 Install Gunicorn
```bash
python3.7 -m pip install gunicorn
```

#### 5.5 add allowed host to your external ip in `_main/settings.py`. In this case, I will use my external ip as allowed host

```python
ALLOWED_HOST = ["123.456.789.123"]
```

#### 5.5 Create a firewall rule first
Before we run the gunicorn to run the server, first we need to create a firewall rule. In this case, I need to create a firewall with port 8000.

![Pasted image 20220616122854](assets/allow-drf-default-port.png)

> please ensure you create your firewall rule for the network used by our `f1-micro` instance.

#### 5.6 Run the server
You can test the api by running this command:
```bash
python3.7 manage.py runserver 0.0.0.0:8000
```

or you can use `gunicorn`:
```shell
python3.7 -m gunicorn -b 0.0.0.0:8000 _main.wsgi
```

### 6. Run the server in the background process
stop the command and run this to send the process to background:
```shell
python3.7 -m gunicorn -b 0.0.0.0:8000 _main.wsgi &
```

The command above will return `pid` number for the process.

You can see the running jobs by running this command:
```shell
jobs -l
```

### 7. See if the server successfully listen to port 8000
You can also run this command to see if the server successfully listen to port 8000:
```shell
sudo lsof -n -P -i TCP:8000 -s TCP:LISTEN
```

If there is no `lsof` you can install it:
```shell
sudo apt install lsof
```
