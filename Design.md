# Programming languages and frameworks

We will use 
* Python for server side processes and data transformation
* Javascript for client code
* For web frameworks we will either use flask, or Django

# Databases
If we can get away with it, we'll use sqlite, if we need more performance we'll use PostGreSQL

# Data work

Reproducibility and Auditibility are critical for this project.

* We will keep raw data in the repository
* We will write scripts to transform that raw data to final forms
* If a transformation is not captured in a script, it is not allowed. This includes filtering rows, renaming colums, remove whitespace. 
No matter how apparently trivial, every transformation but be reproduced in a script.

For scripting, we will use

* python
* bash scripts

As components of the script we recommend

* csvkit
* the standard linux tool-chaing (grep, sed, awk, make)


