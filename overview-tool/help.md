---
title: Overview Tool | Help
author: Jarmo Kivekäs
layout: hotosm-layout-overview-tool

---


The intended use of this tool is to help HOTOSM activation managers to keep track of progress in ongoing projects in an activation.





## Search Criteria



**Note** this software is an experimental prototype. Many of the filter values require exact spelling to match search results. Ideally there would be a auto-completion feature for accepted values. However it's yet to be implemented. Instead you can press the `(?)` next to each filter field to get the JSON API listing of the accpted values. It's inconvenient, but hopefully a little helpful.

Filter fields may be left empty, in which case they are simply ignored. Please use at least one field: if all the fields are empty, the search will return every project in the tasking manager. 

- **Text search** is a free-form keyword search for projects. Useful for example in large activations 

- **Campaign** has to be a specific campaign in the tasking manager. For now the list of valid values are listed here https://tasking-manager-tm4-production-api.hotosm.org/api/v2/campaigns/

- **Country** in which the project area is situated in. Exact spelling of accepted values spelling here https://tasking-manager-tm4-production-api.hotosm.org/api/v2/countries/

- **Organisation name** Name of the organisation runnin or requesting the project, e.g "British Red Cross" or "Missing Maps". Accepted values listed in  https://tasking-manager-tm4-production-api.hotosm.org/api/v2/organisations/


- **Interests** one of the mapper interests, e.g. "disaster response" or "public health". Accepted valus listed in  https://tasking-manager-tm4-production-api.hotosm.org/api/v2/interests/


## Saving filters for future use

Search filters are saved to the URL of the page when clicking the "Apply Filters" button. You can save or share a search result by copying the page's URL from you browser address bar. Accessing the link later will run the search again with the same filters applies.



## Sort orders

Currently uses the Tasking manager default sorting order which is based on the urgency


### By project ID

Ordering by project ID is very useful for creating tables for Wikis or spreadsheets that are consistent over the time of the activation. Project ID's are a sequential increasing number. This means sorting by project ID will sort the project in order of creation. Over the span of weeks or months during the activation, this order will stay the same which makes it a good default order to use in activation documentation as it will prevent projects moving up and down in the table over time. 

#

## Planned features


### Pending Archival filter 

Projects matching the "Pending archival" filter are:

- Over 99% mapped
- Over 99% validated
- Have the `PUBLISHED` status

These projects need attention from activation management to be brought all the way to completion, and eventually set to the `ARCHIVED` status. 

### Pending Validation filter

Project mathing the "Pending Validation" filter are:

- over 99% mapped
- less than 99% validated
- have the `PUBLISHED` status

These projects can be brought to the attention of validation teams by the activation management 

### Autocompletion

Autocompletion of dropdown list of accepted values if filter fields

