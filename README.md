# URL_Shortner
This script shortens those lengthy URLs that seem to go forever. 
The code uses url encoding in order to locate the correct website. Certain values which are not a part of the ASCII character list need to be rewritten in order to properly work.

Additionally, by running this code the user is given the option to create a new database and store the new shortened link. Users are also given the opprotunity to delete the database by simply providing its name. This feature uses PostgreSQL and the Python PostgreSQL library psycopg2

The data is inserted into the table "short", which inputs the website name, old url, and the new shortened link. The website name cannot exceed 50 characters and the old url cannot exceed 100 characters.  
