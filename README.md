# Localitty

Link to live Localitty project: [Localitty - CI Project Five - Eccommerce Specialization](https://ci-localitty-e5ac9cc8af68.herokuapp.com/)

## Table of Contents 
1. The Project
    - Project Goals
    - Initial Design
2. M.V.P
3. Features
    - The Plan
    - Implemented
    - Future Development
    - Security Features
4. Business Plan
    - The plan
    - Media Page
5. Technology used
6. Testing
    - Manual
7. Bugs
8. Project Deployment
9. Sources
    - Code
    - Colors
    - Images


## The Project


### Project Goals

With the ever growing problems that arise in day to day life, people are turning towards wanting a fresh and local supplier for food. Instead of using the large chain supermarkets. Meaning people are becoming more conscious of how there food is grown and where it comes from. This opens the market for local suppliers.

But there has been no platforms for them to sell on, unless its at there store in person. This has inspired a centralized store for all things local. With local suppliers coming together to sell there goods. Localitty was born to fill this gap. 

Allowing users of the store to know that the goods they are purchasing are local to them, helping them to support local and eat fresh produce. 

With region expansion planned and product expansion planned. Localittys aim is to incorporate into every day life to supply local products to local people.

### Initial Design (Wireframes)

During the initial design phase of the project, wire frames were created to give a visual design idea and an end goal to work towards. With thought and care taken to make the design of the application as responsive and user friendly as possible for all device types. 
Whilst the wire frames may not be accurate to the final deployed project. The application has been adjusted to work and function correctly on all device types. The wireframes were designed to give a core design to the store.

<details>
<summary>Page Designs</summary>
<br>

### Home, Shop and User dashboard

The design was intended to be simple and intuitive for the user. To allow them to use the store as intended. Keeping it clean and simple at the same time as giving the user all the information they would need on that page.

<img alt="Home Page, Shop Page and User Dashboard" height="250px" width="400px" src="static/media/readme/home-shop-user.png">

###  Support, Dont GnocchIt and Admin Dashboard

<img alt="Support Page, Dont Gnocchit and Admin Dashboard" height="250px" width="400px" src="static/media/readme/support-dontgnocchit-admin.png">

Despite there being other pages on the application that are not included in the initial wireframe design. They all followed the core theme of the application and store. This allowed less going back and forth designing new pages in wireframe's, meaning the development of certain features and pages could commence straight away.

</details>
<br>
<details>
<summary>Database Diagram</summary>
<br>
With the design of the database being a crucial part of the applications core design it was important to get it right. 

Although not all designs are implemented into the live application this is leaving room for future development such as the implementation of 'user product rating and comments' and 'individual supplier stores' to allow them to manage their own products and sell on the platform.

<img alt="Localitty database design" height="250px" width="400px" src="static/media/readme/locality-database.png">

</details>

## M.V.P - Minium Viable Product for launch

Having a basic plan of a minium product that is able to be launched and used as intended is one of the best places to start. As this enables the developer to start the programming side of the product, with a direction to follow and targets to hit as the project grows.

1. Basic Website 
    - Basic responsive landing pages
    - Clear intent of the product
    - Visually Appealing design
2. Product Pages
    - Main store page showing the entire range
    - Product search and filtering options
    - Product detail pages ( Image, Description, Price )
    - Add to cart
    - Quantity Selection buttons
3. Shopping Cart 
    - View items in cart
    - Update quantity/Remove from cart
    - Proceed to checkout
4. User Authentication
    - Allow the user to create a secure account
    - Allow guest users to checkout securely without creating an account. But give the option at checkout
5. Checkout 
    - Input shipping details
    - Input Billing details 
    - Order summary and order confirmation 
    - Secure checkout. Using products such as stripe
6. Order History
    - Show the users order history
7. Notifications
    - Show confirmation messages to the user
        - Added item to cart
        - Updated quantity/cart
        - Order confirmation
        - Contact form submitted successfully 
    - Email notifications
        - Order confirmation
        - Account managment options
        - Support form confirmation
8. Support
    - Support forms/support chats 
9. Security 
    - Add SSL Certificates
    - Secure encryption of passwords and billing information
    - Ensure all users data is securely stored in a protected database
10. User Feedback 
    - Give feedback on the products
    - Give feedback on the store itself
    - Report any bugs to the site admins

## Features

### The Plan

Having a plan determined by the M.V.P results in a developer building out a task list. Of features that are essential to the store and others that are not. But will be added at a later stage in the products development cycle.

By using Agile development methods I created a Kanban bored using githubs projects features. This allowed me to keep track of the project as a whole, Features I was working on and any bugs that had arisen that I wasn't able to fix right away.

<details>
<summary>Kanban Board</summary>
<br>
<img alt="Kanban bored of the project" height="300px" src="static/media/readme/kanban.png">
</details>
<br>
<details>
<summary>Bug Reports</summary>
<br>
<img alt="Bug reports on the project" height="300px" src="static/media/readme/bugs.png">
</details>

### Implemented

The basic features that are currently implemented into the application are

<details>

- User Contact form
- User account creation
- User store functionality(add items to bag, checkout securely, receive order confirmation email)
- User to save information to their account
- User to see previous order history
- User to sign up for mailing list
- Job Postings
- Job Applications
- Job CRUD (Create, Update, Delete)

- Admin CRUD (create, update and delete products)
- Admin Full Order history
- Admin total revenue, products and order count

</details>

### Future Development

Future features that are in development are

<details>

- Dark Mode
- Recipe/Developer Blogs
- Order History Filtering
- Vendor Accounts
- User product reviews and ratings
- Custom delivery schedule 
- Order dispatch emails
- Live Support Chats and messaging
- Locality Mobile App
- Job Applicants Status Updates
- Full Job postings page

</details>

### Security

With an online store security is one of the highest priority beside the functions of the store itself.
This is to protect the users, protect the store and all its data.

<details>
<summary>Security Features</summary>

- Django All Auth( Used for Django account creation and security )
- ElephantSQL ( Used to store all the data from the store, users, orders, products )
- Heroku ( Secure online website hosting  Through the use of Config vars to connect to outside sources )
- CSRF Tokens provided by django ( Allow the secure movement of data between the user and the backend of the application )

</details>

## Business Plan

Locality's ultimate goal is to connect local farmers and producers of goods to the local people in a certain area. Allowing for the sustainable production of goods.

Promoting sustainable living, supporting locals and to have the best produce available to the customer. Locality's vision is to become the go to online retailer for local farmers/growers/producers to sell there goods to the local people.

As a company it is a priority for us to be a sustainable and environmentally friendly as possible. Due to the nature of making deliveries and using certain packaging. This has become a high priority for us. We can achieve this by:

- Packaging: Use eco-friendly packaging materials and encourage customers to recycle.
- Reducing Food Waste: Implement strategies to minimize food waste, such as donation programs and responsible inventory management.
- Deliveries: By using electric vans/Hybrid vans to make our deliveries

### Target Market:

- Locals in the Essex area who value fresh, locally sourced products.
- Health-conscious consumers seeking organic and sustainably produced goods.
- Busy individuals who prefer the convenience of online shopping without compromising product quality.

### Products and Services:

- Offer a wide and diverse variety of produce for locals
- Eventually offer subscription boxes and curated bundles to cater to specific preferences and dietary needs.

### Marketing:

- Digital Marketing: Utilize social media, SEO, and online advertising to reach and engage the target audience.
- Partnerships: Collaborate with local food bloggers and community organizations.
- Customer Loyalty Programs: Reward loyal customers with discounts, exclusive deals, and eventually referral programs.

### Operation Plan: 

- Relationships: Develop strong relationships with local farmers and producers. Also engaging in the local community with events to help promote eating/buying local.
- Inventory Management: Implement a robust inventory system to ensure freshness and minimize waste.
- Order Fulfillment: Building a team of local drivers to deliver our service in time frame we require to keep the customers happy. Ensuring they go the extra mile to assist customers when delivering our product.

As this is an ever growing business there is no set time line. Due to everything that can change on a weekly basis with the nature of the service that is offered. 

But by rolling our in phases we are able to cut the chance of things going wrong drastically. Starting by launching our core products in Essex. Having them become established as a service and getting everything right. Before eventually expanding to different regions and areas, forming new relationships with farmers/artisans/bakers/producers around the country.

## Media Page

An online presence for a new business is a crucial part of the launch of a new company. As this promotes to a wide audience of people in a targeted area. 
<br>
<details>
<summary>Media Page</summary>
<br>
<img alt="Localitty facebook media mockup page" height="300px" src="static/media/readme/locality-media.png">
</details>

## Technology Used

During the development of the app multiple different types of technology was used and utilized to build the final application. 

- HTML - Was used to create the basic web page for the project
- CSS - Was used to style the web page and the different elements that make up the application
- JS - Was used to create a few simple functions for ease of use. Such as changing the date in the footer.
- Python - Used during the development of the back end of the application for everything that communicates with different servers and databases
- Django - Was used as the base development framework. Allowing the use of template and and back end driven development. 
- Bootstrap - Was used to speed up development time due to the vast array of helper classes and systems they have in place. And with the various free templates and code snippets they offer to their users.
- AWS - Used to hose the static files for the application (Media files and Static Files)
- ElephantSQL - Was used for the hosting of the database that contains all the products on the application
- Github - Was used for source control of the project allowing progress of the application to be tracked and stored in one place
- Gitpod - Was used as an IDE. Allowing for the development of the application anywhere anytime
- Heroku - Was used to host the application on the internet for all to use and see

## App Testing

During the development of the Project it has been subjected to different testing methods to ensure that all points are hit. No errors are found in the code as well as manual testing of the app to ensure everything works as intended. There was also testing involved to ensure that the application would be responsive and work on all screen sizes and device types by using the built in google chrome developer tools. To allow for the best accessability possible. The image for this can be found at the top of the document.


| Test | Intended Result | Result |
|------|-----------------|--------|
| Account Creation | Allows the user to create an account and confirm their email address | Passed |
| Change Password | Allows the user to change their password | Passed |
| Email Verification | Allows the user to verify their email address | Passed |
| Change Email | Allows the user to change or update their email | Passed |
| Jop Application | Allow a user of the application to submit an application for a job | Passed |
| Job Application Message | Display a message informing the user that the application was submitted successfully | Passed |
| Job Send copy | Send a copy of the job application to the applicant | Passed |
| Item Favorites | Allows the user to 'favorite' an item for quick access later on | Passed |
| Item Remove favorites | Allow the user to remove an item from their favorites | Passed |
| Select Quantity | Allows the user to adjust quantity of items to add to the bag | Passed |
| Add items to bag | Allow the user to add items from the store to the bag | Passed |
| Bag items edit | Allow the user to change item quantity and remove items from the shopping bag | Passed |
| Add items to favorites | Allow the user to create a favorite items list | Passed |
| Remove items from favorites | Allow the user to remove items from a favorites list | Passed |
| Add items to basket message | Display a message when an item is added to the basket | Passed |
| Remove items from basket message | Display a message when an item is adjusted or removed from basket | Passed |
| Order confirmation message | Display a message once an order has been completed | Passed |
| Display message for errors | Display a message if a user cannot access a certain page of the application | Passed |
| Product Add Message | Display a message when a product is added to the store | Passed |
| Product Edit Message | Display a message when a product is being edited | Passed |
| Delete Product Message | Display a message when a product has been deleted | Passed |
| Error 404 Page | Display an Error 404 page if there is an error on the application | Passed |
| Secure Checkout | Allows the user to add their billing information securely into the app | Passed
| Checkout | Allow the user to checkout securely checkout and process the order | Passed |
| Order Creation | Order is created inside of the database | Passed |
| Order Confirmation | Displays the order confirmation to the user with the correct order number | Passed |
| Order History | Allow the user to see their previous order history | Passed |
| Order Confirmation Email | Sends the order confirmation emails to the user (Including all items in order) | Passed |
| Save info | Allow the user to save default shipping information to their profile | Passed |
| Support | Allow the user to send a support contact form request | Passed |
| Admin Order History | Allow the store admins to view all order history | Passed |
| Admin product create | Allow the store admins to create products on the store | Passed |
| Admin product edit | Allow the store admins to edit current products on the store | passed |
| Admin product delete | Allow the store admins to delete current products on the store | Passed |
| Admin Job Create | Allow the admin to create a job post | Passed |
| Admin Job Edit | Allow the admin to edit a job post | Passed |
| Admin Job Delete | Allow the admin to delete a job | Passed |
| Admin View Applicants | Allow the admin to view job applications | Passed |
| Admin Delete Applications | Allows the admin to delete new job applications | Passed |
| Job Post Message | Display a message when a job was posted successfully | Passed |
| Job Edit Message | Display a message when a job was edited successfully | Passed |
| Job Delete Message | Display a message when a job was Deleted successfully | Passed |
| Job Application Email | Send an email with the job applicants data to the admin | Passed |
| Total Store Items | Allows the Admin to see the total number of items in the store | Passed |
| Total Revenue | Allow the store admins to view the total store revenue | Passed |

<br>
<details>
<summary>Lighthouse</summary>
<br>
Although only one image is shown of a lighthouse score. The average score across the site is 75 to 80 of total performance
<br>
<img alt="Lighthouse testing" height="300px" src="static/media/readme/lighthouse.png">

</details>
<br>

<details>
<summary>HTML </summary>
<br>
Testing the html is a vital part of web development, To ensure that all features and parts of a website function as intended by the developer.
<br>

Deployed website showing errors. But only due to the django syntax inside of the html file. And the validation tool used not understanding or working with such syntax.
<br>
<img alt="Html testing" height="300px" src="static/media/readme/lighthouse.png">

<br>
Despite errors being shown in the validation tools. No errors due to html are present. The errors are due to the validation tools not working with the django/python syntax. This can be avoided by using different validation middlewares that are designed to work with django and python.
<br>
<img alt="Html testing Errors" height="300px" src="static/media/readme/html-error.png">

</details>
<br>

<details>
<summary>Css Testing</summary>
<br>
Despite there being errors in the validation. I believe this is due to the validation service not being updated for newer versions of css.
<br><br>
<img alt="CSS Testing" height="300px" src="static/media/readme/css-validate.png">

</details>
<br>

<details>
<summary>Javascript Testing</summary>
<br>
Despite there being warnings on the JS testing. This is due to missing semi colons and JSON syntax not being recognized. Not causing any code breaking bugs.
<br><br>>
<img alt="JS Testing" height="300px" src="static/media/readme/js-testing.png">

</details>
<br>

<details>
<summary>Pep8</summary>
<br>

Despite warnings about line length and blank spaces at the end of the lines of code. There are no significant application breaking bugs in any of the python code that is running the application.
<br><br>

<img alt="Pep8 Showing line to long errors" height="300px" src="static/media/readme/pep81.png">
<br>
<img alt="Pep8 Showing no errors in code" height="300px" src="static/media/readme/pep82.png">


</details>
<br>

## Bugs

During the development of the application there were many different bugs along the way. From a simple syntax error to an application breaking bug. Some of them are in the table below.


| Bug | Fix |
|-----|-----|
| Profiles Modules not being found | Fixed by re ordering the urls in the main application files | Fixed |
| Product filtering selection not displaying on the selection box. But filtering products | Unfixed |
| Product Quantity selection not working. Page refreshing on button click | Small typos in the JS file | Fixed |
| Orders not being saved to the database. But being sent to stripe | Connected to other small bugs. But fixed by fixing a typo with the UUID generation | Fixed |
| Checkout success page not loading | Error in the name of the checkout success page file name | Fixed |
| Pagination errors. Cant paginate an un ordered list | Fixed by adding the order_by() method onto the selector | Fixed |
| Confirmation emails not being sent during development | Due to stripes webhook handlers not working in development on a local host. But working when deployed |
| Delivery costs not calculating correctly | Fixed by changing the percentage to be divided by | Fixed |
| Product category not displaying on product card in store page | Unfixed |
| Delivery Charge not calculating correctly at checkout | Due to total amount not being divided inside of the contexts | Fixed |
| Image on product edit page not displaying | Not entirely sure what caused this error. But dditing forms.py file seemed to fix the issue. | Fixed |
| Favorites being shown on the product edit form | Due to all fields being rendered on the form. Edited forms.py to remove that field | Fixed |
| Job Edit form not displaying | Due to the job post model being used instead of the form inside of the view | Fixed |

## Project Deployment

Heroku was used to deploy the application live to the internet. The live Application can be found here.
<br>
[Localitty](https://ci-localitty-e5ac9cc8af68.herokuapp.com/)

<details>
<summary>Elephant SQL Deployment</summary>
<br>
The database behind Localitty was done by utilizing the free tier of SQL from ElephantSQL. By following the below steps you can see how the database was created and in the following Heroku deployment steps. You can see how they are linked together to work with each other. 

### Step One

<br>
Create a new instance on your user dashboard
<br>

<img alt="Create the Database" height="300px" src="static/media/readme/sql-1.png">

### Step Two 

<br>
Name the instance of for your app and select the plan that is required. That is connected to a certain project. It is recommended that these are similar, so not to get confused.
<br>

<img alt="Fill Out the information" height="300px" src="static/media/readme/sql-2.png">

</details>

<br>

<details>
<summary>Heroku Deployment</summary>
<br>
Heroku is used as a way for developers and companies to deploy and manage their websites with ease. Allowing the easy connection of things such as databases and media storage. 

### Step One
<br>
Click on the create an app button on your heroku dashboard.
<br>

<img alt="Create The App" height="300px" src="static/media/readme/heroku-1.png">

### Step Two

<br> 
Name your new application and select a server that is local to you, to improve the speed and reliability of your application.
<br>

<img alt="Name the app" height="300px" src="static/media/readme/heroku-2.png">


### Step Three

<br>
Linking the Heroku app to the Github repo allows for smoother and automatic deployments. Directly from pushing an update to github, the Heroku Service will automatically build a new version and deploy with web app.
<br>

<img alt="Link to github" height="300px" src="static/media/readme/heroku-3.png">

### Step Four

<br>
Add config variables to your app. So you are able to control things from inside of the app from an external source. Such as sending emails by connecting to smtp servers. Or a database so you can store information required for features of the app to run.
<br>

<img alt="Add the config vars" height="300px" src="static/media/readme/heroku-4.png">

</details>

<br>

If you are wanting to take a look at the code and potentially add on your own features to the project you can do so by cloning or forking the repo. By doing this it will allow you to locally develop and add your own features to the app.

<details>
<summary>Clone and Forking</summary>
<br>

By clicking the fork button. You are able to then clone the repo as it is and add it as a repo inside of your own github profile. Where you can develop and push new and improved features to the repo on your profile without touching the original project. 

Step 1
<br>
<img alt="Clone the repo" height="300px" src="static/media/readme/fork-repo.png">

<br>
Step 2
<br>
<img alt="Clone the repo" height="300px" src="static/media/readme/fork-repo1.png">

<br>
Alternatively you are able to simply clone the repo straight from the code itself. Without adding it to your own github profile. But when doing this, a warning is required as pushing new code and features to this method will push them to the main repo of the project. This can be avoided by making a new branch of the code.

<br>
<img alt="Clone the code" height="300px" src="static/media/readme/clone-repo.png">

</details>

## Sources

### Code

All code for the project was written by myself. Whilst using Stack Overflow, Google, various Youtube videos and Code Institute Slack Chats for reference and problem solving. Also being aware of the Code Institutes 'Botique Ado' Walkthrough for code reference and guidance along the way

Also using various code samples Bootstrap library of free sample code

### Colors 

The colors that were chosen for the project were picked because they were all simple yet bold colors. All contrasting each other allowing for an easy to read/view application. 

<details>
<summary>Color Palette</summary>

<img alt="Color Palette for the application" height="150px" src="static/media/readme/locality-colors.png">

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

