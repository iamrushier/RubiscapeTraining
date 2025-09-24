# RubiscapeTraining

# Assignment : Django Event Scheduler Assignment

Python web framework: **Views, URLs, Templates, Models, Forms**

---

## Django Assignment: Event Scheduler Web Application

### Objective

Extend the Event Scheduler from the Python assignment into a web application using Django.  
The web application will allow users to **create, view, update, and delete events**, as well as **set reminders**.  
This will involve user authentication, form handling, and integrating templates for a seamless user experience.

---

### Assignment Steps

#### 1. Project Setup

- Create a new Django project named `event_scheduler`.
- Create a new app within this project named `events`.

#### 2. Models

Define an **Event** model with the following fields:

- `name` (CharField)
- `date` (DateField)
- `time` (TimeField)
- `description` (TextField)
- `created_at` (DateTimeField, auto_now_add=True)
- `updated_at` (DateTimeField, auto_now=True)

Each event should be associated with a **user** (use Django’s built-in `User` model).

#### 3. User Authentication

- Implement user registration, login, and logout functionality using Django’s built-in authentication views.
- Each user should only be able to manage **their own events**.

#### 4. Forms

- Create a form for creating and updating events.
- Implement form validation to ensure **no scheduling conflicts**.

#### 5. Views

Create views for:

- List all events for the logged-in user.
- Create a new event.
- Update an existing event.
- Delete an event.
- View event details.

#### 6. Templates

- Create simple templates for the views mentioned above.
- Use Django template language to handle form submissions and display event details.

#### 7. Testing

- Write basic **unit tests** for models, forms, and views.
