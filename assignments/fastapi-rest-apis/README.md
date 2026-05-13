# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a RESTful API using the FastAPI framework. Students will learn how to define routes, validate request data with Pydantic models, handle HTTP methods, and return JSON responses.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Application

#### Description
Start a FastAPI app with a simple route that returns a list of items. Each item should include a name, description, price, and availability.

#### Requirements
Completed program should:

- Create a FastAPI application instance named `app`
- Define a `GET /items` endpoint that returns a list of sample items
- Use a Pydantic model to define the item schema
- Ensure the response is JSON serializable


### 🛠️ Add Item Detail and Error Handling

#### Description
Add an endpoint that returns a single item by its `item_id`. The endpoint should return a 404 error when the item does not exist.

#### Requirements
Completed program should:

- Define a `GET /items/{item_id}` endpoint
- Return the item details when the item exists
- Use `HTTPException(status_code=404)` for missing items
- Demonstrate the endpoint with at least two sample items


### 🛠️ Create and Update Items

#### Description
Add endpoints to create a new item and update an existing item using JSON request bodies.

#### Requirements
Completed program should:

- Define a `POST /items` endpoint that accepts a JSON body for a new item
- Validate request data using the `Item` Pydantic model
- Define a `PUT /items/{item_id}` endpoint that updates an existing item
- Return the updated item data after creation or modification
