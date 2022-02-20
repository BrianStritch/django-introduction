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

# __Models Part 1__
    - In the last lesson we ran Django's initial database migrations in order to
        set up our sequel Lite 3 database.
        And created a superuser that we could use to manage it.
        We also took a brief look at the built-in Django admin panel.
        And we were able to see the users and groups tables that were created by those initial migrations.
        To get back to our to-do list app.
        In this video we're gonna create our own Django model
        which will represent records in a new table in the database.
        Specifically, our model will represent the characteristics of all
        todo items which will live in a new items table.
        To better understand how models work let's think of our sequel Lite database as an Excel spreadsheet.
        If you think of the database as the entire spreadsheet then each table in the
        database is represented by a single sheet.
        For example, we know that there's a user's table in the database already
        so we could rename this sheet to users.
        Then on the user's sheet the first row should describe some things that we
        know all users will have in common.
        For example they probably should all have a user id.
        username, password, email, first name, and last name.
        Each subsequent row then represents an individual user record in our database.
        So, for example, our superuser might look something like this
        With the username a password email
        a first name and the last name.
        And to add more records to the database we just add more rows with all the relevant information.
        If we create an item sheet to represent our todo items.
        We need to consider what types of things all todo items might have in common.
        To keep it simple for now let's say that each item only has a few attributes
        An item id a name and a done status
        We might have a few items like learn HTML, learn CSS, learn JavaScript, and learn Django.
        And HTML CSS and JavaScript are already done so we can mark those is true.
        But learning Django still needs to be completed so we'll leave that as false for now.
        In this spreadsheet the model that describes what each item looks like
        is this first row which contains the column headers.
        Heading back to our code. We need to essentially duplicate this design in Python
        and to do it we're going to use the models.py file inside of the to-do app
        In this file let's define a class called item. The class here is analogous to the item
        sheet in the spreadsheet we were just experimenting with.
        When Django sees that we've created a new item class it will automatically create
        an items table when we make and run the database migrations.
        There's a key thing you need to understand here though. And that's that by itself this class won't do anything
        We need to use something called class inheritance to give it some functionality.
        You'll see at the top of this file there is already an item called models imported from django.db
        What this means is that we're literally importing the model's folder from the
        Django / DB directory in our project site-packages.
        And by doing so we gain access to everything in that folder.
        Just like when we imported our view function in urls.py
        To dig even deeper if you go to the Django source code on github.
        You'll see that you can drill into the django directory.
        The db directory and finally the models directory and you'll see a number of files.
        if you look in __init__ .py
        You'll see that all it is is a bunch of imports pulling in various python files and classes.
        So that we can just import the entire model's folder and be able to access all of these things.
        In particular, if you look here in the imports. You'll see that we were able to
        access the model class from django.db.models. base
        Which is where the default model class that's built into Django lives.
        You could even go into base.py And find the literal class definition for model.
        So all this functionality that's defined in the model's folder and all its files
        is accessible to us just by importing models from django.db
        And that's what will give us the ability to start our own model with all of that base functionality.
        To do that I'm going to inherit the base model class by putting models.model
        here in the parentheses so that our item class can do everything the built-in Django model class can do.
        This concept of class inheritance it's going to be very important as you progress
        in your understanding of python and object-oriented programming in general.
        For now just remember that if you need functionality from one class to be available in another.
        All you need to do is inherit the one you need.
        Now that we've inherited all the base functionality from the built-in Django model class.
        All that's left to do is define the attributes that our individual items will have.
        We can skip the Id field that we had in our spreadsheet since Django will create that for us automatically.
        But we do need to define a name field and a done status field.
        The name field will use one of the built-in Django fields called a char field.
        Which means it will just have characters or text in it. And the done field will be a boolean field.
        So models.boolean field
        Meaning it can be either true or false.
        Finally let's give these fields a couple of restrictions I'm going to add the max length attribute
        on the name field just to keep the length of our item names reasonable.
        So we'll say 50 characters
        And add both null equals false. And blank equals false
        To prevent the creation of todo items without a name. The null equals false attribute here
        prevents items from being created without a name programmatically
        and blank equals false will make the field required on forms.
        This way we're certain that a todo item can't be created without a name
        whether it's done in Python code. Or by a user in a web form or even an administrator in the admin panel.
        And next I'm gonna do the same for the done field. Null equals false and blank equals false.
        And I'm gonna add a default value of false here just to make sure
        that to-do items are marked as not done by default

