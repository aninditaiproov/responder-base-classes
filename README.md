# Responder-base-classes: Base Classes for [Responder (kennethreitz)](https://github.com/kennethreitz/responder#installing-responder)

[![Build Status](https://img.shields.io/travis/com/iancleary/responder-base-classes/master.svg)](https://img.shields.io/travis/com/iancleary/responder-base-classes)
[![image](https://img.shields.io/pypi/v/responder-base-classes.svg)](https://pypi.org/project/responder-base-classes/)
[![image](https://img.shields.io/pypi/l/responder-base-classes.svg)](https://pypi.org/project/responder-base-classes/)
[![image](https://img.shields.io/pypi/pyversions/responder-base-classes.svg)](https://pypi.org/project/responder-base-classes/)
[![image](https://img.shields.io/github/contributors/iancleary/responder-base-classes.svg)](https://github.com/iancleary/responder-base-classes/graphs/contributors)

## More Examples

TODO: See [todo link that goes to docs](#) for more details on features available in Responder.


# Installing Responder-base-classes

Install the latest release:


    $ pip install responder-base-classes


Only **Python 3.6+** is supported ([as required by the Responder package](https://github.com/kennethreitz/responder#installing-responder))

# The Basic Idea

The primary concept is to provide base classes for REST APIs with JSON and [Responder's class based views](https://python-responder.org/en/latest/tour.html#class-based-views)

- Extend Responder with extensions similar to [Flask's extensions]( http://flask.pocoo.org/extensions)
- Responder executes the on_request method followed by on_{method}, where method is an HTTP verb.
- Two Base Classes are provided: OpenBaseView and AuthBaseView
- OpenBaseView requires no authorization but checks content-type and implemented routes
- AuthBaseView extends OpenBaseView with Basic Auth and Custom Auth 
   - with placeholder classes for your implementation of a User class


# Thoughts
- move to pipenv?

----------

# Contributing Guide (Welcome!)

### First Steps to fix an issue or bug
- Read the documentation (working on adding more)
- create the minimally reproducible issue
- try to edit the relevant code and see if it fixes it
- submit the fix to the provlem as a pull request 
- include an explanation of what you did and why

### First steps to contribute new features
- Create an issue to discuss the feature's scope and its fit for this package
- try to edit the relevant code and implement your new feature in a backwards compatible manner
- create new tests as you go
- update the documentation as you go
- run black to format you code as you go

### Requirements to merge code
- you must include test coverage
- you must update the documentation
- you must run black to format your code (run the snippet below from the base directory)

~~~~
black responder_base_classes/ tests/ setup.py
~~~~

---

### Recommended background reading on etiquette for contributions
- Mike McQuaid's [how-to-not-fail-at-using-open-source-software-in-your-organisation](https://mikemcquaid.com/2018/09/04/how-to-not-fail-at-using-open-source-software-in-your-organisation/)
    - No affiliation, just a fan of the article (the quote block below is from the article)
    - The Contributing Guide is based on it

> If you follow these steps your experience using and modifying OSS will be much more pleasant. What if you don’t feel confident making changes?
> *  help others help you by helping yourself
> You need to be willing to put in the time and effort to make it easier for others to help you. Starting with the easiest:
> 
> * read all the documentation before asking for help
> * create minimally reproducible issues
> * look at the code you think might be relevant
> * try to edit the relevant code and see if it fixes the problem
> * submit the fix to the problem as a pull request
> 
> Similarly on your issues, pull requests, tweets and everything related to open source:
>
> * have reasonable expectations (most maintainers are volunteering in their free time)
> * prioritise maintainers’ time (there’s more of you than there is of them so your time is less valuable)
> * defer to maintainers (it’s up to them if changes get made or merged; argue respectfully)
> * help others where you can (if you want help you need to give help)
>
> If you want to read more about how to do all aspects of OSS well check out the Open Source Guides. These are the best single resource on the internet on how to contribute to, start and maintain an open source project.
>
> Finally, just be a nice, kind human. It’s surprising how appreciated (and how rare) kind words are in OSS. Use them generously and you’ll reap the rewards.

Thank you and I hope you find my/our work useful!  Have a nice day :)
