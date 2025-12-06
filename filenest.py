import os
import shutil

def organize_files(bp):
    if not os.path.isdir(bp):
        print("The path does not exist.")
        return
    
    for item in os.listdir(bp):
        ip =os.path.join(bp, item)

        if os.path.isfile(ip):
            fn = os.path.splitext(item)[0]
            fpnew = os.path.join(bp, fn)

            if not os.path.exists(fp_new):
                os.mkdir(fpnew)
            shutil.move(ip, os.path.join(fpnew, item))
            print(f"Moved '{item}' into '{fn}/'")

    print("done organizing")
fp= input("Enter the folder path: ")
organize_files(fp)