# __Models part 2__
    - So we've created our item class now and we need to actually create the table in
        the database. You might remember that Django uses migrations to handle
        database operations. So what we need to do is use the command python3 manage.py
        by make migrations in order to make a migration file. So I'm going to stop the server now.
        And run python3 manage.py make migrations.
        And I'm going to run it with the dry run flag just so that we're sure of what it's going to do.
        And I'm not making any unintended changes. And if I do that I can see that it
        all looks good so I'm gonna run it for real now.
        And what happens here is Django sees
        that we've added a new model to our app so it creates a new Python file in the
        migrations folder. That contains the code to create that database table based on our model.
        So this code will be converted to sequel by Django and executed on the
        database when we actually run the migrations.
        We can also use the python3 manage.py show migrations
        command to see that we do in fact have an unapplied migration on our to-do app now.
        And to apply it all we need to do is run python3 manage.py migrate
        I'm gonna run this with the plan flag. Once again just to be 100% certain that I'm not
        doing anything unintentional.
        And we can see that it's going to create the model item. That's the planned operation.
        And that all looks good so I'm going to go ahead and run it now.
        And that migration has been applied.
        Even though the items table has been created and we could start creating
        items programmatically now.
        We won't be able to see our items in the admin until we expose them.
        
    - To do that we need to register our model in the todo apps admin.py file.
        I'm gonna go to admin.py and import our item model from .models
        So from models. import. Let's put this at the top actually.
        From .models import item.
        And this says from the current directories models file we want to import the item class.
        And then we're going to use the admin.site.register function.
        To actually register our item model.
        If we save that. Now we can run our project with python3 manage.py runserver
        If we go to the admin panel now we can see our new items table.
        To create a new item we can simply click on items.
        Click add item.
        And fill out the form.
        So let's make an item called create_item_class
        Which is done.
        We'll click Save.
        And let's add another one.
        Register item model.
        Which is also done.
        I'll click Save.
        And we can see that these items have been created but they don't have very friendly names.
        So let's make one last change to our model just to clean that up.
        The item object value in the admin is actually coming from the fact that we
        inherited the base Django model class. When we created our item model.
        By default all models that inherit this base model class will use its built-in string
        method to display their class name followed by the word object.
        Just so that there's sort of a generic way to display them.
        And you can actually see this method defined in the base model class in django.db.models.base.
        If you want to take a look. You can see the string method right here.
        It returns object. And then the primary key. So that's what we see in the admin panel.
        To change that we need to actually override that string method with our own.
        And we can do that just by redefining it here in our own class.
        so if we define __string__
        And this is going to take in self. Which is the class itself as its own argument.
        And all it's going to do is just return self.name.
        So this is going to return the item class's name attribute which in our case
        is going to be the name that we put into the form.
        So this is the beauty of class inheritance we still get all of the default functionality
        of the default Django model class.
        But we can override this string method just to change how our items are displayed.
        Doing this will make sure that in the admin we see our item names instead of item object.
        So if we go ahead and save that. And then go back to the admin. And refresh.
        We'll see that the items that we've created now display their names.
        Instead of the generic values that were displayed before.

# __Rendering Data part 1__
    - Before we get started with rendering data.
        I want to take just a quick moment to fix some problems in our code.
        If you're using gitpod you'll notice that it has a problems tab at the bottom near the terminal.
        One thing this tab is doing is monitoring our code for issues in coding style using a Python package
        called flake8.

        Flake8 is based on a style guide for Python called pep8.
        And you can see up here that pep8 guides software developers on things like.
        indentation using tabs versus spaces, maximum line length, how to write good comments, and so on.
        Flake8 uses these guidelines to act as a sort of spell checker except it's looking
        for things like bad coding practices, packages were importing that we're not using, and so on.
        So I've noticed I've got a few problems in the code I've written so far.
        So I'm just gonna quickly fix those just to demonstrate some generally good coding practices.
        This isn't critical to our project.
        But in professional software development you should just always strive to follow
        industry-standard guidelines. so that's all I'm doing here.
        The first one I'm going to ignore since it's in a migration file. And those are automatically generated.
        But you can see here it's just telling us that line 17. At a hundred and fourteen
        characters is too long. Because it's greater than 79 characters which is the
        standard guideline from pep8.
        The next couple we can easily fix though. First in admin.py it looks like we need to
        add a new line at the end of the file.
        So I'm gonna go there and just do that. And save it. And that takes care of that one.
        Then in models.py. It looks like we need to add a new line at the end of the file so I'll do that.
        And we also need to add two blank lines above our class definition.
        So if we do that and save it. We can see that all these errors except for the one
        that we're ignoring are now gone.

    - Getting back to the task at hand. Let's talk about rendering data.
        In the last video we set up our item model and put a couple of items in the database.
        The next thing we need is the way to display the to our users.
        So we need to find a way to get those items from the database into a template.
        Remember that in the Model View template design pattern
        The views represent the programming logic that allows users to interact with
        the database through the templates that they see.

    - That means that we should probably start in views dot.py
        And by the way if we look here it looks like we have the same problems that we had in models.py
        We need two blank lines above our function definition.
        And one new line at the end of the file. Just to get rid of those flake eight errors

    - In views.py, We need access to the item model in this file so the first thing I'm going to do
        is right at the top. From .models import item.
        That's going to allow us to use the item model in our views.
        In the get_todo list function. we can then get what's called a query set of all the
        items in the database.
        By creating a variable. Let's call it item. Equal to item.objects.all
        And since this is going to return multiple items let's call it items.
        Next I'm going to create a variable called context. Which is just going to be a
        dictionary with all of our items in it.
        So it needs a key of items. And that value is going to be our items variable that we just created.
        And finally I'm going to add that context as a third argument to the render function.
        And this will ensure that we have access to it in our todo list .html template.

Once we save this we've got everything we need to ensure complete communication.
Between the users of our app on the front end. And our database on the back end.
I'm going to go down to the terminal now and start the app with python3 manage.py runserver
And then open the page. You won't see any change to the template yet because we haven't actually edited
the template file so let's do that now.

    - If we head back to our project and open the template file.
        We can render the items key from the context dictionary that we just created
        using this double curly bracket syntax.
        This is called a template variable and anything that you return to the template
        in that dictionary can be rendered in the same way.
        That includes almost anything that you can use in Python
        Meaning you can return strings, numbers, lists, other dictionaries, or even functions and classes.
        So let's save this and then refresh the template and see what we've got.
        And as expected we have the value of the items key from the context dictionary
        which you might recall I said was a Django query set.
        We're getting pretty close to having a nice list of our items here but this
        output isn't very user friendly.

        A query set is kind of like a list which means we can iterate through it in our
        template just like we could iterate through a list in Python.
        If we go back to the file.
        We can adjust the syntax slightly to turn it into a loop that will iterate through our items.
        In Django templates any template variables we'll use this double curly bracket syntax.
        And any other kinds of functionality like for loops, for example, wi'll use this
        opening and closing curly bracket % sign syntax which looks like this.
        So opening and closing.
        And for a for loop, for example, we might do something like for item in items.
        And then the closing tag will be an end for.
        Now inside this loop we can do anything we want which revolves around an item.
        So I'm going to create a table surrounding the loop and for each item, in items, we want to create a row.
        And inside that row, we want to td elements.
        And let's just tab those in.
        The first td element is going to contain the item's name.
        So we'll use the template variable syntax there.
        And call item .name
        And the second one will contain the items done status.
        so item dot done.
        And personally just to keep my code clean I prefer to tab in for loops
        just as I would with regular HTML.
        This is 100% a personal preference.
        If we save this and go back to refresh our template one more time.
        we've got our items and they're done status rendered out here.
        And just to clean it up let's get rid of this query set so go back to the template.
        And remove the item's tag there at the top.
        And save it. And then we can refresh. And that's a little bit cleaner.

