import base64
import os 

home_page_location = "/"

title_1 = "Object detection & Tracking"
medium_link_1 = "https://medium.com/@jarrodmccarthy12/object-tracking-with-yolov5-and-sort-589e3767f85c"
git_link_1 = "https://github.com/JarrodMccarthy/vision/blob/main/detector.py"
image_1 = "/static/images/resized_detect.png"
#encoded_image_1 = base64.b64encode(open(image_1, 'rb').read())


title_2 = "Transfer Learning & Binary classification"
medium_link_2 = "https://medium.com/@jarrodmccarthy12/transfer-learning-and-binary-classification-7b1ed02cb431"
git_link_2 = "https://github.com/JarrodMccarthy/vision/blob/main/transfer_face.py"
image_2 = "/static/images/resize_transfer.png"
#encoded_image_2 = base64.b64encode(open(image_2, 'rb').read())


title_3 = "DQ-Learning for Cartpole (& more)"
medium_link_3 = "https://medium.com/@jarrodmccarthy12/d311ccf1dfc0"
git_link_3 = "https://github.com/JarrodMccarthy/pytorch_atari/blob/main/cartpole.py"
image_3 = "/static/images/resized_cartpole.png"
#encoded_image_3 = base64.b64encode(open(image_3, 'rb').read())


title_4 = "DQN - Dynamic picking - On the way"
medium_link_4 = "https://medium.com/@jarrodmccarthy12/dqn-dynamic-picking-45c2ad4220f0"
git_link_4 = "https://github.com/JarrodMccarthy/cobot"
image_4 = "/static/images/resized_robo.png"
#encoded_image_4 = base64.b64encode(open(image_4, 'rb').read())


title_5 = "Robot Lawn mower - On the way"
medium_link_5 = "https://medium.com/@jarrodmccarthy12/remote-control-lawn-mower-3fe24541258e"
git_link_5 = "https://github.com/JarrodMccarthy/robotlawnmower"
image_5 = "/static/images/placeholder286x180.png"
#encoded_image_5 = base64.b64encode(open(image_5, 'rb').read())

title_6 = "Robust HA with MQTT - On the way"
medium_link_6 = "https://medium.com/@jarrodmccarthy12/robust-ha-with-mqtt-failover-7e06cfc2bfd9"
git_link_6 = "https://github.com/JarrodMccarthy/robustha"
image_6 = "/static/images/resized_ha.png"
#encoded_image_6 = base64.b64encode(open(image_5, 'rb').read())


titles = [title_1, title_2, title_3, title_4, title_5, title_6]
medium_links = [medium_link_1, medium_link_2, medium_link_3, medium_link_4, medium_link_5, medium_link_6]
git_links = [git_link_1, git_link_2, git_link_3, git_link_4, git_link_5, git_link_6]
images = [image_1, image_2, image_3, image_4, image_5, image_6]
#encoded_images = [encoded_image_1, encoded_image_2, encoded_image_3, encoded_image_4, encoded_image_5, encoded_image_6]


TIMEOUT = 60