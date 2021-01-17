# Image-sequencer-for-NCORR
This is a image sequencer made for preparing data to be used in NCORR, which is a program that allows one to measure the two dimensional strain of an object using image correlation, created by Justin Blaber.

https://github.com/justinblaber/ncorr_2D_matlab


The program has a GUI made with Tkinter, and will sequence a video file into individual images and then save them in a folder named after the video at the videos path. It will also correctly name the frames so it fits with the ncorr format, making the data ready to be processed. futhermore it will open ncorr through the GUI.

# requirements 
1. Matlab
2. NCORR
3. Anaconda

# known bugs
1. closing the sequencer will also close NCORR
2. cant process files with unusual characters like æøå