# __Rendering Data part 2__
    - This looks okay but we can make it better.
        I'm going to go back to the template and update our loop to use an
        if statement inside it that will strike out the item if it's been done.
        Rather than rendering true or false for the done status.
        using the same syntax that we used for the for loop.
        We can create if-else statements in Django templates just like in python
        So let's create an if-else and if block here.
        And instead of rendering the name. We want to check whether the item is done
        and then render something accordingly.
        So what we need is.
        Three of these.
        The first is going to be if
        The second is going to be the else
        And the third is going to be the end if.
        And then all we need to do is check if item.done.
        We want to render a td. But strike it out.
        And otherwise, we just want to render a regular old td with the item's name.
        So let's save that and see what we've got
        And we can see that both of our todo items are now struck out because they're both done.
        To demonstrate that this really is communicating with the database. If we go to the admin.
        Go into the items table. Open up the second item that we created and uncheck its done status
        then save it.
        If we go back to the template and refresh we'll see that the second item is no longer struck out.
        There's one last thing i'd like to add here and that's to handle what should
        happen if our database doesn't have any todo items in it.
        To handle that we can use a special tag called empty. Right before the endfor tag.
        After the empty tag all we want to do is render a single row.
        With a single td element in it. Which says you have nothing to do.
        If I save that.
        Then go back to the admin. Open up the items table.
        And delete all the items.
        Our template will now show us that we have nothing to do.

# __Creating a New Item Part 1 CRUD - CREATE__
    - At this point we've seen how to render data from a Django database in a
        front-end HTML template. But users of our todo list app still don't have a way to
        actually interact with that data such as the ability to create their own todo
        items or mark them as complete. In this video we're going to cover the first
        part of a concept known as crud. Which stands for create, read, update, and delete.
        By giving users the ability to create their own to-do items.
        Generally, with crud, you'll want different templates for different operations.
    
    - Our home page at the moment represents the read operation in crud.
        To give users the ability to create an item.
        I'm going to simply duplicate the todo list at HTML template.
        Rename it to add_item.html.Then we'll open this new template.
        Update the header. To Add a Todo Item. And remove the table.
        I also need to add a link on the home page to access the new template.
        So I'm going to add that here right after the table. With an a href equals
        And we're gonna link this to add. And we'll just call it Add an Item.
        And just to be sure that we're starting at the root let's add a slash right in front of add.
        Next we need a view to display this template so let's go up to views.py
        And to keep it simple we'll just copy the get_todo list view and make some changes to it.
        I'm going to rename it to add_item
        Remove the items and context since we don't need them anymore.
        Change the template to our new add_item.html template.
        And remove the context since this view has no context at the moment.
        Lastly we need a new URL to access this template because right now
        if we click the link to add an item we'll get a page not found error.
        So I'm gonna go to urls.py and copy the URL for the home page.
        Change this URL to add
        Update the view to our new add_item view.
        And will update the name to add as well.
        And finally import the new add item view into this file to make it accessible to urls.py
        if we run the server now with python3 manage.py runserver
        And it looks like we forgot a comma at the end of this item here.
        So that should fix that.
        And looking good so the server is running now we can go to open ports.
        Open the browser. And click the link to add an item. And we can see our new view is working perfectly.
        Now we just need a way to actually add an item from this template.
        So let's go back to the add_item.html template and create a form element.
        This form is going to be the mechanism by which a user can enter the name for a todo item.
        And whether or not it's done.
        And to do that we're just going to need two inputs and a submit button.
        I'm gonna wrap them in paragraph elements inside a couple of divs for now
        just so they look a little cleaner.
        So the first thing that we need is three divs.
        The first two divs are going to have a paragraph element inside of them.
        So we'll add those here.
        And the paragraph there and the last div is going to be our submit button.
        So we'll tab that in and add a button element for the last div.
        And the first input is going to go inside this first paragraph.
        So I'll create that here and it's going to be an input of type text
        because this is where the name of the to-do item will go.
        And I'm going to give this input two attributes.
        One is ID Which will have a value of id_name.
        And the other is the name attribute. Which will have a value of item_name.
        As a quick review, the name attribute of this input is the name we'll use to access
        the input's value in our view function.
        And the ID attribute is the way that we can identify it on the page to apply its label CSS and so on.
        And speaking of the label let's apply a label to this input element right now by creating a label for equals id_name
        And giving it a value of name.
        Now to create the done status input. I just need to copy this and make a couple of quick changes to it.
        I'm gonna change the labels for attribute to id_done
        And obviously, give it a label of done instead of name.
        This is going to be a checkbox.
        And it will have the ID of id_done and a name of done.
        Lastly, we need to give our button here a type of submit.
        So that it'll submit our form. And let's give it a label of Add Item.
        Also just so this button has the same margins around it as the inputs above it.
        I'm gonna wrap a paragraph element around the button as well.
        The form is mostly done at this point the only thing it needs is a method of post.
        And an action of add. This is going to be our add URL that we're going to submit the form to.

