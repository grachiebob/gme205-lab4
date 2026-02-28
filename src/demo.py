# testing spatial.py (Implementing SpatialObject, Point, Parcel)
from spatial import Point, Parcel
from analysis import total_active_area, parcels_above_threshold, count_by_zone, intersecting_parcels # testing analysis.py

# p1 = Point(100,80)
# p2 = Point(-100,-80)
# print(p1,p2)

parcel_1 = Parcel(
    p_id=1,
    zone='Commercial',
    is_active=True,
    geometry_data={'type': 'Polygon', 'coordinates': [[(120.56,17.65),(124.89,15.46),(120.64,14.65),(121.0,15.56),(120.56,17.56)]]}
)

parcel_2 = Parcel(    
    p_id=2,
    zone='Residential',
    is_active=False,
    geometry_data={'type': 'Polygon', 'coordinates': [[(121.10,16.50),(122.00,16.46),(122.64,15.65),(121.0,15.60),(121.20,16.50)]]}
)

# print(parcel_1)
# print(parcel_2)

# print("Do parcels intersect?", parcel_1.intersects(parcel_2))

parcels = [parcel_1, parcel_2] 
print("Total active:", total_active_area(parcels))

'''
for parcels above threshold
'''
total_threshold = 0.1                                                  
above_threshold = parcels_above_threshold(parcels, total_threshold)
print (f"Parcels with area > {total_threshold}:")
for par in above_threshold:
    print(par)

'''
parcel counts by zone
'''
counts_zone = count_by_zone(parcels)
print("Parcel counts by zone:")
for zone, count in counts_zone.items():
    print(f"{zone}: {count}")

'''
Intersecting parcels
'''
parcel_residential = intersecting_parcels(parcels, "Residential")
print("Residential parcels:")
for res in parcel_residential:
    print(res)