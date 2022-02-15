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

In the last video we created a django project.
And looked at the files that are automatically generated for all new django projects.
These files were created by the start project command which comes with the django admin utility.
And include manage.py.
As well as the files that were created for us in our project directory.
Which in our case is called django_todo
When we ran our project for the first time using the python3 manage.py runserver command.
You might have noticed that a couple of other new items were automatically generated.
The pycache directory which contains compiled python code.
And the more important one here which is db.sqlite3.
This file will act as our database for the project.
So you want to be really careful not to delete or change this file in any way.
Since doing so will cause a lot of problems with our project.
And most likely make any data that we've put into the database unrecoverable.
With that said let's talk a bit more about how Django works.
Django projects are organized into small components called apps.
You can think of an app as a reusable self-contained collection of code.
That can be passed around from project to project in order to speed up development time.
So if you need an authentication system for example that handles logging in
logging out password resets and so on.
Rather than build your own you could use a Django app. And simply install it into your project.
Almost everything that we do in Django is going to revolve around these apps.
So let's create one now using the manage.py startapp command.

# __URLs - CREATING APPS__
    - Since we're going to build a to-do list. Let's create an app called todo
        To do that we can type python3 manage.py startapp todo
        You'll see this creates another folder called todo in the file explorer.
        And if we open that folder we'll see a number of other items
        We'll get to all of these eventually but for now we're going to focus on
        only one of them and that file is views.pi
        If we want to build a todo list web application.
        The first thing that we obviously need to be able to do is render some sort of
        web page
        You might recall from the intro video to this module that the views in the model
        view template design pattern.
        Are the mechanism by which users on the front end of our app can communicate
        with the back end where the data lives.
        In our case, that data is going to be our to-do items.
        So we need to render some sort of an interface that allows our users to interact with those items
        Just to demonstrate how this is going to work.
        Let's define a simple python function in views.py called say_hello
        And literally all this python function is going to do.
        Is take an http request from the user and return an http response
        to the user that says hello
        And that's it. We're gonna need to import HttpResponse from the Django shortcuts
        which is built into Django.
        So we're going to import that here. And we'll talk more about this later.
        But for now just go ahead and import it. And that's it.
        So our python function is done.
        And it should say hello.
        But how do we make this function available to the web browser.
        The answer is we do it through urls.py which we spoke about briefly in the last video.
        In order to bring the pieces together here let's go to urls.py. And before we do anything else
        We know that we're going to need our python function from the views file.
        So let's import that right here at the top. By typing from todo.views import say_hello
        This is going to allow us to use the say_hello function inside of the urls file.
        Once that's done all that we need to do is define the url that's actually going to
        trigger the say hello function and return the http response to the browser.
        To do that we use the built-in path function which typically takes three arguments.
        It takes the url that the user is going to type in. In our case we're going to say hello.
        It takes the view function that it's going to return.
        Which is our say_hello function.
        And it takes a name parameter which we'll get to a bit later but for right now we'll just call it hello
        And that's it that's all it takes. So if we go ahead and save this file now.
        Jump down to our terminal and type python3 manage.py runserver
        to start our Django application.
        We'll see we have the service running now. And we get a service available on port 8000
        We can open the browser.
        And we get page not found why. Because we haven't typed /hello
        At the end of the url
        And there we go. There's our hello function saying hello to the browser.

## __Templates__
    - In the previous lesson we demonstrated the basic functionality of a django web application.
        This included writing a simple Python function in views.py
        that returns an HTTP response saying hello to the browser.
        And then connecting that Python function to a URL. Using the path function in urls.py.
        Let's say for instance that instead of just rendering a string though
        you wanted to render a heading in a paragraph of text.
        You might think that we could do something simple like this.
        Where we just write actual HTML.
        If you put a heading in here and say hello. And then jump to the end and put a paragraph of text.
        This is a paragraph.
        save it.
        And you would be right we actually could do that.
        If we run the server using python3 manage.py runserver.
        Click on open ports
        Then open browser. And go to our hello URL
        You'll see that we actually do get valid legitimate HTML in this response.
        But you can probably see how this would become really difficult to maintain
        when we start dealing with JavaScript and CSS and lots of HTML content.
        So to solve this problem Django provides a templating system which allows us
        to create HTML files in a template directory inside of each app.
        And then we render those templates with our Python functions instead of rendering
        simple HTTP responses or long drawn-out strings of HTML like this.

### __todo_list.html__

    - To get our app really started we're going to go to the to-do app folder.
        Right-click and create a templates folder inside of this.
        Then inside that templates folder we'll create another folder called todo.
        And inside of the todo folder create a file called todo_list.html
        and this is going to act as our first template.
        Now this folder structure here might seem a bit awkward and redundant at first.
        But there's actually a good reason for it. The reason that we're creating this
        secondary todo folder inside the templates directory
        is because when Django looks for templates inside of these apps
        it will always return the first one that it finds.
        So by separating it into a folder that matches its app name.
        We can ensure that we're getting the right template even if there's another template
        of the same name in a different app.
        With that done let's go to the todo_list.html template.
        And if you simply type HTML here and arrow down to the html5 item and press enter
        this will generate the basic boilerplate for an html5 file. So this is just a gitpod shortcut
        Now in the body of the HTML file we can add some real actual HTML
        So let's create a heading.
        And just say things I need to do. And then save this file.

