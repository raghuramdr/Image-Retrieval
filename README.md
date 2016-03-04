# Image-Retrieval
Contains Python 2.7 code for a no frills CBIR engine.

The database used is the Columbia Object Image Library-100 (COIL-100). The link to the website is http://www1.cs.columbia.edu/CAVE/software/softlib/coil-100.php
The workflow is pretty simple. The images are described and indexed using 3-D RGB histograms. For a query image (from the database), the top five histograms similar to the histogram of the query image are located and the corresponding images are displayed. The histogram similarity is computed using the histogram intersection argument available in OpenCV's cv2.compareHist command.
I plan to add code to accept external query images and there are plans to select the query image using a GUI. It is still in the works.
