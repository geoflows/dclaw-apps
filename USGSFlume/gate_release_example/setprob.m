
% This routine is called after setplot2.m by plotclaw2.
%
% Set some additional things for plotting D-Claw/GeoClaw output.
%

%PlotType = 11;     % = 11 for colored surface plot
                   % = 12 for contour plot
quiverplot=0;
PlotFlow = 1;      % plot the surface of the flow
PlotTopo = 1;      % plot the topography
ContourValues = linspace(-1,1,21);
topoContourValues = 30;   % Contour levels for topo.
                          % Set to either a scalar or vector


discrete_colormap=1;
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

zLandColorsMalpassetZoom = [   1200  DarkGreen;
                           1400  Green;
                           1550  LightGreen;
                           1600  Brown;
                           2000 Tan;
                           2800 White;
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
                10.0 Red];

z_velocity2 = [ -1 Blue;
                0 White;
                1. Red];

z_depth = [0. White;
           10.0 LightBlue;
           20.0 Blue];
       
z_eta= [364-2. Blue;
           364 White;
           364+2. Red];
       
lse = 364.;
zcm = jet(12);
tse = [-5,-2,-1,-0.1,.1,1,2,5,20]+lse;
Zcm = [zcm(1:4,:);White;zcm(end-3:end,:)];
z_eta = [tse',Zcm];

lse = 364.;
zcm = jet(16);
%tse = [-0.1,.1,0.5,1,2,5,10,20]+lse;
tse = [-.5,0.1,.2,0.4,0.6,0.8,1.0,2.0,20]+lse;
Zcm = [zcm(4,:);White;zcm(end-6:end,:)];
z_eta = [tse',Zcm];



z_m = [0.0 Blue;
        0.5 White;
            1.0 Red];
        
zcm = jet(8);
tse = [.1,.2,.3,.4,.5,.6,1];
%tse = [1.1,1.2,1.3,1.4,1.5,1.6,11];
Zcm = [zcm(1:6,:);.42,.167,.03];
z_m = [tse',Zcm];

z_m_brown = [0.0 0.2,0.2,0.7;
        0.35 White;
            0.7 .42,.167,.03];
        
%        z_m_brown = [.60 Blue;
%        0.62 Red;
%            0.64 Blue];

 zDigPressure = [-1 Red;
                0  White;
                10/18.5  LightBlue;
                1  Blue];
            
zcm = flipud(winter(5));
tse = [0.1,.2,.4,.6,.8,1];
nc = length(tse)-2;
Zcm = [White;zcm(end-nc:end,:)];
zDigPressure = [tse',Zcm];

zcm = flipud(hot(8));
%tse = [0.1,.25,1.,2,10,50,100,500];
tse = [.01,.05,0.1,0.2,0.5,1.0,2.0,500];
nc = length(tse)-2;
Zcm = [White;zcm(end-nc:end,:)];
z_depth = [tse',Zcm];

           zLandColorsMalpasset = [   0  DarkGreen;
                           200  Green;
                           400  LightGreen;
                           600  Tan;
                           800 Brown;
                           1000 White];

           zWaterColorsMalpasset = [-5  DarkBlue;
                          0 White;
                         5 Red];

if mq==6
    flow_colormap = z_velocity;
elseif mq==5
    flow_colormap =zDigPressure;
elseif mq == 1
    flow_colormap = z_depth;
elseif mq==4
    flow_colormap = z_m;
elseif mq==2
    flow_colormap = z_velocity2;
else
    flow_colormap = z_eta;
end

%flow_colormap =zWaterColorsMalpasset;
%topo_colormap =zLandColorsMalpassetZoom;
topo_colormap = [ 0 Gray8;
                10000. Gray8];


% or for non default colormaps for the water
% set flowcolormatrix to any colormap desired (ie any m by 3 rgb matrix)
%[flowcolormatrix,ncolors]=deacolor;
%[ncolors,n]=size(flowcolormatrix);
%flow_colormap=[linspace(-TsAmp,TsAmp,ncolors)',flowcolormatrix];

