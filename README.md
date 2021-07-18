<h1 align="center">Salt and Pepper<a name="#top"></a></h1>
<h1 align="center"><img src="static/img/readme-images/mockups/home.png"/></h1>


## About
Salt and Pepper is the website for anyone who believes that good food brings us together, no matter where are you (they) live.

KEEP COOKING DAILY - these recipes show you how to make a delicious meal or incredible drinks easyly in your home.

Salt and Pepper is a website for all food lovers who love to eat, try different flavour and create magnificent recipes!


I created this for **Milestone Project 3 (Python and Data-Centric Development), Full Stack Software Development** in [Code Institute](https://codeinstitute.net/), Ireland.
It is fully responsive on all devices and easy to navigate for users.
The link to the website is available [HERE](http://salt-and-pepper-project.herokuapp.com/home/).

<div align="right"><a href="#top">🔝</a></div>

## Table of Contents

[User Experience](#ux)

[Design](#design)

[Features](#features)

[Technologies](#technologies)

[Testing](#testing)

[Deployment](#deployment)


<div align="right"><a href="#top">🔝</a></div>
<a name="ux"></a>

## User Experience (UX)

### User Stories
Salt and Pepper gives the information about different recipe with cooking method, cooking-time, ingredients-list posted by users.
Salt and Pepper provides to create your own account and post recipe.
- #### Generic User
    1. I want to easily understand the purpose and the layout of the site without additional instructions needed.
    1. I want to easily navigate through the site to browse the content.
    1. I want the site is responsive on all device.
    1. I want to use the navigation at all times so I can quickly navigate from one page to another.

- ####  Admin/Owner
    1. As a Admin/Owner I want to read all the recipe.
    1. As a Admin/Owner I want to add, edit and delete my recipe.
    1. As a Admin/Owner I can delete others recipe from my site.
    1. As a Admin/Owner I want manage categories of recipes.I want to add, edit and delete the category.

- #### User who wants to get recipe
    1. I want to check all the recipe without login or sign up on site.
    1. I want to get recipe by search option.

- #### User who wants to post recipe
    1. I want to create my profile by sign up.
    1. I want to easliy login and check my page.
    1. I want to add new recipe on my page and available to all users of site.
    1. I want to edit and delete my recipe only.

<div align="right"><a href="#top">🔝</a></div>    
<a name="design"></a>

## Design
### Colour 
* The main colors which is used for the website can be find [HERE](https://colorhunt.co/palette/111d5ec70039f37121c0e218).
    
    <img src="static/img/readme-images/01.png" height="40px"/>
    
    The grey, and white color is used for text-color and background-color.

     <img src="static/img/readme-images/3d454d.svg" height="40px"/>
     <img src="static/img/readme-images/ffffff.svg" height="40px"/>

### Typography

* The font used is a Alegreya Sans SC with sans-serif as a fallback font.
* The logo font used is a Pattaya for brand name and Alegreya Sans SC for brand slogen.

### Icons

* The icons have functional purposes such as the hamburger menu and social media icons and provided by [Font Awesome](https://fontawesome.com/). 


### Defensive Design

* The user is not able to break the site by clicking on buttons.
* The add and edit recipe form:
    - The category has to be chosen.
    - The Difficulty Level has to be chosen.
    - The image URL must start with https://.
* Recipes or categories can't be deleted by just one click. 
    - If someone clicks on the delete button, there will be a modal with a confirmation
        if someone is sure to delete the recipe or category.

### Mockups

- #### Mockup made through original website 
    -[Wireframes](https://techsini.com/multi-mockup/index.php)

    img src="static/img/readme-images/mockups/home.png"/>
    img src="static/img/readme-images/mockups/recipes.png"/>
    img src="static/img/readme-images/mockups/signin.png"/>
    img src="static/img/readme-images/mockups/sindup.png"/>
    img src="static/img/readme-images/mockups/404.png"/>
    img src="static/img/readme-images/mockups/403.png"/>


    
    
<div align="right"><a href="#top">🔝</a></div>
<a name="#features"></a>

## Features
### Existing Features
* On each page header allows user to easily navigate across all pages
  - The header is positioned to always be visible (positioned absolutely using Bootstrap 'fixed-top' class) at the top of the screen (mobile and desktop) which allows visitors to find it quickly.
  - The brand logo is positioned on the left and is visible on all pages and by clicking the logo returns users to the home page.
  - Navigation links is more visible when hovered over. This lets the visitor know that it is clickable.
  - Navigation links collapse when viewed on mobile device.
* Flash messages
  - Messages displayed at the top of the page to provide the user confirmation of actions like sing-in, adding or editing recipe etc.
* Responsiveness
  - All Pages are responsive on different viewport size.
* Footer
  - There are social links and when hovered over, it changed the color.
  - There is a Business copyright information.

**Home page Features**
  - This page has header, footer and search box. 
On the page three subcategory, each subcategory has a clickable links that takes the user the selected category page.
Eeach subcategory has three recipe cards with recipe name, short description, difficulty level, who is the chef, the posted date and the recipe image.
Each cards is clickable and takes the user to the selected recipe page.
If the card has no recipe image custom image will appear.
The header has navigation bar and footer has copyright and social links.
The image brings the user's attention and inviting the user to explore the website.

**Recipes page Features**
  - This page has header, footer and search box.
This page has list of all recipes with recipe name, short description, difficulty level, who is the chef, the posted date and the recipe image.
Each cards is clickable and takes the user to the selected recipe page.
The user can change the category by clicking the navbar recipes dropdown menu and choose the different category
The image brings the user's attention and inviting the user to explore the website.

**Profile page Features**
  - This page contains all of the user recipes.
This page has header, footer.
There is an Add recipe button that takes the user to the new recipe page where user can add new recipes.
There is an Edit and Delete button by clicking on it user can edit or delete there own recipes.

**New recipes page Features**
  - This page contains a recipe form for the user to fill out and upon submission will go into the database and show on the users profile page.
At the bottom of the form there are the add recipe and Cancel buttons. 

**Manage Category page Features**
  - Only admin can access this page. In this page admin can manage categories
Add, Edit and Delete categories.

**Recipes Description page Features**
  - This page displays recipe description of selected recipe.

**Sign-In Modal Features**
  - This modal has login form. After login user will reach on his page.

**Sing-Up Modal Features**
  - This modal has sign up form. After sign up a profile page created where users can add recipe.

### Features Left To Implement
* Resetting Password When Users Forget It

* Upload Image For Each Recipe:
  - Image data cannot be stored in MongoDB so this is not possible with the current project however, having image for recipes is achieved by using image URL

* Review By Other Users:
  - A page where people can leave review and comments.

* “Like” or "Rate" By Other Users/Owners:
  - Create a way for the user to rate and like the recipes without having to type up feedback.


<div align="right"><a href="#top">🔝</a></div>

<a name="#technologies"></a>

## Technologies Used
- [HTML5](https://en.wikipedia.org/wiki/HTML) for markup
- [CSS3](https://en.wikipedia.org/wiki/CSS) for style
- [Bootstrap 4.6](https://getbootstrap.com/) for the mainframe of the website
- [Python3](https://www.python.org/) as a backend programming language
- [Flask](https://flask.palletsprojects.com/) &#40;a micro web framework written in Python&#41; as the main framework of Python
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/) as database
- [Google Fonts](https://fonts.google.com/) for fonts
- [Font Awesome](https://fontawesome.com/) for icons
- [Gitpod](https://www.gitpod.io/) as Integrated Development Environment &#40;IDE&#41;
- [Git](https://git-scm.com/) for local version control, keeping the files & documents
- [GitHub](https://github.com/) for online version control and keeping the files & documents
- [Heroku](https://www.heroku.com/) for deploying the website

<div align="right"><a href="#top">🔝</a></div>

<a name="#testing"></a>

## Testing
* Testing report is available **[TESTING.md]()**

<div align="right"><a href="#top">🔝</a></div>

<a name="#deployment"></a>
## Deployment

<div align="right"><a href="#top">🔝</a></div>

## Credits
#### Code
* Bootstrap library was used to create a responsive design.
#### Content
* The recipes and the Image URL-s of the page was copied from [Jamie Oliver](https://www.jamieoliver.com/)
#### Media
###### No recipe Image
* The [No Recipe Image](https://norecipes.com/karaage-recipe/) was used from this website.
###### Carousel and Header Images  
* The carousel and header images found on [UNSPLASH.com](https://unsplash.com/)
###### Icons
* The Icons used from [Font Awesome](https://fontawesome.com/)
###### Favicon
* The [emoji graphics](https://github.com/twitter/twemoji/blob/master/assets/svg/1f374.svg) are from the open source project [Twemoji](https://twemoji.twitter.com/). The graphics are copyright 2020 Twitter, Inc and other contributors. The graphics are licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).
###### Fonts
The project used [Google fonts](https://fonts.google.com/)


#### Acknowledgements
* Many Thanks to my mentor Akshat Garg who was brilliant and helping me throughout the project and giving me important suggestions and feedback of my work.
* Thanks to my fellow student and tutors on slack channel who helped me in some way.


#### Disclaimer
This project was made as my 3st. Milestone Project in [Code Institute](https://codeinstitute.net/5-day-coding-challenge/?utm_term=%2Bcode%20%2Binstitute&utm_campaign=a%26c_BR_IRL_Code_Institute&utm_source=adwords&utm_medium=ppc&hsa_net=adwords&hsa_tgt=kwd-319867642491&hsa_ad=326751276603&hsa_acc=8983321581&hsa_grp=56427889178&hsa_mt=b&hsa_cam=1378516521&hsa_kw=%2Bcode%20%2Binstitute&hsa_ver=3&hsa_src=g&gclid=EAIaIQobChMIiJjgxOrD7QIVz8LtCh3OQQgLEAAYASAAEgLd4vD_BwE&gclsrc=aw.ds)
<div align="right"><a href="#top">🔝</a></div>

