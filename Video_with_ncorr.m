clc;    % ryd command window
close all;  % luk all figure
imtool close all;  % luk alle imtool figure.
clear;  %slet eksisterende variable.

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

%load data til program

%load reference billede
path = string(g{1,1}(1,tt))+'/Frame_0000.png';
path_new = strrep (path, '\', '/');
ref = imread(path_new);

%for at loade current images skal de stilles op i et cell array til dette
%laves der et loop 

%sæt hent path op
dircur = string(g{1,1}(1,tt))+'/*.png';
%bestemmer længeden af path



    ca = 'C:\Users\chris\Desktop\Program_efter_aflevering\Data_01\Refbillede 29-10-2020\Frame_0000.png';
    


%diffinere vores current til at være det cell array


%deffinere vores region of interest
%dette kræver at man selv har lavet et billede eller skal det tegnes på

%roi = imread('auto hent path før');

%deffinere dataen i ncorr
handles_ncorr.set_ref(ref);
handles_ncorr.set_cur(ca);
%handles_ncorr.set_roi_cur(roi);

%%your code here


end