# GmE 205: Laboratory 4 
## Structured Programming + Object Systems Integration

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
