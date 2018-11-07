import github, sys, os, re

def testAuth(g):
    try:
       rate = g.get_rate_limit()
    except github.BadCredentialsException as e:
        print("Error authenticating. Bad Credentials. Make sure you are uisng the correct token and try again.")
        exit(1)
    except github.TwoFactorException as e:
        print("GitHub requires a onetime password for two-factor authentication. Please remove two-factor authentication and try again.")
        exit(1)
    except Exception as e:
        raise e
    if rate.core.remaining <= 0:
        print("You have exceeded your rate limit. Please try again later.")
        exit(1)

def checkIfExists(repo, shortlink):
    try:
        repo.get_file_contents(pathToShortlink(shortlink))
        return True
    except github.UnknownObjectException:
        return False

def generateMessage(shortlink, url):
    return "creating shortlink for {} redirecting to {}".format(shortlink, url)

def validateUrl(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url)   

def pathToShortlink(shortlink):
    return "shortlinks/{}.md".format(shortlink)

def generateShortlinkFileText(shortlink, url, g):
    return """---
permalink: /{}
added_by: {}
redirect_to:
- {}
---""".format(shortlink, g.get_user().login, url)



if len(sys.argv) < 2:
    print("You must pass a GitHub OAuth token.")
    exit(1)

REPO = "dot-slash-cs/dot-slash-cs.github.io"

g = github.Github(sys.argv[1])
testAuth(g)

try:
    r = g.get_repo(REPO)
except github.UnknownObjectException as e:
    print(e)
    print("Repository could not be found. Make sure the repository is correct.")
    exit(1)


shortlink = ""
while not shortlink:
    shortlink = raw_input("What shortlink would you like to create?: ")
    if not shortlink or checkIfExists(r, shortlink):
        print("ERROR: '{}' already exists or is invalid. Please choose another shortlink...".format(shortlink))
        shortlink = None

url = ""
while not validateUrl(url):
    url = raw_input("Please enter a valid URL for the shortlink (i.e. https://example.com): ")

try:
    r.create_file(pathToShortlink(shortlink), generateMessage(shortlink, url), generateShortlinkFileText(shortlink, url, g))
except Exception as e:
    print(e)
    exit(1)