# __Creating a New Item Part 2__
    - This would be a good time to talk about the difference between get and post requests.
        And that difference is quite simple. Get requests get information from the server.
        And post requests send or post information to the server.
        In our case we're going to be sending the data for a new todo item to the /add URL
        So we want to use post.
        On that note we do need to add a special template tag to the form as a security measure.
        Just inside the opening form tag whenever we're posting information in Django.
        We need to add the CSRF or cross-site request forgery token.
        This token is a randomly generated unique value which will be added
        to the form as a hidden input field when the forms submitted.
        And works to guarantee that the data we're posting is actually coming from our
        todo list app and not from another website.
        If we were to skip adding this token.
        Django would throw an error when we submitted the form because it wouldn't
        be able to guarantee that the post data wasn't coming from another site.
        With all that done the final piece of the puzzle here is how to handle what
        happens when the user clicks submit on the form.
        I'm gonna go back to views.py. And since we set the form action to our add URL.
        we need to add an if statement in the add item view to check what type of requests
        this is.
        If it's a get request we're already all set because all we want to do is get the
        add item.html template.
        However if the request to this URL is a post request that would mean it came
        from someone clicking the submit button on our form. And we want to actually
        create a to-do item and then redirect back to the home page to show the user
        their updated to-do lists.
        To do this all we need to say is if request.method equals post.
        we want to set a variable for the name and a variable for done
        And remember we can get these values using the name attributes from our form.
        So to get the items name we just need to look up request.post.get.
        And the name of that attribute which in our case was item_name
        For the checkbox it's a little bit different. Since it's just a boolean value but in
        order to check if the item is done. All we have to do is check whether the post
        data actually has a done property in it. By checking whether done in request.post
        At this point we should have everything we need to actually create a new item.
        We've already got our item model imported from .models up here at the top.
        And to create an item is actually extremely simple.
        All we need to do is call item.objects.create and give it these two variables.
        So name equals name done equals done. And that's it finally we need to return a redirect
        back to the get_todo list URL name.
        And in order to do that we're going to need to import redirect from the Django shortcuts.
        So what's gonna happen here is when somebody hits this add_item URL
        they're going to end up in this add_item view.
        If it's a get request then we'll just return the add_item HTML template by rendering it to them.
        But if it's a post request we'll get the information from the form that comes
        in from this template.
        And use it to create a new item.
        And then we'll redirect them back to the get todo list view.
        Where they'll see their updated todo list.
        So if we run the server now. Which I believe it's already running and it is.
        If we just go and let's just make sure that's saved.
        If we just go and refresh this. We now have a form so let's create a new item called
        learn how to create an item. Which is obviously done. And if we click add_item.
        We will see
        Things I need to do
        Learn how to create an item. Is marked off.
        We can go back and create another one.
        Learn something else
        And leave it as unfinished.
        Click add item And we can see that it is now working exactly as it should.
        We've now covered 50% of crud. We have the ability to read from our database.
        And the ability to create items in our database.


# __Forms__
 In the previous lesson we created a form in the add_item HTML template. Which allows users to add todo items to the database.
This works perfectly fine but creating forms manually leaves our application open to errors if we don't validate them properly.
For example if we create a form and forget to mark one of the fields as required. But that field is required on the database model. Django would try to create an item in our database with the missing field which could result in an error on the front-end
To alleviate this issue. In Django it's possible to create forms directly from the model itself. And allow Django to handle all the form validation.

#### __forms.py CRUD - READ__

    -   To make this happen we need to create a new file in the todo app directory called forms.py
        Inside the forms.py file we need two things.
        First from Django, we need to import forms which will allow us to leverage
        some of the built-in Django form functionality.
        And secondly, we need our item model.
        Just like when we created the item model itself.
        Our form will be a class that inherits a built-in Django class to give it some basic functionality.
        To set it up we need to create a new class.
        I'll call mine ItemForm and it's going to inherit all the functionality of forms.ModelForm
        To tell the form which model it's going to be associated with.
        We need to provide an inner class called meta.
        This inner class just gives our form some information about itself.
        Like which fields it should render how it should display error messages and so on.
        In this class the only thing I'm going to define our model. Which is going to be our item model.
        And fields which will tell it we want to display the name in done fields from the model.
        The idea of creating this form in Django is that rather than writing an
        entire form ourselves in HTML.
        We can simply render it out as a template variable.
        To make sure we've got it available for use in the template.
        Let's head to views.py and import the item form.
        With the form imported we can now create an instance of it in the add_item view.
        Create a context which contains the empty form.
        And then return the context to the template.
        This means that in the add item template we can now go delete all the fields we created ourselves.
        And instead render the form just like we would any other template variable.
        Loading the page now will show us that our new form renders just fine.
        But if you try to add a new item you'll see that we get an integrity error.
        Django is telling us that the not null constraint on the name field failed when trying to create an item.
        In other words, we set null equals false on the model to indicate we wanted the name to be required.
        But we're trying to create an item without a name.
        The reason we're seeing this error is that we've deleted the name and done fields
        we created ourselves and are instead using the Django form.
        But the view is still looking for the old fields we made ourselves.
        To fix it and finalize the functionality let's go back to the add_item view.
        Here in the request.post handler instead of trying to create the item manually.
        Let's let our new form from forms.py do it.
        To do that we can use a similar syntax to what we use to create the empty form.
        But instead here will populate the form in Django with the request.post data.
        Then we can simply call the is_valid method on the form.
        And Django will automatically compare the data submitted in the post request
        to the data required on the model.
        And make sure everything matches up.
        To save our item then all we need to do is call form.save and then redirect to the
        get_todo list view like we were before.
        If you go back to the add_item page now you'll see the form works as expected.
        You probably notice that when we removed our own form elements we
        lost the vertical layout.
        To get that back Django forms actually have a number of built-in methods we can use in the template.
        Such as. As p which will render the fields as paragraphs. And as table. Which will render them as a table.
        I'll use as p here to get our vertical styling back.
        With our Django form functional let's now move on to the next element of crud.
        Updating or editing items.

