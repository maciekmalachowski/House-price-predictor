[![Run tests](https://github.com/maciekmalachowski/House-price-predictor/actions/workflows/test.yml/badge.svg)](https://github.com/maciekmalachowski/House-price-predictor/actions/workflows/test.yml)

<h1 align="center">💲🏡 House-price-predictor</h1>

<h2 align="center">See for yourself <br> ▶ https://hppredictor.herokuapp.com ◀</h2>

## Table of Contents

 - [First look](https://github.com/maciekmalachowski/House-price-predictor#first-look)
 - [Installation](https://github.com/maciekmalachowski/House-price-predictor#installation)
 - [Fields](https://github.com/maciekmalachowski/House-price-predictor#fields)
 - [User authentication](https://github.com/maciekmalachowski/House-price-predictor#user-authentication)
 - [App appearance](https://github.com/maciekmalachowski/House-price-predictor#app-appearance)
 
 <br>
 
<h1 align="center" id="first-look"> First look 👀 </h1>

#### Predictor is a web application built on `django` along with machine learning features. The application models are written in `jupyter-notebook`, which uses `RandomForestRegressor` to properly create all predictions. 

#### To select the parameters of the house, the application uses `django-forms`, which automatically enters the data into the database and returns the result of the prediction in the form of price and details that we selected for our dream house in **Ames City**. 

#### It also has `user authentication` and all to improve your predictions.

<br>

<h1 align="center" id="installation"> Installation ℹ </h1>
 
First, you need to install the requirements contained in ``requirements.txt``. Open your shell and paste the following commands:
```
pip install -r requirements.txt
```
Then you have to go to the ``server`` folder 
```
cd House-price-predictor/server
```
Next, run the server with this command
```
manage.py runserver
```
After that, you will see a link leading to our application, and it looks like this:
```
http://127.0.0.1:8000/
```
Copy and paste it into the browser window to *open the application*.

<br>

 <h1 align="center" id="fields"> Fields ☑</h1>
 
To create your dream house, you have many options to choose from, such as:
 
- **Lot size in square feet**
- **General shape of property**
- **Type of dwelling**
- **Style of dwelling**
- **Physical locations within Ames city limits**
- **Type of road access**
- **First Floor square feet**
- **Second floor square feet**
- **Number of bedrooms above basement level**
- **Number of kitchens**
- **Total rooms above grade (does not include bathrooms)**
- **Full bathrooms above grade**
- **Basement quality**
- **Total square feet of basement area**
- **Basement full bathrooms**
- **Garage type**
- **Size of garage in square feet**
- **Type of roof**
- **Roof material**
- **Type of foundation**
- **Paved driveway**
- **Open porch area in square feet**
- **Pool area in square feet**
- **Heating quality and condition**
- **Central air conditioning**
- **Electrical system**

<h1 align="center" id="user-authentication"> User authentication 🔑</h1>

User authentication was created to reduce the risk of database hacking. <br>
It is a very simple `login` along with `account registration`. <br>
Below, you can see how both sides look.

## Login
![](media/login.png)

## Registation
![](media/registration.png)


 <h1 align="center" id="app-appearance"> App appearance 🔍</h1>
 
The application is divided into three parts: 
- **Main** part, where you choose from among the given fields which house we are interested in.
- **Predictions** part, where all our created houses are displayed together with their estimated price.
- **Details** part, where you can see our selections when creating the house.

<br>

## Main

After clicking the `Make prediction` button, you will be taken to the next page, where previous predictions are displayed.
and your last prediction will be displayed at the bottom.

![](media/main.png)

###### If you do not see the gif below, please wait a moment

![](media/main.gif)

<br>

## Predictions and details

To go to the details of the prediction, click on it. It will take you to the next page, where you will find the details.

![](media/predictions.gif)


#### More images and gifs can be found in the `media` folder.



