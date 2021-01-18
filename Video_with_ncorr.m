clc;    % clear command window
close all;  % close all figures
imtool close all;  % luk all imtool figures.
clear;  %slet existing variabels.

scriptpath = matlab.desktop.editor.getActiveFilename;
scriptpath = erase(scriptpath, '\Video_with_ncorr.m');

dirtxt = append(scriptpath,'\dir.txt');

filepaths=fopen(dirtxt);
g = textscan(filepaths,'%s','delimiter','\n');
fclose(filepaths);

am_vids = 2;


tt = 1;
while tt < am_vids
handles_ncorr = ncorr;

%load data to program

%load reference picture
path = string(g{1,1}(1,tt))+'/Frame_0000.png';
path_new = strrep (path, '\', '/');
ref = imread(path_new);
 


dircur = string(g{1,1}(1,tt))+'/*.png';


%load region of interest
%roi = imread('auto hent path før');

%deffine data in ncorr
handles_ncorr.set_ref(ref);
handles_ncorr.set_cur(ca);
handles_ncorr.set_roi_cur(roi);



end