# __Editing An Item CRUD - UPDATE__
    - Now that our todo app has the ability to create items.
        In this video we'll give it the ability to edit existing items.
        To do that the first thing we need is a button next to each item that will take us to the Edit item page.

    - In the todo list.html template.
        I'll render a new td element in each row which contains a link with a button in it.
        The href on the link will point to a new URL we'll create in a moment edit.
        And we'll also append the items ID which is automatically generated by Django.
        If you click on these buttons and look at the URL. You'll see they give us URLs like edit/3 edit /4 and so on.
        These are the automatically generated django ids.
        As you can see these urls currently return a 404.
        And that's because thus far we haven't created either a view or a URL in the urls.py file.
        Let's start with the view

    - In views.py I'll create a new view called edit_item.
        This view will be pretty similar to the add_item view.
        But with a couple key differences.
        First along with taking in the request. This view will also take in an item ID parameter
        And that's the item ID we just attached to the Edit link.
        Also, this view will return a different template called edit item.html

    - Let's save this for now and create the edit_item template.
        It's actually almost a carbon copy of the add_item template.
        So I'll begin by just duplicating that renaming it to edit_item.html
        And making a few minor changes.
        First the title of the page can be changed to Edit a Todo Item.
        Then we can actually remove the form action entirely which will cause it
        to post to the same URL we're currently on.
        And lastly I'll change the button text to update item.

    - Now in urls.py. I'll create a new path which will point to edit /item_id
        Call the edit_item view. And have a name of edit.
        This angular bracket syntax here is common in Django URLs.
        And is the mechanism by which the item ID makes its way from links or forms
        in our templates.
        Through the URL and into the view which expects it as a parameter.
        After importing the Edit item view we should now be able to click the links on the home page.
        And access the Edit item template.
        You can see right now though that the form is missing.
        And that's because we've still got a few more things to do in the view to bring it all together.

    - Back in the edit_item view. Let's first get a copy of the item from the database.
        We can do this using a built in django shortcut called get_object_or_404
        Which we'll use to say we want to get an instance of the item model.
        With an ID equal to the item ID that was passed into the view via the URL.
        This method will either return the item if it exists. Or a 404 page not found if not.
        Then just like above we'll create an instance of our item form and return it to the template in the context.
        To pre-populate the form with the items current details.
        We can pass an instance argument to the form.
        Telling it that it should be prefilled with the information for the item we just got from the database.
        Lastly let's import the get_object_or_404 shortcut. And then take another look.
        We're almost there.
        The form is now on the Edit item page and it's pre-populated with the items data.
        But when we update it.
        it still doesn't actually update because we haven't written a post handler in the Edit item view.
        Let's go do that now.
        It's quite simple.
        I'm actually just going to copy the entire handler from the add item view and paste it in here.
        Making only one small change and that's to give our form the specific item instance we want to update.
        Everything else can remain exactly the same.
        And with that saved. We can now reload our site and see that updating items is working as expected.
        In the next video, we'll create another simple view as a shortcut to toggle in item status
        And complete the last bit of crud functionality.
        Giving users the ability to completely delete an item.

# __Toggling And Deleting An Item CRUD - DELETE__
    - Users of our web application now have the ability to do 75% of crud.
        We've covered creating an item. Reading items or listing them out on the home page.
        And updating an existing item.
        Let's add one more small piece of update functionality.
        Giving the user is the ability to quickly toggle in items done status.
        And then give them the ability to completely delete an item.

    - First in the todo list .html template.
        Let's copy the edit link and just change the URL and the button text to toggle.

    - We'll need an almost identical URL for this in urls.py
        So I'll copy the edit_item URL. and just change edit to toggle for the URL itself the view and the name.

    - You might notice now that if we import the toggle item view.
        Our list of imports here at the top is getting quite long.
        So let's change this slightly just to clean it up.
        Instead of importing each view individually.
        I'll just remove them all and change the import to from to do import views.
        Now I can simply add views dot in front of all the views.
        And everything is exactly the same. But a little less verbose.
        with the new URL ready. Let's go create a view for it.
        This one won't even have a template because it's just going to toggle the item status.
        And then redirect back to the to-do list.
        I'll call this view toggle_item so it matches what we put in urls.py.
        And like the edit_item view. It'll take in the request as well as the item ID the user wants to toggle.
        We can then use the same logic to get the item in question.
        Change it's done status to the opposite by using not.
        Which will just flip it to the opposite of whatever it currently is.
        And then save the item.
        So this will make it so that when a user clicks toggle. Our view will get the item.
        And if it's done status is currently true it will flip it to false and vice versa.
        Finally we'll just redirect back to they get_todo list view and we should be all set

    - For the last part of crud. The ability to delete items. Our structure will be
        pretty much identical to everything we've done so far.
        I'll start by copying the toggle item view.
        But instead of changing the item status and saving it.
        I'll simply delete the item and then redirect.
        Of course, we'll need a URL for this so let's head over to urls.py
        And copy the toggle item URL. Then change it to an appropriate URL. our new view.
        And an appropriate name.
        Lastly in the todo list template. We can simply add one more button to delete the item.
        Our users now have the ability to create read update and delete items.
        And we've covered every part of crud.
        Moving forward we'll talk about how to use built-in Django testing.
        To ensure our code is always working as we expect.

# ------------------------- __TESTING__  -------------------------------

