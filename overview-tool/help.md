---
title: Overview Tool | Help
author: Jarmo Kivekäs
layout: hotosm-layout-overview-tool

---




# Search Criteria


**Text search** is a free-form keyword search for projects

**Campaign** has to be a specific campaign in the tasking manager. For now the list of valid values are listed here https://tasking-manager-tm4-production-api.hotosm.org/api/v2/campaigns/

**Country** in which the project area is situated in. Autocomplete missin. Specific spelling here https://tasking-manager-tm4-production-api.hotosm.org/api/v2/countries/

**Interests** shall be one of the interested parties listed in  https://tasking-manager-tm4-production-api.hotosm.org/api/v2/interests/

# Planned features


## Pending Archival 

Projects matching the "Pending archival" filter are:

- Over 99% mapped
- Over 99% validated
- Have the `PUBLISHED` status

These projects need attention from activation management to be brought all the way to completion, and eventually set to the `ARCHIVED` status. 

## Pending Validation

Project mathing the "Pending Validation" filter are:

- over 99% mapped
- less than 99% validated
- have the `PUBLISHED` status

These projects can be brought to the attention of validation teams by the activation management 