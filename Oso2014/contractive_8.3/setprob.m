
% This routine is called after setplot2.m by plotclaw2.
%
% Set some additional things for ploting GeoClaw output.
%

%PlotType = 11;     % = 11 for colored surface plot
                   % = 12 for contour plot
quiverplot=0;
PlotFlow = 1;      % plot the surface of the flow
PlotTopo = 1;      % plot the topography
ContourValues = linspace(-1,1,21);
topoContourValues = 30;   % Contour levels for topo.
                          % Set to either a scalar or vector



geo_setzcolormaps;    % set up some useful default colormaps for land, water

zWaterColorsMalpasset = [0  DarkBlue;
                          50 Blue;
                         100 LightBlue];

zWaterColorsMalpasset = [98  LightBlue;
                          100 Blue;
                         102 DarkBlue];

zWaterColorsMalpasset = [98  0 1 1;
                          100 Blue;
                         102 DarkBlue];

zLandColorsMalpasset = [   0  DarkGreen;
                           25  Green;
                           50  LightGreen;
                           100  Tan;
                           150 Brown;
                           200 White];

zLandColorsMalpassetZoom = [   400  DarkGreen;
                           600  Green;
                           650  LightGreen;
                           800  Brown;
                           1550 Tan;
                           ];

zFlume = [ 1.117 Tan;
            1.115 Gray8];

zRedWhiteBlue = [-10 Green
            -1 Red;
            0  White;
            1  Blue];

z_flumedepth = [.5 DarkBlue;
                .1 White;
                0.0 Red];

z_velocity = [ 0 White;
                1.0 Red];
            
z_velocity2 = [ 0 White;
                1.e-2 Blue;
                1. Red];

z_depth = [0. White
           10.0 LightBlue
           20.0 Blue];

z_white = [0. White
           10.0 White
           20.0 White];


z_m = [0.0 Red;
        0.42-1.0e-5 Blue;
        0.42 White
        0.42+1.e-5 Green;
            1.0 Red];

 zDigPressure = [-1 Red;
                0  White;
                10/18.5  LightBlue;
                1  Blue];
            
           zLandColorsMalpasset = [   75+3  DarkGreen;
                           85+3  Green;
                           105+3  LightGreen;
                           120+3  Tan;
                           200+3 Brown;
                           300+3 White];

if mq==6
    flow_colormap = z_velocity;
elseif mq==5
    flow_colormap =zDigPressure;
elseif mq == 1
    flow_colormap = z_white;
elseif mq==4
    flow_colormap = z_m;
else
    flow_colormap = z_velocity;
end

%flow_colormap =zWaterColorsMalpasset;
topo_colormap =zLandColorsMalpasset;



% or for non default colormaps for the water
% set flowcolormatrix to any colormap desired (ie any m by 3 rgb matrix)
%[flowcolormatrix,ncolors]=deacolor;
%[ncolors,n]=size(flowcolormatrix);
%flow_colormap=[linspace(-TsAmp,TsAmp,ncolors)',flowcolormatrix];

