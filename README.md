# Food Truck Finder API

Welcome to the Food Truck Finder API! This API is designed to help you discover food trucks based on your location using latitude and longitude coordinates.

## Introduction

The Food Truck Finder API allows users to find food trucks in their vicinity by providing their geographical coordinates. Whether you're in a new city or just exploring your local area, this API makes it easy to locate and discover various food trucks offering delicious meals.

### Key Features:

- **Location-Based Search:** Find food trucks based on your current location, making it convenient for users to explore nearby culinary delights.

- **User-Friendly Interface:** The API is designed with simplicity in mind, ensuring an intuitive and straightforward user experience.

## Getting Started

### Prerequisites

Make sure you have the following installed on your machine:

- Python (3.7 or higher)
- pip (Python package installer)

### Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/food-truck-finder-api.git
    cd food-truck-finder-api
    ```

2. **Create a Virtual Environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment:**
   - On Windows:

        ```bash
        venv\Scripts\activate
        ```

   - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install Requirements:**

    ```bash
    pip install -r requirements.txt
    ```

### Run the API

1. **Apply Migrations:**

    ```bash
    python manage.py migrate
    ```

2. **Create a Superuser (Optional):**

    ```bash
    python manage.py createsuperuser
    ```

3. **Run the Development Server:**

    ```bash
    python manage.py runserver
    ```
4. **Access the API:**

- Open your web browser and go to http://127.0.0.1:8000/ to explore the API.
- Use tools like Postman or Insomnia to interact with the API programmatically.
- If you created a superuser, you can access the Django Admin at http://127.0.0.1:8000/admin/ and log in with the superuser credentials.

### API Endpoints
- /api/foodtrucks/: Retrieve a list of all food trucks.
- /api/foodtrucks/{food_truck_id}/: Retrieve details of a specific food truck.
- /api/foodtrucks/search/: Search for food trucks based on location coordinates.
  - Provide you latitude and longitude and the API will return foodtrucks in a 1km radium of where you are:
      - http://127.0.0.1:8000/api/foodtrucks/search/?latitude=33.42&longitude=-122.44&limit=5&offset=0
  - If you want a wider area, you can also provide the radium you desire:
      - http://127.0.0.1:8000/api/foodtrucks/search/?radium_km=2&latitude=33.42&longitude=-122.44&limit=5&offset=0

Feel free to explore and enjoy the Food Truck Finder API! If you have any questions or feedback, please reach out to us.
