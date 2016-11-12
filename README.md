Life Hacks
-----------
Life Hacks is a project for a community to create and receive life hacks based on location, personal profile, and more. The application will have three basic functions, as indicated below:
1. Publish and rate "life hacks," or concise, clever descriptions of how to accomplish daily tasks.
2. Create and manage user profiles.
3. Recommend life hacks to users based on different matching procedures.
<b>Project procedure:</b> Go through the TODO list in each commit and tackle (usually only one) item on the list (or sublists) at a time. Once you have performed a task, delete it from the TODO. PLEASE use descriptive commits. <code>git commit -m "descriptive-text-here"</code> exists for a reason. See resources below for other important info.

TODO
------------
- basically everything lmao
- create website structure
  - home page
  - login page
  - user profile page
  - life hack creation page
- create style
  - install all necessary frameworks
  - create color scheme
  - define global and local variables for reuse
- create static files for each application

Resources
-----------
Here are some important links for brushing up on or referencing different technologies.
- <a href = "http://rogerdudler.github.io/git-guide/">Basic Git</a>
- <a href = "http://gitref.org">More Complete Git Reference</a>
- <a href = "https://docs.djangoproject.com/en/1.10/">Django</a>
- <a href = "https://docs.djangoproject.com/en/1.10/">Bootstrap</a>
- <a href = "https://docs.djangoproject.com/en/1.7/topics/templates/">DTL</a>
- <a href = "http://lesscss.org">LESS</a> (CSS Extension)
- <a href= "http://api.jquery.com">JQuery</a>
- <a href = "http://www.w3schools.com">General Web Development</a> (you can learn pretty much anything client side here)

Structure
-----------
The main application is within the folder "main". Here, you should find another folder named main. this is the location of the code of the main application. In the root directory, there are two other apps, hack and login, which are the hack creation and login applications, respectively. Within the folder for each app, there is a templates folder. This is where all the static files go.
