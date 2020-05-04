---
title: Summarizing TM Project statuses in Google Sheets
author: Jarmo Kivekäs
---


Manually keeping track of Tasking Manager projects during an activation can be very time-consuming. And a dull chore.
This chapter describes how project managers and those in the tasking or reporting roles can automate creating Tasking Manager project summaries
for activations using Google Sheets.


The end result is a spread sheet similar to this, which updates the fields automatically:

XXX: add image


# Using the TM API with `ImportJSON()`


Google Sheets does not by default understand the JSON format in which project status data is published by the Tasking Manager.
Luckily, that can be remedied using custom scripts right in the Google Sheets.


You can access Tasking Manager data by adding the  `ImportJSON.gs` script from the [bradjasper/ImportJSON repository on GitHub](https://raw.githubusercontent.com/bradjasper/ImportJSON/master/ImportJSON.gs) to you spreadsheet:

1. Create the sheet where you want the automated project summaries
2. In Google Sheets open *Tools* > *Script Editor*. This should open a new tab with an empty text editor.
3. Get the [`ImportJSON.gs` script](https://github.com/bradjasper/ImportJSON/blob/master/ImportJSON.gs) and paste it into the Google Sheets script editor.
4. press ctrl-S to save the script
1. Set the project name to `ImportJSON` if prompted for a name.

Now you should be able to get project data for project using the `ImportJSON` command. In an empty sheet, use a formula like this (project #8301 in this case):

```
=ImportJSON("https://tasks.hotosm.org/api/v1/project/8301/summary")
```

By default it creates outputs the column headers on the first row and the project data on the next row.

## Improving usability

A nice way to create an automatically updating spreadsheets is to make a **Project ID** column – which you keep manually up to date as new projects are published – and a column which creates all the rest using `ImportJSON(...)`.

Notice that the formula for row 2 is different, using `rawHeaders` instead of `noHeaders`. It is also offset horizontally by one row, as the command creates the column headers on row 1, and ouputs the project data on row 2. `noHeaders` outputs only data, so there is no need for the offset.



row | A | B
---|--|--
1| "ProjectId (Manual)" | `=ImportJSON(concat(concat("https://tasks.hotosm.org/api/v1/project/", A2), "/summary"),"","rawHeaders")`
2|_8301_ |
3|_8302_ | `=ImportJSON(concat(concat("https://tasks.hotosm.org/api/v1/project/", A3), "/summary"), "", "noHeaders")`
4|_8303_ | `=ImportJSON(concat(concat("https://tasks.hotosm.org/api/v1/project/", A4), "/summary"), "", "noHeaders")`
5|_8304_ | `=ImportJSON(concat(concat("https://tasks.hotosm.org/api/v1/project/", A5), "/summary"), "", "noHeaders")`
6|_8305_ | `=ImportJSON(concat(concat("https://tasks.hotosm.org/api/v1/project/", A6), "/summary"), "", "noHeaders")`

Just copy the formulas in the `B` column as many times as needed, and fill in the project IDs that are part of you activation.
