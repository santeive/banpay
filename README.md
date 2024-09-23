# BANPAY APP

This README file covers local (development) and testing directions.

## Develpoment

### Run with docker

#### Requirements

- Install [Docker and Docker compose](https://docs.docker.com/compose/install/)
- Notice docker-related files are placed under `local` folder.

#### Create an `.env` file in the root of the project

Fill the `.env` with the correct values (It will be send by email)

#### In the root of this project

#### Build the image

```bash
make build
```

#### Start the service

```bash
make up
```

#### Stop the service

```bash
make down
```

### Run migrations

```bash
make migrate
```

### Create superuser

```bash
make createsuperuser
```

### Show urls

```bash
make show_urls
```

### tests

```bash
make tests
```

---

## Postman Collection
The Postman collection includes all the above endpoints organized into folders. The **local** and **development** environments allow easy switching between running the API locally or on the development server.

## Environments
1. **Local**: The local environment points to the API running on your local machine.
2. **Development**: The development environment points to the API running on the development server.

- **Postman Environment Variables**: 
  - `{{baseUrl}}`: The base URL for either the local or development environment.
  - **Local example**: `http://localhost:8000`
  - **Development example**: `https://banpay.onrender.com`

## Endpoints Overview

### 1. Folder: USERS
This folder contains endpoints related to user management. All endpoints require authentication unless otherwise stated.

- **Get Users**: 
  - Retrieves a list of all users.
  - **Method**: `GET`
  - **Authentication**: Required
  - **Endpoint**: `/users/`
  
- **Get User**: 
  - Retrieves details of a specific user by their ID.
  - **Method**: `GET`
  - **Authentication**: Required
  - **Endpoint**: `/users/{id}/`
  
- **Update User**: 
  - Partially updates a user's information (can use PATCH for partial updates).
  - **Method**: `PATCH`
  - **Authentication**: Required (Admin role required)
  - **Endpoint**: `/users/{id}/`

---

### 2. Folder: AUTH
This folder manages authentication endpoints, including sign-up, login, and token management.

- **Sign up (Create Users)**: 
  - Creates a new user account.
  - **Method**: `POST`
  - **Authentication**: Not required
  - **Endpoint**: `/auth/signup/`

- **Login**: 
  - Logs in a user and returns access and refresh tokens.
  - **Method**: `POST`
  - **Authentication**: Not required
  - **Endpoint**: `/auth/token/`

- **Logout**: 
  - Invalidates the refresh token, logging the user out.
  - **Method**: `POST`
  - **Authentication**: Required
  - **Endpoint**: `/auth/logout/`

- **Refresh Token**: 
  - Refreshes the access token using the refresh token.
  - **Method**: `POST`
  - **Authentication**: Not required, but a valid refresh token is required
  - **Endpoint**: `/auth/token/refresh/`

---

### 3. Folder: MOVIES
This folder contains an endpoint to retrieve movies based on the user's role.

- **Get Movies**: 
  - Retrieves a list of movies that the user can access based on their role. 
  - **Method**: `GET`
  - **Authentication**: Required
  - **Endpoint**: `/movies/`

---

## Additional Notes
- All endpoints that require authentication use JWT (JSON Web Tokens).
- Make sure to include the `Authorization` header with the access token in the format:
  ```plaintext
  Authorization: Bearer <access_token>
