import os
import time
import cv2

train_videos = ["20220510_034500_4647_B8A44F311703_0.mkv", "20220510_034500_4647_B8A44F311703_1.mkv"]
test_videos = ["20220510_034500_4647_B8A44F311703_2.mkv"]
data_path = "../data/Hens_videos/"
save_path = "/home/vks/Documents/uni/bio/github/hens_tracking/data/photos/"
fpslimit = 1 # throttle limit

def load_video(videos, data_path, save_path):
    
    for i, video in enumerate(videos):
        
        if not os.path.exists(os.path.join(save_path, video.split(".")[0])):
            os.makedirs(os.path.join(save_path, video.split(".")[0]))

        path = os.path.join(data_path, video)

        starttime = time.time()
        cap = cv2.VideoCapture(path)

        # to find the fps of the video
        # fps = cap.get(cv2.CAP_PROP_FPS)
        # print(f"{fps} frames per second")
        
        num = 0
        while(cap.isOpened()):
            # Capture frame-by-frame
            ret, frame = cap.read()

            # if frame is read correctly ret is true
            if not ret:
                print("Can't receive frame. Exiting...")
                break

            nowtime = time.time()
            if (int(nowtime-starttime)) > fpslimit:
                # operations on frame 
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                # cv2.imshow("frame", frame)
                cv2.imwrite(os.path.join(save_path, video.split(".")[0]) + "/" + "frame" + str(num) + ".png", frame)
                num += 1
                starttime = time.time() # reset time
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    # When everything is done, release the capture
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    load_video(train_videos, data_path, save_path)