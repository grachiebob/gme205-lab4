from spatial import Parcel
import json
import os
import analysis

DATA_PATH = "data/parcels.json"
OUTPUT_DIR = "output"
RESULTS_PATH = os.path.join(OUTPUT_DIR, "lab4_results.json")


def load_parcels(filepath: str) -> list:
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    parcels = []

    for item in data:
        p = Parcel(
            p_id=item.get("parcel_id"),
            zone=item.get("zone", "Unknown"),
            is_active=item.get("is_active", False),
            geometry_data=item.get("geometry")
        )
        parcels.append(p)

    return parcels


def main():
    print("=== Laboratory Exercise 4 ===")

    parcels = load_parcels(DATA_PATH)

    if not parcels:
        print("Error: No parcels found.")
        return
    else:
        print(f"Parcels loaded successfully: {len(parcels)} parcels.")

    total_threshold = 10000

    active_area = analysis.total_active_area(parcels)
    above_threshold = analysis.parcels_above_threshold(parcels, total_threshold)
    counts_zone = analysis.count_by_zone(parcels)
    parcels_residential = analysis.intersecting_parcels(parcels, "Residential")

    print("Total Active Area:", active_area)
    print("Parcels Above Threshold:", len(above_threshold))
    print("Zone Counts:", counts_zone)
    print("Residential Parcels:", len(parcels_residential))

    summary = {
        "total_active_area": active_area,
        "parcels_above_threshold": len(above_threshold),
        "zone_counts": counts_zone,
        "residential_parcels": len(parcels_residential)
    }

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    with open(RESULTS_PATH, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print(f"\nSaved report to: {RESULTS_PATH}")


if __name__ == "__main__":
    main()