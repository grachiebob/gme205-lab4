# GmE 205: Laboratory 4 
## Structured Programming + Object Systems Integration

### *Description*
This project integrates structured functions and object oriented design to analyze the land parcel data in JSON records.

### *Dependencies*
* Python 3.14
* Visual Studio Code
* shapely

### Algorithm for this Project
1. Start
2. Load `data/parcels.json`
3. If file does not exist:
    - Display error message
    - Stop program
4. Convert each record into a Parcel object
5. Store all parcel objects to `all_parcels`
6. If no parcels are loaded:
    - Display `"No parcels found"`
    - Stop program
7. Set:
    - `total_active_area` = 0
    - `total_threshold` = 10000
    - `selected_development_zone` = "Residential"
8. Create:
    - `parcels_above_threshold` = empty list
    - `intersecting_parcels` = empty list
    - `count_by_zone` = empty dictionary
9. For each parcel in `all_parcels`:
    - If parcel is active:
        - Add `parcel.area()` to `total_active_area`
    - If `parcel.area()` is greater than `total_threshold`:
        - Add parcel to `parcels_above_threshold`
    - If `parcel.zone` not in `count_by_zone`:
        - Create `count_by_zone[parcel.zone]` = 0
    - Increment `count_by_zone[parcel.zone]` by 1
    - If `parcel.zone` equals `selected_development_zone`:
        - Add parcel to `intersecting_parcels`
10. Print results:
    - Total active area
    - Parcels above threshold
    - Parcel count per zone
    - Suitable parcels
11. Save summary to `output/summary.json`
12. End

### Pseudocode for this Project
```text
BEGIN
    LOAD data/parcel.json

    IF parcel.json DOES NOT EXIST THEN
    PRINT "Error: File does not exist"
    STOP
    END IF

    CONVERT record INTO Parcel objects
    STORE IN all_parcels

    IF all_parcels IS EMPTY THEN
    PRINT "No parcels found"
    STOP
    END IF

    SET total_active_area = 0
    SET total_threshold = 10000
    SET selected_development_zone = "Residential"

    CREATE parcels_above_threshold = EMPTY LIST
    CREATE intersecting_parcels = EMPTY LIST
    CREATE count_by_zone = EMPTY DICTIONARY

    FOR EACH parcel IN all_parcels
        IF parcel.is_active THEN
            ADD parcel.area() TO total_active_area
        END IF

        IF parcel.area() IS GREATER THAN total_threshold THEN
            ADD parcel TO parcels_above_threshold
        END IF

        IF parcel.zone NOT IN count_by_zone:
            CREATE count_by_zone[parcel.zone] = 0
        END IF

        INCREMENT count_by_zone[parcel.zone] BY 1

        IF parcel.zone EQUALS selected_development_zone THEN
            ADD parcel TO intersecting_parcels
        END IF
    END FOR

    PRINT "Total active area:", total_active_area
    PRINT "Parcels above threshold:", parcels_above_threshold
    PRINT "Parcel count per zone:", count_by_zone
    PRINT "Suitable parcels:", intersecting_parcels

    SAVE summary TO output/summary.json

END
```

### *Reflection*
1. The sequence appears in `run_lab4.py` where it appears to load error, print results in `active_area`, as well as load parcels. The selection is visible in `if parcel.is_active`, which decides what parcel should be included in the total. It is also evident in `if not p:` in `analysis.py`, since it validates whether the parcels are loaded. The statements with `if` let the system choose which is which. For repetition, `for parcel in parcels` in `analysis.py` repeats the same operations to all parcels, such as computing the area or filtering the parcels by threshold. <br> 
2. Algorithm planning helps in organizing the design for the solution. If this phase is removed, the program will most likely be unorganized and complicated, creating `God Functions` or `God Objects`. This phase serves as a systematic guide on how the program or codes will be executed depending on the specified problem.<br>
3. Spatial behavior lives in `Spatial Object` and `Parcel` classes. The `Spatial Object` class contains the method for intersection (`.intersects()`), which means that it executes a geometry-related operation for calculating or checking objects that might possibly intersect or overlap. <br>
4. `analysis.py` contains all the structured function because it performs the data processing and analysis for this exercise. On the other hand, `demo.py` is a running script meant for running, testing or displaying the results to verify whether the functions in the `analysis.py` work. These two Python files remain separated for clarity purposes.<br>
5. If all filter logic were inside the `Parcel` class, the code will become overloaded, producing a `God class`. In this case, `Parcel` would mix geometry and analysis rules. The responsibility of this class would be broad enough and harder to maintain when errors arise or changes are needed.<br>
6.  In this design, add a new rule such as "exclude inactive industrial parcels" will be easy, since the responsibilities of `spatial.py` and `analysis.py` are separated. `Parcel` class contains the geometry, while `analysis.py` contains the functions for filtering and computing. With this design, the system can easily quickly and safely adapt new rules, as the rest of the codes will work as before.<br>
7. Separating structured logic from object behavior prevents `God classes` but just giving the system one responsibility per `.py` file. In `Parcel` class, the responsibility is for geometry purpose, while `analysis.py` is responsible for structured function. With this design, it avoids duplication of tasks and makes the code easier to extend without affecting functionality.<br>

## Author
Maria Graciella L. Roque  
Discord:[@grachiebob]

## Acknowledgements
* GmE 205 Laboratory Exercise 3 Manual
* [MarkDown](https://www.markdownguide.org/cheat-sheet/)

Edited on VS Code