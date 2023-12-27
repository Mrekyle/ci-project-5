# Localitty

Link to live Localitty project: [Localitty - CI Project Five - Eccommerce Specialization](https://ci-localitty-e5ac9cc8af68.herokuapp.com/)

## Table of Contents 
1. The Project
    - Project Goals
    - Initial Design
2. Features
    - Implemented
    - Future Development
3. Business Plan
    - The plan
    - Media Page
    - Keyword Research
4. Technology used
5. Testing
    - Manual
6. Bugs
7. Project Deployment
8. Sources
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

<img alt="Home Page, Shop Page and User Dashboard" height="250px" width="400px" src="../ci-project-5/media/readme/home-shop-user.png">

###  Support, Dont GnocchIt and Admin Dashboard

<img alt="Support Page, Dont Gnocchit and Admin Dashboard" height="250px" width="400px" src="../ci-project-5/media/readme/support-dontgnocchit-admin.png">

Despite there being other pages on the application that are not included in the initial wireframe design. They all followed the core theme of the application and store. This allowed less going back and forth designing new pages in wireframe's, meaning the development of certain features and pages could commence straight away.

</details>


<details>
<summary>Database Diagram</summary>
<br>
With the design of the database being a crucial part of the applications core design it was important to get it right. 

Although not all designs are implemented into the live application is leaving room for future development with the implementation of 'user product rating and comments' and 'individual supplier stores' to allow them to manage their own products and sell on the platform.

<img alt="Recipe database design" height="250px" width="400px" src="../ci-project-5/media/readme/locality-database.png">

</details>

## Future Development

### Implemented

The basic features that are currently implemented into the application are

<details>

- User Contact form
- User account creation
- User store functionality(add items to bag, checkout securely, receive order confirmation email)
- User to save information to their account
- User to see previous order history
- User to sign up for mailing list

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
| Add items to bag | Allow the user to add items from the store to the bag | Passed |
| Bag items edit | Allow the user to change item quantity and remove items from the shopping bag | Passed |
| Checkout | Allow the user to checkout securely checkout and process the order | Passed |
| Save info | Allow the user to save default shipping information to their profile | Passed |
| Previous Orders | Allow the user to view previous order history on their account | Passed
| Support | Allow the user to send a support contact form request | Passed |
| Admin Order History | Allow the store admins to view all order history | Passed |
| Admin product create | Allow the store admins to create products on the store | Passed |
| Admin product edit | Allow the store admins to edit current products on the store | passed |
| Admin product delete | Allow the store admins to delete current products on the store | Passed |
| Total Revenue | Allow the store admins to view the total store revenue | Passed |


<br>
<details>
<summary>Lighthouse</summary>

<img alt="Clone the repo" height="300px" src="">

</details>
<br>

<details>
<summary>W3C</summary>

<img alt="Clone the repo" height="300px" src="">

</details>
<br>

<details>
<summary>Css Testing</summary>

<img alt="Clone the repo" height="300px" src="">

</details>
<br>

<details>
<summary>JsLinter</summary>

<img alt="Clone the repo" height="300px" src="">

</details>
<br>

<details>
<summary>Lighthouse</summary>

<img alt="Clone the repo" height="300px" src="">

</details>
<br>

<details>
<summary>Pep8</summary>

<img alt="Clone the repo" height="300px" src="">

</details>
<br>

## Bugs

During the development of the application there were many different bugs along the way. From a simple syntax error to an application breaking bug. Some of them are in the table below.


| Bug | Fix |
|-----|-----|
| Profiles Modules not being found | Fixed by re ordering the urls in the main application files |
| Product filtering selection not displaying on the selection box. But filtering products | Unfixed |
| Product Quantity selection not working. Page refreshing on button click | Small typos in the JS file |
| Orders not being saved to the database. But being sent to stripe | Connected to other small bugs. But fixed by fixing a typo with the UUID generation |
| Checkout success page not loading | Error in the name of the checkout success page file name |
| Pagination errors. Cant paginate an un ordered list | Fixed by adding the order_by() method onto the selector |
| Confirmation emails not being sent during development | Due to stripes webhook handlers not working in development on a local host. But working when deployed |
| Delivery costs not calculating correctly | Fixed by changing the percentage to be divided by |
| Product category not displaying on product card in store page | Unfixed 

## Project Deployment

Heroku was used to deploy the application live to the internet. The live Application can be found [Here](https://ci-localitty-e5ac9cc8af68.herokuapp.com/)

If you are wanting to take a look at the code and potentially add on your own features to the project you can do so by cloning or forking the repo. By doing this it will allow you to locally develop and add your own features to the app.

<details>
<summary>Clone and Forking</summary>
<br>

By clicking the clone repo button. You are able to then clone the repo as it is. By clicking the fork button you are able to take the code and add it to your own account where you can develop and push new and improved features to the main application. 

<img alt="Clone the repo" height="300px" src="../ci-project-5/media/readme/forking.png">

</details>

## Sources

### Code

All code for the project was written by myself. Whilst using Stack Overflow, Google, various Youtube videos and Code Institute Slack Chats for reference and problem solving. Also being aware of the Code Institutes 'Botique Ado' Walkthrough for code reference and guidance along the way

Also using various code samples Bootstrap library of free sample code

### Colors 

The colors that were chosen for the project were picked because they were all simple yet bold colors. All contrasting each other allowing for an easy to read/view application. 

<details>
<summary>Color Palette</summary>

<img alt="Color Palette for the application" height="150px" src="../ci-project-5/media/readme/locality-colors.png">

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

