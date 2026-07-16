import os

assets_dir = r"C:\Users\Saurav\Desktop\Kshamatalaya\assets"
approach = os.path.join(assets_dir, "approach.png")
mission = os.path.join(assets_dir, "mission.png")
temp = os.path.join(assets_dir, "temp.png")

if os.path.exists(approach) and os.path.exists(mission):
    os.rename(approach, temp)
    os.rename(mission, approach)
    os.rename(temp, mission)
    print("Successfully swapped approach.png and mission.png")
else:
    print("Images not found.")
