# __Hello Django__

## __ installing django__

Since this video was created Django have introduced a new version that will be automatically installed if you use the command in the video.

To ensure that you get the a version of django that will work while following these videos, instead of the command pip3 install django, please use this:

pip3 install Django==3.2

Django 3.2 is the LTS (Long Term Support) version of Django and is therefore preferable to use over the newest Django 4

    - To do this we're going to use a tool called pip.
        And pip is a recursive acronym that stands for pip installs packages.
        And it's widely accepted as the industry-standard tool for installing Python packages.
        Behind the scenes, pip is connected to the Python package index
        which is a central repository for tens of thousands of different Python packages and utilities.
        So we can use pip to install all kinds of useful tools that are written in Python and that includes Django.
        To do this let's type pip3 install django
        And we'll see that Django is downloaded from the Python package index and installed here in gitpod.
        Notice that we typed pip3 by the way when installing this.
        Because we want to install Django for Python version 3.
        And using only pip would install it for python version two.
        Before we continue it's useful to know what it actually means when Django
        or any package for that matter is installed.
        In the literal sense what pip did was download a bunch of Python files from
        the Python package index.
        And copy them into a directory here in our workspace.
        That directory will usually be called site-packages and in gitpod we can
        access it by using the CD or change directory command.
        So we're gonna CD into /workspace/.pip-modules/lib/python3.7/site-packages/
        And then the site-packages directory.
        And if we now use the ls -la command in this directory to list out all of the files and directories inside it.
        we can see that Django along with the other requirements that came in with it
        are installed in this directory.
        So any packages that you install with pip will end up in this site-packages directory.
        You should feel free to explore this directory to learn more about the packages your installing.
        But keep in mind you should never change anything in here since it
        could corrupt your version of Django or even your Python installation.
        We can use a shortcut cd - to get back to the last directory that we were working in.
        So now that we've got Django installed. We're ready to create our first django project.
        Django comes with the built-in admin command for things like starting projects
        and other core functionality.
        So let's use that to create a project.
        We'll type Django admin start project
        And we'll call this project Django_todo
        And put a dot at the end of this command this will signify that we want to create
        this project in the current directory.
        If we look in the file explorer now we'll see we have two new items we've got Django_todo
        And manage.py
        This is our project directory. The django_todo folder.
        And manage PI as a management utility we'll need throughout the project.
        If we open the django_todo folder there's an __init__.py file which was automatically created
        to tell our project that this is a directory we can import from.
        We've also got three key files in here. settings.py, urls.py and wsgi.py
        settings.py contains the global settings for our entire Django project.
        So things like whether we want to show debug information when errors happen.
        And things like where our HTML templates are located.
        And which database we're going to connect to. These are all controlled in the settings.py file
        urls.py contains the routing information that allows our users to type a specific
        URL into their address bar. And hit a specific Python function.
        So this is analogous to app.root in flask.
        And finally we have wsgi.py which contains the code that allows
        our web server to communicate with our Python application.
        And that's it. That's all we need to start a new Django project.
        In order to run our project.
        We can use that manage.py utility. By typing Python3 manage.py runserver
        This will tell us that a service is listening on port 8000 but it's not exposed.
        So we will expose that. And then click on open browser.
        And there we go the install worked successfully.
        Congratulations we have created our first django project.

# __URLs__
    - 












































































