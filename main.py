from frame_extractor import FrameExtractor
import random
input_path="D:\BE Final Year Project\dump\input_video.mp4"
output_path="D:\BE Final Year Project\Data_extraction\output_frames"
fname=''.join([random.choice(['a', 'b', 'c', 'd', 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']) for i in range(6)])
print(fname)
frameextractor=FrameExtractor(input_path,output_path,fname)
frameextractor.extract_frames_by_percentage()