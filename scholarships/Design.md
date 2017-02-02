# Scholarships DB Design

Due to the information scholarships are described there are interesting attributes of scholarships that are not easy
to model in a database with a single type. This file is meant to document the discrepancies that lie in representing
Scholarships as single rows in a database.

## Scholarship Attributes
There are many properties of scholarships that can be modeled and be used when filtering results based on a user's
profile or search filters set. This is a list of attributes we've come up with.

* Name
* Deadline
* Award Amount
** Could be a fixed value (e.g. $3000), a range (e.g. $500-1000), full tuition, or unspecified
* Website
* Description
* Award Acceptance Rate
* Is Active?
** i.e. Do we know if this scholarship is active? There's a similar attribute we could add called Is Verified if we can
distinguish the use cases between the two.
* Type
** e.g. Academic/Community/Organization/Athletic


## Eligibility Attributes
Pertaining to a scholarship often times are eligibility requirements. In a single table this information could inline with
a scholarship table entry, but would perhaps be better separated if there are disjunctive eligibility requirements

* Minimum GPA
* Major/Area of Study
* Current Education Level
* School/Organization Affiliation Requirement
* Nationality
* Race
* Location/State
* DACA Required?
* Income Requirements
* First Generation?
* Gender
* Eligibility Notes

## Potential Database Design Issues
A lot of these attributes are pretty varied in their representation (such as Award Amount) or don't have a straightforward
solution (such as Location/State). Additionally, qualitative attributes with infinite values are difficult to
provide for scholarship filtering (such as granular Location or Affiliation Requirement).

## Solution
The solution I believe most appropriate solution to target the potential issues that arise is through a couple of steps.

1. For now, leave out attributes that rarely show up or are hard to access or do little to affect the user value of a scholarship.
If this information is available, they could be added to the Description.
** Award Acceptance Rate is a difficult value to retrieve
** Type is useful for classifying the different types of scholarships. However, unless a user is looking for a specific
type of scholarship, this will not be of much value to the typical user.
** Income Requirements, as useful as it can be for a select few scholarships, doesn't usually show up
** First Generation is an attribute that also rarely shows up.
2. Limit text attributes so they can be filterable. In particular, attributes where the user meets only one.
** Major/Area of Study will require a list of possible majors if we're to go to that level of precision. Perhaps it could
be generalized to a more limited set of areas of studies such as Art, Math, Tech, Science, Medical, etc.
** School/Organization Affiliation Requirement could be limited to be a college in the United States (so no organization) or
Not Specified/Blank for all other entries
** Nationality could use the list of all countries.
** Race could be the racial groups used by Census
** Location/State could be limited to the 50 states + territories.
3. Let free text attributes be searchable by query, but not by search filters
** Description, Website, Eligibility Notes are arbitrary text entries, not filterable.

## Proposed Design
