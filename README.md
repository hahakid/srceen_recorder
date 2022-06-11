# srceen_recorder
Auto win10 recording img for TX meeting


python == 3.6 for win32gui

All dependences are listed in `requirements.txt`, use `pip install -r requirements.txt`

scikit-image ssim is used to compare continues images when TX meeting is on (use full screen, and cancel the Power options of win10 for not shutdown the screen during the meeting).

following parameters can be changed based you.

# sim_thresh = 0.9  # for similarity, the bigger the similar
# slot = 5  # sleep 5 second between two samlping

still need manully checking the recorded images, and merge as a PDF.
