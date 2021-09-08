# File Naming Conventions
This file includes guidelines for writing file names used in the spatial data 
analysis of the 
projects. 
Files should be named consistently, they must be unique and no folder name
should be included in the file name  

## Characters
____
1. Delimiters- use underscore (_) as delimiter to separate terms, do not use 
   spaces 
2. No special characters such as: '*' ':' '' '/' '<' '>' '|' '"' '!' '?' 
   '[' ']' ';' '=' '+' '&' '£' '$' '€' '%' or ','. may be used
3. Periods are only allowed for file format naming (i.e .jpg) and version assignments
4. All the name characters in non directory files should be in lowercase and no
   uppercase shall be used
5. Exceptions apply for functional requirements, for example in names such as R
   referring to R programming language, or 
   [sass partials](https://sass-lang.com/guide#topic-4).
6. Directories may not have multiple versions

**Example:**
```
a_file_created_by_you.file    
Directory_of_some_data
```


### Naming order
The name of each file, including any of the following details should be as 
follows:
1. Description- the name describing the content of the file
2. Data- the date of file creation, Use date format ISO 8601: YYYYMMDD
3. Initials of the group's name- veg: vegetation, carb: carbon, igis: iGIS, 
   admin: administration
4. Name of file creator in camel case (lowercase last name followed by 
   uppercase first name)
5. Status- status of the file (i.e. final, draft) final files of each version 
   must have the status
6. Version- Include a version number, versions should be a "v" letter followed
   by two digits numbers followed by sub-version

**Examples:**
```
desc_20210402_veg_smithJack_final_v01.0.tif     /* extreme combination */
desc_20210412_draft.shp
```


