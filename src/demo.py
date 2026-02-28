#testing spatial.py (Implementing SpatialObject, Point, Parcel)
from spatial import Point, Parcel

p1 = Point(100,80)
p2 = Point(-100,-80)
print(p1,p2)

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

print(parcel_1)
print(parcel_2)

print("Do parcels intersect?", parcel_1.intersects(parcel_2))