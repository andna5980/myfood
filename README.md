

[View the live project here.](http://tastemyfood.herokuapp.com/get_recetas)

This is the 3rd Milesone.
Free RecipeBook where users can save and share recipes. It has been designed so it can be responsive for a range of devices.

<h2 align="center"><img src="https://github.com/andna5980/myfood/blob/main/assets/images/Tastemyfood-mockup.png"></h2>


## User Experience (UX)

### User stories

1. As a first-time visitor, I want to quickly understand the main purpose of the website and how I can benefit 
    from the service provided.

2. As a first-time visitor I want to navigate the page in a ease and clear way.
    
3. As a firt-time visitor I want to get access to content without the need of register os join the service. 

4. As a first-time visitor I want to find on the site all the social media links, so I can check if the site is 
    trustworthy. Also, I would like see the real testimonials that help me understand the benefits of the product.

5. As a returning visitor, I would like to be able to filter recipes so i can see only what i am interested in.
    
6. As a retuning visitor I would like to see new content that can inspire me to create my own recipes 
    
7. As a returning visitor, I would like to be able to create and save my own recipes 
    
8. As a frequent user I want to be able to see new recipes from different users.
    
9. As a frequent user I would like to be able to delete or edit any of my recipes if I want.  
    
    
## Structure

The website will contain 3 pages for users that are not members.

- Home Page will explain the puropose and the page and also the list of recipes created by the users.

- A log in Page for registered users.

- A Register Page for users to registered.

The website will contain 4 pages for users that are registered and are logged.

- Home Page will explain the puropose and the page and also the list of recipes created by the users.

- A Profile Page that will confirm the user name of the current user.

- A New Recipe Page will allow users to create and save recipes for later access.

- A log Out Page will let the users logout if they want.


## Database

### Database Schema:

This project used a non-rational database by using MongoDB. 

One main database (RecipesBook)


3 Collections
    UserId: this collection will store the documents of the accounts created with the keys. username and password 
    foodTypes: this collection contains the foodtypes created by the Admin. 
    recetas: Will contain 4 documents. 
        1) foodType_name(string) will contain the foodtype of the recipe.  
        2) receta_name(string) will contain the name of the recipes.
        3) cooking_instructions(string) will contain, ingredients and cooking instructions.
        4) created_by(string) will contain the username that created the recipe.

## Data Model

Website User's journey
<h2 align="center"><img src="https://github.com/andna5980/myfood/blob/main/assets/wireframes/data-model.png"></h2>

## Features

### Navbar:

Navigation bar will include a background image food related, home page which include the purpose of the website and will display a list of the recipes created by the users. Log in page will   

### Footer:

It contains all the social media so the user can visit all related channels

### Log in:

Page for already registered users, they can access by providing username and password. Once this authentication procces is validated users can create or modify their own recipes.

### Register:

Page where users can create an account, they only have to provide a username(not already exist) and a password.

### Profile:

Page that confirm the user is under their account.

### New Recipe:

Page where users that are logged can create, save and edit their recipes.

### Logout:

Functionality in the navbar that will allow the logged users to logout/exit the web 

## Future Features Improvements

- User options to upload images for the recipes saved

- User options to provide and save more personal details.

- Options for users to interact with other users.

- Options for users to contribute/comment other recipes


## Color Scheme and Typography

- The color scheme use is called organic color Palette, basically a mix of greens which represent a plant-base fare. 
  This color palette matches the food topic, this colours are mainly used in restaurants and food oriented pages.

- Typography throughout the whole page is BlinkMacSystemFont which is a Apple font. Is a simplistic font, easy to read in various devices.

## Technologies
### Languages and Frameworks

- HTML5 - Mark-ip language mainly used for the web structure
- CSS3 - Used to provide style the web
- JavaScript - Language use to create web functionalities 
- Python - Backend language to develop everything not seen by the user
- Flask - Framework
- jQuery - JavaScript library needed for Materialize framework to work  
- Github - Online service to host repositories.

### FrontEnd

- Materialize - Framwork use for the creation of different areas of the web
- FontAwsome - Vector icons used in the website
- Balsamic - Used to created wireframes

### BackEnd

- MongoDB - Database used to store user's details and all recipes added by them
- Heroku - Platform used to deploy and Host the website

## Testing

### Screen Viewport

