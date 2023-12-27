# myRecipe

Link to live myRecipe project: [myRecipe - CI Project Four - Full Stack Frameworks](https://ci-myrecipe-921534e8b4ab.herokuapp.com/)

## Table of Contents 
1. The Project
    - Project Goals
    - Initial Design
    - Manual Testing
2. Features
    - Implemented
    - Future Development
3. Technology used
4. Testing
    - Manuel
5. Bugs
6. Project Deployment
7. Sources
    - Code
    - Colors
    - Images


## The Project


### Project Goals

With the ever growing need to find a simple recipe to cook for you and your family. The idea of myRecipe was created with the intention of creating an application where you can create and view your own or others recipes. With the intention of future development to build tools to allow chefs and restaurants the same ability and have everything in one place.

### Initial Design (Wireframes)

During the initial design phase of the project, wire frames were created to give a visual design idea and an end goal to work towards. With thought and care taken to make the design of the application as responsive and user friendly as possible for all device types. 
Whilst the wire frames may not be accurate to the device screen size. The designs has been adjusted to work and function correctly on all device types.

<details>
<summary>Page Designs</summary>
<br>

### Home Page

<img alt="Home Page" height="350px" src="./static/media/home.png">

###  Pricing and Contact page

<img alt="Pricing and Contact Page" height="350px" src="./static/media/pricing-contact.png">

### User Login and User Home Page

<img alt="User login and user home page" height="350px" src="./static/media/login-userhome.png">

### User registration and payment wall

<img alt="User registration and payment" height="350px" src="./static/media/signup-payment.png">

### User Logout and User Account Page

<img alt="User logout and user account" height="350px" src="./static/media/logout-account.png">

### Recipe and CRUD Pages

<img alt="Recipe and CRUD Pages" height="350px" src="./static/media/recipe-crud.png">

### Database Design 

<img alt="Recipe database design" height="350px" src="./static/media/databasedesign.png">

</details>

<details>
<summary>Features</summary>
<br>

### Implemented

The basic features that are currently implemented into the application are

- User contact form 
- User registration and authentication
- User recipe creation
- User recipe edit/delete
- Recipe browsing 

### Future Development

Future features that are in development are

- Restaurant Recipe creation 
- Allergen and calorie counting
- Menu Creation
- Recipe/Menu Costing 
- User Support Chats
- Instant Messages between users
- User Profiles
- Dark Mode
- Restaurant Stock Take
- Shopping lists
- Order Reports (Based of menu created by chefs)

</details>

## Technology Used

During the development of the app multiple different types of technology was used and utilized to build the final application. 

- HTML - Was used to create the basic web page for the project
- CSS - Was used to style the web page and the different elements that make up the application
- JS - Was used to create a few simple functions for ease of use. Such as changing the date in the footer and sending emails on the contact form
- Python - Used during the development of the back end of the application for everything that communicates with different servers and databases
- Django - Was used as the base development framework. Allowing the use of template and and back end driven development. 
- MDN - A bootstrap library. Allowing the use of different components and defined classes throughout the application to speed up development. (Upon review, I would choose to use the base Bootstrap library.)
- Cloudinary - Used for the hosting of the images that are uploaded to the application for the recipes
- ElephantSQL - Was used for the hosting of the database that contains all the recipes on the application
- Github - Was used for source control of the project allowing progress of the application to be tracked and stored in one place
- Gitpod - Was used as an IDE. Allowing for the development of the application anywhere anytime
- Heroku - Was used to host the application on the internet for all to use and see

## App Testing

During the development of the Project it has been subjected to different testing methods to ensure that all points are hit. No errors are found in the code as well as manual testing of the app to ensure everything works as intended. There was also testing involved to ensure that the application would be responsive and work on all screen sizes and device types. To allow for the best accessability possible. The image for this can be found at the top of the document.


| Test | Intended Result | Result |
|------|-----------------|--------|
| Navigation | All pages are correctly linked together with the correct navigation | Passed |
| User Registration | Users can register to the application to create an account | Passed |
| User Logout | User can successfully logout of their account | Passed |
| User Login | User can successfully login into their account | Passed |
| Contact Form | Users(registered and not) can submit the contact form to the admins. Showing a success message on successful submission | passed|
| Contact form Clear and Message | Contact form clears itself on submission and a success message is displayed back to the user | Passed |
| Access restricted | Users who are not logged into their account cannot access certain information | Passed |
| View Recipes | User can view all recipes posted to the application | Passed |
| View Own Recipes | User can see all of their own recipes they have posted in one single place | Passed |
| Edit Recipe | User can edit any of their own recipes. With the updates being displayed and posted to the database immediately | Passed |
| Delete Recipe | User can delete any of their own recipes. With a warning page being displayed. Any action taking immediate effect | Passed |

## Bugs

During the development of the application there were many different bugs along the way. From a simple syntax error to an application breaking bug. Some of them are in the table below.


| Bug | Fix |
|-----|-----|
| Summernote displaying html code syntax on the page when rendering the recipe | Fixed by adding the 'safe' argument onto the template |
| Footer styling issue on the user login page | Fixed by removing extra closing 'div' tags causing the issue |
| Recipe creation form not submitting recipe | Fixed by converting the form from html to native django and python, by using the forms module |
| No reverse match for home page | Fixed by removing the .slug prefix on the page navigation once removing the slug from the model |
| Multiple pages receiving multiple arguments when one is required | Fixed by adding 'as_view()' to the urls when the views were converted |
| Users image not uploading to the application when submitting the 'Create a Recipe form' | Fixed by adding the 'enctype' to the form element |


## Project Deployment

Heroku was used to deploy the application live to the internet. The live Application can be found [Here](https://ci-myrecipe-921534e8b4ab.herokuapp.com/)

If you are wanting to take a look at the code and potentially add on your own features to the project you can do so by cloning or forking the repo. By doing this it will allow you to locally develop and add your own features to the app.

<details>
<summary>Clone</summary>
<br>

By clicking the clone repo button. You are able to then clone the repo as it is. By clicking the fork button you are able to take the code and add it to your own account where you can develop and push new and improved features to the main application. 

<img alt="Clone the repo" height="300px" src="./static/media/fork-clonerepo.png">

</details>

## Sources

### Code

All code for the project was written by myself. Whilst using Stack Overflow, Google, various Youtube videos and Code Institute Slack Chats for reference and problem solving. Also being aware of the Code Institutes 'Botique Ado' Walkthrough for code reference and guidance along the way

Also using various code samples Bootstrap library of free sample code

### Colors 

The colors that were chosen for the project were picked because they were all simple yet bold colors. All contrasting each other allowing for an easy to read/view application. 

<details>
<summary>Color Palette</summary>

<img alt="Color Palette for the application" height="300px" src="">

</details>



### Images

All images that are found in the application on all pages are from a selection of websites. That are listed below.

- Pexels - Royalty Free Images
- FedFedFed - Online food retailer
- Google Image Search
- The Fruit and Veg Man
- Meatless Farms
- Blackwells Butchers
- The Cornish Fish Monger

### Favicon 

Favicon was generated using favicon.io

