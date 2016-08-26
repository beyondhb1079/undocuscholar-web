# Backend Web Service

## Contents
- [About](#about)
- [Setup](#setup)
- [API Overview](#api-overview)
  - [HTTP Methods](#http-methods)
  - [Response Format](#response-format)
  - [HTTP Status Codes](#http-status-codes)
- [Scholarship API](#scholarship-api)
  - [Scholarship Attributes](#scholarship-attributes)
  - [Querying Scholarships](#querying-scholarships)
  - [Creating a Scholarship](#creating-a-scholarship)
  - [Updating a Scholarship](#updating-a-scholarship)
  - [Archiving a Scholarship](#archiving-a-scholarship)
  - [Unarchiving a Scholarship](#unarchiving-a-scholarship)

## About
This application serves as the backbone for UndocuScholar by providing a Web Service that returns JSON

## Setup
*TODO*: details on how to clone this repo and set things up

## API Overview

### HTTP Methods
Method | Use
------ | -----------
GET    | Retrieving resources.
POST   | Creating/Unarchiving resources.
PUT    | Updating resources.
DELET  | Deleting/Archiving resources.

### Response Format
Responses are in JSON format.

Node | Description
---- | -----------
code | Error code. A non-zero value indicates an error occurred.
message | Message for the response.
results | List of resources.

### HTTP Status Codes
The following HTTP Status Codes are possible.

Status Code | Description
--- | ---
200 | OK
404 | URL Not Found
500 | Internal Server Error

### Pagination
*TODO*

## Scholarship API

### Scholarship Attributes
*TODO*

Name | Type | Description
--- | ---- | -----------


---
### Querying Scholarships
`GET /api/scholarships`

#### Query Parameters:
*TODO*

Name | Type | Description
--- | ---- | -----------

---
### Creating a Scholarship
`POST /api/scholarships`

#### Arguments
Name | Description | Required? 
--- | --- | ---


---
### Retrieving a Scholarship
`GET /api/scholarships/<id>`


---
### Updating a Scholarship
`PUT /api/scholarships/<id>`

#### Arguments
See arguments for "Creating a Scholarship"


---
### Archiving a Scholarship
`DELETE /api/scholarships/<id>`


---
### Unarchiving a Scholarship
`POST /api/scholarships/<id>`