The website has been tested in different view ports using Google Inspect tools. The website and it functions is clearly displany without any problem in varios 
screen sizes. Starting from 400px to 1620px. 

### Operation System & Browsers

The website has been tested in different OS, that includes iOS, Windows but also in the 3 main browsers Chrome, Safari and firefox. 
The results for those tests were positive.

See also Lighthouse Performance test resuls
<h2 align="center"><img src="https://github.com/andna5980/myfood/blob/main/assets/images/Lighthouse%20performance%20test.png"></h2>


## Code Validation

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) Showed no errors or faults.

- [JS validator](https://jshint.com) JavaScript validator detected no erros.

- [PEP8 Online](http://pep8online.com) Python code validator. Showed no main issues with the code.

## Solved Bugs

- Search, edit and delete buttons overlap under mobile views. I had to modify the size of the buttons and also insert border-radius in order to soft the corners.
  Buttons fit perfectly.

- Footer social media icons and copyright information did not hsowed completely under profile page. In Order to solve this issue I have to increase the height of     the footer itself from 80px to auto. By doing this the footer section used any space needed. 

- Navbar headings were to white and therefore not very clear to read with the background image. So I included an style line for every ul so it will create a shadow   and a stronger border in the text. This helped to read clear. 
  See below the code line that fixed the issue.
  style="text-shadow: 1px 1px 2px black, 0 0 25px black, 0 0 5px darkblue;
  
## Deployment

### Config
It is important to config the python file, which in my project is run.py. Part of the configuration is to import local enviroments saved on env.py

After all the "imports os" are done should follow ...

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


But also .....

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)

See above how debug=True; this always need to be set True during the development stages, but then change to False once the project is finish.

Requirements.txt also need to be included as there the list of all instances needed in order to run the project. In order to create the requirements file, it can be done typing in the terminal "pip3 install -r requirements.txt"
The file can be updated anytime a new instance is installed by typing in the terminal "pip3 freeze --local > requirements.txt"


Another file that also need to added is a Procfile. Inside this file needs to be included the following line
    web: python run.py

### Local Environment

Create a new file named env.py by typing in the terminal 'touch env.py'.  This will create a file where all the configurations should be listed. 
See below my configuration without the actual real information.

import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "PASSWORD")
os.environ.setdefault("MONGO_URI", "mongodb+srv://<user>:<password>@<projectname>.kfnli.mongodb.net/<database>retryWrites=true&w=majority")
os.environ.setdefault("MONGO_DBNAME", "<database name>")

 ### Heroku Deployment
    
Requirements needed
- MongoDB Account
- Heroku Account
   
Deployment Process
- Create Heroku Account
- Once in the Heroku Acc, Choose to create a new App
- Select Europe Region, as I am based in Europe
- Select to deploy using Github method
- Choose the repository (repository name) you want to deploy 
- Go to settings and select 'Config vars'
- 'config vars' details should be the same that appears in env.py file
- Before deployment, double check that 'requirements.txt' and 'Procfile' files are in place, otherwise deployment will incur in errors
- Go to Deploy tab / manual deployment, choose your branch and click in manual deployment, once deployment is succesfull you will be able to see the                 application
    

## Credits

### Code and Content 
- [Materialize framework](https://materializecss.com/)  Frontend development
- [Stackoverflow](https://stackoverflow.com/) General queries on code.
- [Colorspace](https://mycolor.space/) Color Palette website that generates a selecion of matching colors.  
- [W3schools](https://www.w3schools.com/) For general database on software development.

### Media

- [Fontawsome](https://fontawesome.com/)Vector Icons used in the whole project.
- [Undraw](https://undraw.co/search) Illustrations used in landing page and profile page
- [Background Image - Navbar](https://www.naturalproductsinsider.com/sites/naturalproductsinsider.com/files/Functional%20fats%20as%20functional%20ingredients.jpg)
    This image in part of the background used in the navbar

### Acknowledgements

- Code Institute Community, Student care and [Slack](https://slack.com/intl/en-gb/) group. 

- The private WhatsApp group created by Code institute Students for all the support and support during the hard moments you keep the motivation levels up.

- Code Institute Task Manager mini Project. The project you provided and the explanation really help me to used that project as an example of what could be done.

- My Wife for her support and companion during my long study nights.

- Juan Antonio Santana Medina for his help, support. 