# __Django Testing__
    - Like many development languages and frameworks including JavaScript and Python itself.
        Django has a testing framework available that we can use to create automated tests.
        That ensure our application is working as expected.
    
    - When we created the todo app you might have noticed that it provided us by default
        with a tests.py file.
        Inside this file you'll find that Django imports the test case class.
        This class is an extension of the Python standard library module called unit tests.
        Which provides us with a bunch of methods to assert various things about our code.
        Such as assert equal assert true assert false and so on.
        Testing in most programming languages and frameworks is based on these assertions.
        And we'll use them to test our code in Django as well.
        To get started let's create a class called test Django which inherits the built-in test case class.
        Giving us access to all its functionality.
        Inside our new class. Every test will be defined as a method that begins with the word test.
        I'll create one here called test this thing works.
        And it will take in self as its only parameter.
        Self here refers to our test Django class which because it inherits the test case class
        wi'll have a bunch of pre-built methods and functionality that we can use.
        For example inside the test this thing works method.
        I'll use the built-in assert equal method to determine whether one equals zero.
        Obviously we know one is not equal to zero so this test should fail.
        To run it we can head to the terminal and use the command python3 manage.py test.
        Understanding this output is pretty simple.
        At the very top, there's an F indicating that this test failed and our thing we're expecting to work in fact does not work.
        Beneath that we see exactly which test failed and why.
        And at the bottom a summary telling us it ran one test.
        How long it took and how many failures there were.
        Let's copy this test a few times.
        And make some small changes to demonstrate how it would look if there were more
        I'll call these new tests test this thing worked two three and four.
        I'll correct the first one so it passes. Then we'll make the second one fail.
        The third will have a syntax error.
        And the fourth will also fail.
        Now running Python3 manage.py test again.
        You'll see there's a dot for the first test which passed.
        A F for the ones that failed.
        And an E for the one that had an error.
        This .F and E syntax is important to understand so you can see how your code is doing quickly and easily.
        If I update these tests so they all pass and run the tests again.
        You'll see we get four dots. Which is what you want to see because it
        indicates that all tests ran successfully and they all passed.
        As you write tests you can use this output to determine which ones are passing and
        failing and identify any errors in the tests themselves.
        To finish up let's delete all but the first one here. And then rename this file to test views.py
        If we leave it as tests.py Django will still find it and run our tests.
        But we can also separate our testing logic in order to keep it organized and easy to manage.
        As well as to make our tests more independent of one another.
        So we'll call this one test views. And this will be used as the name implies to test our views.
        Then I'll create another one called test models.
        And another one for testing forms.
        Over the next few videos, we'll complete these test files. And write tests for our entire application


# __TESTING FORMS__
    - Now that you've seen an example of how testing in Django works.
        Let's write some tests for our item form.

    - In test forms.py I'll begin by importing Testcase from django.test
        And our item form from .forms
        Now let's create a new class called TestItemForm.
        Which will inherit Testcase and contain all the tests for this form.

    - We'll begin with the simple test to make sure that the name field is required in order to create an item.
        In general, you'll want to name your tests so that when they fail you can easily see what the issue is.
        So I'll call this one test item name is required.
        I'll begin by instantiating a form and we'll deliberately instantiate it without a name
        to simulate a user who submitted the form without filling it out.
        This form should not be valid.
        So I'll use assert false to ensure that that's the case.
        When the form is invalid it should also send back a dictionary of fields on which
        there were errors and the Associated error messages
        Knowing this we can be even more specific by using assert in to assert
        whether or not there's a name key in the dictionary of form errors.
        Finally to really drive the point home.
        I'll use assert equal to check whether the error message on the name field is this field is required.
        Remember to include the period at the end here as the string will need to match exactly.
        Also just a note we're using the zero index here because the form will return a list of errors on each field.
        And this verifies that the first item in that list is our string telling us the field is required.
        As we're now testing that the form is not valid. The error occurred on the name
        field and the specific error message is what we expect.
        They should be no doubt that the name field is required after running this test.

    - let's write another one to ensure the done field is not required.
        It shouldn't be since it has a default value of false on the item model.
        In this case we'll create the form sending only a name.
        And then just test that the form is valid as it should be even without selecting a done status.

    - Finally let's assume that somewhere down the line another developer comes
        along and changes the item model.
        Adding a field to it that contains some sort of information we don't want to display on the form.
        If you remember we actually defined the fields to display explicitly in the inner metaclass on the item form.
        And the reason for that is otherwise the form will display all fields on the model
        including those we might not want the user to see.
        That said we should write a test to ensure that the only fields that are displayed in
        the form are the name and done fields.

    - I'll call this test. test_fields_are_explicit_in_form_metaclass
        For this test we can simply instantiate an empty form.
        And then use assert equal to check whether the form.meta.fields attribute
        is equal to a list with name and done in it.
        This will ensure that the fields are defined explicitly.
        And if someone changes the item model down the road our form won't
        accidentally display information we don't want it to.
        This will also protect against the fields being reordered. Since the list must match exactly.

With our three tests done let's run them and see how it fares.So we can see that all tests have passed. And in fact it's actually still running the one we created in the last video that lives in the test views.py file.
So this is a good place to explain. You can actually be more specific about what you're testing.
We could for example run only the form tests by using python3 manage.py tests todo.test_forms
Run a specific class of tests by adding that on or even run a specific individual test by adding on the name of the test itself. Like I'll do for the last test here. 
__python3 manage.py test todo.test_forms.TestItemForm.test_fields_are_explicit_in_form_metaclass__
You can see also if I go and change the fields defined in the metaclass on the form. This test will fail letting us know that something is wrong. With our form thoroughly tested. In the next video, we'll move on to testing our views.

# __Testing Views.py__
    - With our forms tested. let's test our views.
        The process here is going to be pretty straightforward.
        We want to test not only that our views return a successful HTTP response
        and that they're using the proper templates.
        But also what they can do. Specifically adding toggling and deleting items.
        Let's start by renaming the existing class in the test views type I file. To test views.
        Next just to show you the bigger picture. 
        
