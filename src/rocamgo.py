from src.cameras import Cameras
from sys import path
path.append('/usr/lib/pymodules/python2.7')
from cv import ShowImage
from cv import WaitKey


def main():
    # Select camera from computer
    cam = Cameras()
    cams_found = cam.check_cameras()
    camera = cam.show_and_select_camera()
    
    while camera: 
        
        # Show current camera
        img = camera.get_frame()
        ShowImage("Camera", img)

        # Detect goban
        
        # Detect stone
        
        # Upload to internet

        # FPS
        key = WaitKey(30)
        if key == 27: # Esc
            break

    
if __name__ == "__main__":
    main()
