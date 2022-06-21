# 💲🏡 House-price-predictor 


## Table of Contents

 - [First look](https://github.com/maciekmalachowski/House-price-predictor#first-look)
 - [Installation](https://github.com/maciekmalachowski/House-price-predictor#installation)
 - [Fields](https://github.com/maciekmalachowski/House-price-predictor#fields)
 - [App appearance](https://github.com/maciekmalachowski/House-price-predictor#app-appearance)

# First look
Predictor is a web application built on `django`. It uses models written in `jupyter-notebook`, which are responsible for all predictions. To select the parameters of the house, the application uses `django-forms`, which automatically enters the data into the database and returns the result of the prediction in the form of price and details that we selected for our dream house in **Ames city**. 

# Installation
First, we need to install the requirements contained in the ``requirements.txt``. Open your shell and paste the following comands.
```
pip install -r requirements.txt
```
Then we have to go to ``server`` folder 
```
cd House-price-predictor/server
```
and run server with this command
```
manage.py runserver
```
After that we will see a link leading to our application and it looks like this:
```
http://127.0.0.1:8000/
```
Copy and paste it into browser window to *open application*.

# Fields
To create your dream house we have many options to choose from, such as:
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

# App appearance


