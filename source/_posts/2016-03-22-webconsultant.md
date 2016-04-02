---
layout: post
title:  "WebConsultant"
date:   2016-03-22 00:05:00
category: project
---

# (From Project's README):

WebAdvisor's interface is somewhat muddly and difficult to work through, but especially so when you're trying to figure out when exactly your classes are and what your weekly schedule looks like. This projects aims to develop a web application that can take care of that automatically.

##Execution Essentials

To run *WebConsultant* for testing, you will need:
- [Python](https://www.python.org/downloads/) (popular high-level programming language)
- [Selenium WebDriver](http://www.seleniumhq.org/docs/03_webdriver.jsp) (tool for scripted/programmatic web browsing)
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) (GUI browser)
- [PhantomJS](http://phantomjs.org/) (GUI-less, or "headless", browser)

Have Python and Selenium WebDriver installled, and have the ChromeDriver and PhantomJS executables in the same directory as the Python files. To run *WebConsultant*, navigate to the directory containing the Python files in command line and use `python parser.py`.

##Current Capabilities

At the moment, *WebConsultant*:
- takes course information for two sections from the user
- searches WebAdvisor for the two sections
- parses section information from the Section Information page
- prints the information for both sections, formatted, onto the console

##Miscellaneous Mentions

Built by Ohlone Students, for Ohlone Students.

Developed and tested with Python 2.7.11 on Mac OS X 10.11.3