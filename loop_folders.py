for root, dirs, files in os.walk(in_raster_folder):
    for name in files:
        if name == "ras.tif":
            print os.path.join(root, name) # C:\...\...\042116\ras.tif
            print os.path.relpath(root, in_raster_folder) # 042116
            print name # ras.tif
