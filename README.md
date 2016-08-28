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
There are a lot of attributes pertaining to each scholarship. Not all attributes
are returned in a given request.

#### Scholarship List Attributes
These are the attributes that will show up when retrieving a list of results. 
Always check for null or the empty string as those often times indicate no value.

Name | Type | Description
--- | ---- | -----------
`scholarship_id` | integer | The unique identifier for the scholarship
`name` | string | The name of the scholarship
`deadline` | string | The deadline date in format 'YYYY-MM-DD'
`amount` | integer | The max amount of the scholarship
`website` | string | The link for scholarship details

<!-- TODO -->
<!--`description` | string | A description summarizing the scholarship-->
<!--`date_updated` | integer | The epoch time when this scholarship was last updated-->
<!--`archived` | boolean | Whether this scholarship is archived or not-->
<!--`verified` | boolean | Whether this scholarship is verified or not-->

<!--#### Scholarship Detail Attributes-->
<!--These attributes only show up when requesting the details of a particular scholarship-->


<!--Name | Type | Description-->
<!----- | ---- | ------------->
<!--`count` | integer | The number of awards given out, if known-->
<!--`date_created` | integer | The epoch time when this scholarship was created-->
<!--`min_gpa` | double | The minimum GPA required for eligibility-->
<!--`education_range` | string | The education level requirements ("any", "high", "ugrad", "grad") where more than one category is separated by a vertical bar '&#124;'.-->
<!--`nationality` | string | Nationality eligibility requirements-->
<!--`race` | string | Race eligibility requirements-->
<!--`state` | char(2) | The state-specific scholarship requirement-->
<!--`major` | string | Major eligibility requirements-->
<!--`degree` | string | Degree eligibility requirements-->
<!--`daca_needed` | boolean | Whether this scholarship requires DACA-->

---
### Querying Scholarships
`GET /api/scholarships`

#### Query Parameters:

Name | Type | Description
--- | ---- | -----------
`q` | string | The query string
`min_amount` | string | The minimum scholarship amount
`max_amount` | string | The maximum scholarship amount
`deadline_after` | string | The minimum deadline threshold
`deadline_before` | string | The maximum deadline threshold
`sort` | string | The attribute for which to sort by
`sort_order` | string | "desc" to sort in descending order, "asc" to sort in ascending order.
<!--`state` | string | The state for which to find scholarships in-->
<!--`gpa` | double | The max GPA threshold-->
<!--`education_level` | string | The education level ("high", "ugrad", "grad")-->
<!--`has_daca` | boolean | Excludes DACA-only scholarships from the results if set to false.-->

---
### Creating a Scholarship
`POST /api/scholarships`

#### Arguments
Use any/all of the scholarship attributes except for future `date_created`, `date_updated`, and `archived` attributes.
Required: `amount`, `deadline`, `name`, `url`.

---
### Retrieving a Scholarship
`GET /api/scholarships/<id>`


---
### Updating a Scholarship
`PUT /api/scholarships/<id>`

#### Arguments
Use any/all of the scholarship attributes except for future `date_created`, `date_updated`, and `archived` attributes.

#### Arguments
See arguments for "Creating a Scholarship"


---
### Archiving a Scholarship
`DELETE /api/scholarships/<id>`


---
### Unarchiving a Scholarship
`POST /api/scholarships/<id>`