### __views.py__
    - The next thing we need to do is update our view function.
        So that instead of returning this long string of HTML
        It returns our template instead.
        We can accomplish that using the render function which was imported into
        this views.py file when we created our app originally.
        The render function takes an HTTP request and a template name as it's two arguments
        And it actually returns an HTTP response like this. which renders that template.
        So instead of returning this HTTP response let's return render.
        Give it the request. And then in quotes we will give it
        todo/todo_list.html
        This is basically just a shortcut to writing a really long HTTP response filled with lots of HTML
        Instead of writing all that HTML as a string in Python
        We can write it in an actual HTML file and pass it to the render function to let Django do the work.
        Now that that's done let's just rename our function to something a little bit more applicable.
        Like maybe get_todo_list
        And get rid of this HTTP response import since we don't need it anymore.
        I'll save that.
### __urls.py__

    -   And now we need to head over to urls.py and change a couple of things around here
        First of all this hello URL is actually kind of annoying
        because when we launched the project without that URL we get the page not found error
        that you've seen at the beginning of this video and the end of the last one.
        It also doesn't really apply to what we're doing so I'm gonna actually wipe it out completely.
        And instead, I'm gonna replace it with just an empty string.
        This means that we don't need to specify any particular URL in order to hit that Python function
        so this is gonna act as our home page.
        I'm also gonna update the view function that this path returns to our new get_todo_list function
        And I'm gonna rename it so that the name matches the function it returns.
        So we'll change this to get to do list as well.
        Since this is our home page we could also call this something like home.
        but just to keep things clear and consistent for now we're gonna leave it like this.
        We also need to update the import since we're not using the say hello function anymore.
        So let's just wipe that out and replace it with get_todo_list.
        And save that.
### __settings.py__
        And the final thing that we need to do to finish this up is to move to Settings.py
        And add our to-do app to the list of installed apps.
        And this is going to allow Jango to know to look inside of that app folder for a templates directory.
        If we now run our app
        Using the Python3, we actually don't need to rerun it because it's already running.
        If we just go up to this tab and refresh.
        We will now get a page not found on the hello URL
        Because we've removed that. But if we remove the hello URL
        We now get our new HTML template things I need to do.
        And we are ready to really start digging into what Jango can do over the next few lessons.

# __Migrations and Admin__
    - Before we get much more involved with creating our to-do list.
        I want to take a step back and talk about some higher-level Django concepts.
        You may have noticed that each time we've run our project so far
        we keep getting this warning that we've got unapplied migrations
        and that our project may not work properly until we apply them.
        The warning tells us that we can run this migrate command from the manage.py
        utility in order to apply them.
        But what exactly is a migration. And why do we need them.

        Migrations are Django's way of converting Python code into database operations.
        In other words when you need to make changes to a database connected to a Django project.
        Instead of running raw sequel commands or using some other database language.
        Django will do everything for you and all you need to do is write Python code.
        The reason that we keep getting that warning when we run our project
        is because Django recognizes that even though we've created a new project and started an app.
        We haven't actually done anything to set up the sequel lite database that it created for us
        it's telling us that we need to run all the initial built-in database operations
        in order for our database to work properly.

        Before I do that let's take a look at three key commands you're going to need
        in order to understand migrations.

        - The first one is python3 manage.py makemigrations
        And we're going to run it with the dry run flag in order to see what it would do if we actually ran it.
        In this case it says that there are no changes detected and that's because we
        haven't actually done anything in our to-do app that requires database changes.
        When we start adding models and making changes to them later on
        We'll need to run this make migrations command without the dry run flag
        in order to tell Django to convert our Python code into sequel code.
        which can be executed on our database.

        - The second command we'll need is python3 manage.py showmigrations.
        And if we run that command we'll see that even though we don't have any
        migrations to apply for our own todo app.
        There are some built-in Django apps like authentication and the Django admin
        and a couple of others that already have some migrations that need to be applied.
        And applying these migrations we'll set up the database and allow us to create
        an admin user that we can use to manage it.

        -The final command that you'll need is the one the warning keeps telling us about.
        And that's the python3 manage.py migrate command.
        Let's run it with the plan flag in order to see what it's going to do.
        You can see that these initial migrations are going to take care of some basic requirements
        like setting up the users groups and permissions tables.
        And altering the fields on some of those tables.
        So I'm going to run that command now to take care of all of this initial setup.
        So all of those migrations have been applied and they all say ok.
        
##### __Login authentication and superuser__

    - Now that that's done. there's one more thing I want to accomplish here.
        And that's giving us a way to actually log in and look at the tables in our database
        And potentially make changes to them if we need to.

    - To do that I'm going to use the command python3 manage.py create superuser.
        And it's going to ask me for a username which I'll fill in as ckz 8780
        An email address which I'll leave blank.
        And a password which I'll fill out and confirm.
        And we can see the superuser was created successfully.
        So at this point, I'm sure you're wondering how you actually log in with the user that you've just created.
        So let's bounce back over to urls.py and take a look.
        You'll see here that by default Django gives us a /admin path.
        So all we need to do to log in with our new superuser is run our project.
        With python3 manage.py runserver
        And we'll see now by the way that that warning is gone.
        And then once the project is running we can just open the browser.
        And go to /admin
        
    - We'll be able to log in with the new superuser that we just created.
        Once we've logged in we can see the authentication and authorization app
        that's been created.
        And the two tables users and group that have been created inside that app.
        And if we open up the users table we'll see our superuser has been created.
        In the next couple of lessons we'll start making changes to the database.
        By delving into the model layer of the Model View template design pattern.









































