I'll write out the names of the six tests we're going to write. And then will complete them one by one.

    - First we'll want to test that we can get the todo list which is the home page.
        Then we'll want to test getting the add_item page.
        And then test getting the edit_item page.
        After that, we'll test that we can add an item.
        Then test that we can delete an item using the delete view.
        And finally we'll test we can toggle an item using the toggle view.
        To test the HTTP responses of the views.
        We can use a built-in HTTP client that comes with the Django testing framework.
        I'll start with the get_todo_list view.
        By setting a variable response equal to self.client.get
        And providing the URL slash since we just want to get the home page.
        We can then use assert equal to confirm that the response.status code is equal to 200
        A successful HTTP response.
        To confirm the view uses the correct template.
        I'll use self.assertTemplateUsed and tell it the template we expect it to use in the response.
        Let's comment out the rest of these temporarily and run this test using
        python3 manage.py test todo.test_views.
        That one passed. So moving on we can test getting the add_item page in the exact same way.
        The only things we have to change are the URL we're getting. And the template we expected to use.
        The Edit item page is a little different.
        I'll paste in the same code and change the template we're expecting.
        But, in this case, the URL will be edit followed by an item ID like 99 for example.
        If we just pass it a static number though. The test will only pass if that item ID exists in our database.
        And we want to be more generic than that.
        Conveniently in Django tests, we can also do crud operations.
        So let's import the item model at the top. And then create an item to use in this test.
        Now that we've got the item created.
        Testing that we can get the Edit URL.
        Is as simple as adding on its ID. Which I'll do with the Python f string.
        if you're not familiar with f strings.
        They work almost identically to the template literals you learned about in the JavaScript lessons.
        All we've got to do is add an f before the opening quotation mark.
        And then anything we put in curly brackets will be interpreted and turned into part of the string.
        The last three tests will evaluate whether we are able to create update and delete items.
        To test creating an item we can set the response equal to self.client.post on the add URL
        And give it a name the item as if we've just submitted the item form.
        If the item is added successfully. The view should redirect back to the home page.
        So I'll use assert redirects. To confirm that it redirects back to slash.
        Now let's test whether we can delete an item.
        First I'll create one using item.objects.create.
        And then I'll use the same syntax as we used on the edit_item view.
        To make a get request. To delete slash the items ID
        Again we'll want to assert that the view redirects us as that's what it should do if it's successful.
        And while we should technically already know the test passed at this point.
        Just to prove that the item is in fact deleted.
        I'll try to get it from the database using .filter and passing it the item ID
        Since that item is the only one on the database and we just deleted it.
        We can be certain the view works by asserting whether the length of existing items is zero.
        Finally let's test whether toggling items is working.
        The first three lines of this test will be almost the same.
        So I'll copy those from above.
        This time let's create an item with a done status of true. Then call the toggle URL on its ID.
        After asserting that the view redirects us. We can get the item again.
        And I'll call it updated item.
        And then use assert false to check it's done status.
        with that complete I'll run all the tests and verify that they all pass
        With nine tests passing. In the next video we'll write one final test.
        To test the item model.


# __Testing Models__
    - To finish up testing for our app. Let's write one more quick test for the models.
        In general, we don't want to test internal Django code because it's
        already been tested by the django developers themselves.
        But there is one thing we can test. Just to demonstrate the philosophy.
        And that's to test that our todo items will be created by default with the done
        status of false.
        I'll begin in test_models.py By as usual importing TestCase from django.test
        And we'll need to import our item model from .models
        Now I'll create a new class called TestModels which inherits TestCase.
        And inside it a method called test_done_defaults_to_false
        This test is extremely simple.
        All we need to do is create an item. Using item.objects.create
        And I'll call this item Test Todo Item.
        And then use assert false. To confirm that it's done status is in fact, false by default
        With that finished let's save the file and run just that test.
        That one passed. So we know now we should have 10 tests passing. And to confirm that I'll run them all
        With all our tests passing. In the next video we'll implement a tool called
        coverage to show what percentage of our code we've actually tested.

# __Coverage__
With all our tests written.It would be nice to know how much of our code we've actually tested.
We can do this with a useful tool called coverage. __Which I'll install now with pip3 install coverage.__
Once it's installed.

    - To run it is as simple as typing  "coverage run --source=todo manage.py test"
        Which will look at all the tests we've written for the todo app and generate a nice report.
        To view the report I'll use the command coverage report.
        You can see looking in the terminal now that we've covered almost all of our code.
        But we're missing a little bit in the views.py file. As well as in models.py
        To see specifically what we're missing. Coverage allows us to create an
        interactive HTML report. Using the command coverage html.
        Doing this we'll end up with a folder over here in our project called htmlcov
        And inside it there's an index.html file.
        To view this file in gitpod.
        We need to treat our application as a simple HTML web page.
        Since otherwise the Django application will end up looking for a URL that
        doesn't exist when we try to get the report.
        To view the page we can use the command python3 - m http.server
        I'll click on open browser. And then click the htmlcov folder.
        Which will automatically open to the index.html page.
        In here we see the interactive version of the report we just looked at in the terminal.
        If I click on models.py you'll see the reason we only have 83% coverage here
        is because we haven't tested the string method of our item model.
        This is really easy to do.
        In test models.py let's create a new test called test_item_string_method_returns_name
        I'll use item.objects.create
        To create an item with the name of Tests Todo Item.
        And then use self.assertEqual to confirm that this name is returned when we render this item as a string.
        Now we can rerun coverage. Regenerate the HTML report and check again.
        You might have to hard refresh to get the new numbers to show up.
        But once you do you should see there are models.py is now at 100% coverage.
        It's important to note here that 100% coverage does not mean 100% of our tests pass.
        Only that we have tested 100% of our code.
        You should still keep an eye on the results of running the tests. To make sure they're all passing.
        It looks like there's only one other thing we haven't tested here. And that's the post method of our edit view.
        Let's write that test now. And get to 100% test coverage at least for our own code.
        In test views.py. I'll write a new test called test_can_edit_item
        First I'll create a new item like we've done above in the toggle item test.
        Then let's grab the code above we use to test getting the edit view.
        Except this time instead of using self.client.get We'll use self.client.post
        And post an updated name.
        We'll then assert that the view redirected us.
        And get the updated item just like we did above in the toggle item test.
        And now finally we can test that the updated items name is equal to updated name using assertEqual
        One last time let's rerun coverage. Regenerate the HTML and check it out.
        We can see all the tests passed.
        And opening the HTML report will show us we're at 97% coverage now.
        And the only untested code that remains is code that is automatically generated by Django.
        For this reason, we're not going to test this code.
        In practice getting to 100% test coverage is unlikely.
        But in this case, we've tested all the critical aspects of our application.
        And that's what matters.
        In the upcoming series of videos, we'll deploy our application to Heroku.
        Putting it in the wild for the world to see

