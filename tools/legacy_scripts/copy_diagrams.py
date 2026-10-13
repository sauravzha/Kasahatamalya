import shutil
import os

source_dir = r"C:\Users\Saurav\Desktop\Kshamatalaya\approach and mission"
dest_dir = r"C:\Users\Saurav\Desktop\Kshamatalaya\assets"

pic3 = os.path.join(source_dir, "Picture3.png")
pic4 = os.path.join(source_dir, "Picture4.png")

approach_dest = os.path.join(dest_dir, "approach.png")
mission_dest = os.path.join(dest_dir, "mission.png")

try:
    # Assuming Picture3 is Approach and Picture4 is Mission based on typical sequential saving
    shutil.copy2(pic3, approach_dest)
    shutil.copy2(pic4, mission_dest)
    print("Successfully copied Picture3.png as approach.png and Picture4.png as mission.png")
except Exception as e:
    print(f"Error copying files: {e}")
