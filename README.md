

[View the live project here.](http://tastemyfood.herokuapp.com/get_recetas)

This is the 3rd Milesone.
Free RecipeBook where users can save and share recipes. It has been designed so it can be responsive for a range of devices.

<h2 align="center"><img src="https://github.com/andna5980/myfood/blob/main/assets/images/Tastemyfood-mockup.png"></h2>


## User Experience (UX)

### User stories

    1. As a first-time visitor, I want to quickly understand the main purpose of the website and how I can benefit from the service provided.

    2. As a first-time visitor I want to navigate the page in a ease and clear way.
    
    3. As a firt-time visitor I want to get access to content without the need of register os join the service. 

    4. As a first-time visitor I want to find on the site all the social media links, so I can check if the site is trustworthy. Also, I would like see the real            testimonials that help me understand the benefits of the product.

    5. As a returning visitor, I would like to be able to filter recipes so i can see only what i am interested in.
    
    5. As a retuning visitor I would like to see new content that can inspire me to create my own recipes 
    
    6. As a returning visitor, I would like to be able to create and save my own recipes 
    
    7. As a frequent user I want to be able to see new recipes from different users.
    
    8. As a frequent user I would like to be able to delete or edit any of my recipes if I want.  
    
    
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

- 