# __DEPLOYMENT__
# __Heroku Setup and CLI__
Update to heroku login command
Since this video was created, the login command for heroku has changed. When the instructor logs in to heroku from the terminal, please use the following command:

heroku login -i

    - To launch our project in the wild. We need to create an account at heroku
        Which is a cloud-based platform as a service.
        That allows us to host data-driven apps in isolated containers on their infrastructure.
        To get started. You'll need to go to heroku.com. And register for a free account.
        If asked you can set your role as hobbyist.
        And primary development language as python.
        Once you've signed up and verified your email.
        You'll find yourself on a dashboard which looks something like this.
        While everything on Heroku is manageable via this user interface.
        There is also a command-line interface that we can use in the terminal.
        This cli was installed by default. If you use the Code Institute gitpod template
        when you created this workspace.
        But if it's not installed for you.
        For containerized environments like gitpod. Heroku recommends installing it
        using the standalone install script in their documentation.
        If you need it because this has changed since the video was recorded
        you can easily find installation instructions with a quick google search
        on installing the Heroku cli. Or asking in the Code Institute slack chat.
        To use the cli we need to log into it.
        So assuming you've got it installed and ready to go.
        You can log in using the command heroku login.
        Doing so will tell us we can press any key to open a browser. And then we can log in.
        If you just type Heroku by the way.
        You'll see all the other commands you can use. In particular the help command.
        If you need to know how any of these other commands work.
        You can simply type Heroku followed by the command. And then the help command.
        For example to learn how the apps command works.
        i can type heroku apps help.
        As we work through these next few videos
        we'll use the Heroku cli. As well as the web ui. To navigate around Heroku.
        Setting up the infrastructure we need. To deploy our to-do app.
        And make it publicly accessible

# __Installing Project Requirements__
    - Before we actually deploy our project to Heroku.
        Let's set up some things it'll need in order to function out there in the wild.
        First of all, you might remember that the db.sqlite3 file in the file explorer.
        Has been acting as our database throughout these videos.
        This is fine for local development.
        But unfortunately, it won't work in production.
        Because Heroku uses an ephemeral file system.
        Which means it's wiped clean every time Heroku runs updates. Or we redeploy our app.
        Because sqlite is a file-based database.
        We'll lose our entire database every time this happens because when the file
        system is wiped the file will be deleted.
        In general, you never want to store anything valuable on an ephemeral file system.
        Because it isn't guaranteed to stick around.

Instead, we'll use an add-on for Heroku.
Which will allow us to use a server-based database called Postgres.
And that one will be separated from our application.
So it'll survive even if the application server is destroyed.

    - To use Postgres in our application. We need to install a package called psycopg2
        Which we can do with pip3 install psycopg2-binary
        Later on, we'll add the Heroku add-on to set it up.
        But this will take care of the Django side.

    - We'll also need a package called gunicorn. Or green unicorn.
        Which will replace our development server once the app is deployed to Heroku.
        Gunicorn will act as our web server.
        And we can install it using pip3 install gunicorn

    - With those two packages installed.
        I'm going to use a new command pip 3 freeze - - local
        And will direct it into a file called requirements .txt
        *************        "pip3 freeze --local > requirements.txt"         ************
        This requirements file is how Heroku will know what it needs to install for our app to work.
        Specifically, it'll tell Heroku all the packages it needs to install using pip.
        Just like we've done throughout our project.

# __Creating an Heroku App__
    - Now that we've got a requirements file and have installed everything our
        project will need to run on Heroku.
        We can actually create the Heroku app itself.
        Before you do this make sure you log in if you're not already.
        By using the Heroku login command.
        To create an app. i'll use the command Heroku apps colon create.
        ckz 8780 django todo app.
        You'll need to specify your own app name. But you can name it whatever you want.
        You can also specify a region using the --region flag
        By default, the app will be created in the us region.
        But if you're in the European union you can simply specify --region eu
        With the app created.
        You should now be able to see it in the list when you run the command Heroku apps.
        Let's take a look in the dashboard also.
        Clicking on the app. Brings us to the overview where we see any installed
        add-ons the type of dyno or container the app runs on. And any collaborator activity.
        On the deploy tab, you can configure how your app is deployed. And we'll get to that a bit later.
        There's also an activity tab which will keep a log of things like deploying new
        versions of the app.
        And a settings tab where we'll be able to configure different app information
        environment variables, ssl certificates, domains and other app settings.
        Heading back to the terminal.
        Going forward we're going to use a tool called git. To manage different versions of our app.
        And handle deploying it to Heroku.
        Git is a version control system. That'll allow us to track changes to our code over time
        Similar to being able to save your progress in a video game.
        When we create a Heroku app.
        It automatically sets up a git repository for us that we can push our code changes to.
        And this is how we'll deploy our project.
        If you type git remote -v for verbose.
        You'll see that there are two key remote urls here.
        One for pushing code to Heroku. And one for fetching code from Heroku.
        This tells us that when we use the command git push heroku master
        It will be pushed to the master branch at this url.
        If we use the command git push origin master. It would go to the other remote url
        If this doesn't make complete sense yet don't worry.
        Because we're going to go through this in detail when we deploy the app.
        For now, just remember that git is the tool we're going to use to push our code to Heroku.
        And that this remote is the url it'll be pushed to.
        In the next video, we'll set up our Heroku database.
        Using an add-on for the app we just created.









































