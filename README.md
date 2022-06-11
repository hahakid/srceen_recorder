# srceen_recorder
win10 recorder img for tx meeting
python == 3.6 for win32gui

All dependences are listed in `requirements.txt`, use `pip install -r requirements.txt'

scikit-image ssim is used to compare continues images when TX meeting is on (use full screen, and cancel the Power options of win10 for not shutdown the screen during the meeting).

ssim_thresh = 0.9  # for similarity, the bigger the similar
slot = 3  # sleep 3 second between two samlping

still need manully checking the recorded images, and merge as a PDF.
