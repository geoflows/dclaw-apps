
%use this routine to set axis properties and whatever else you wish to the
%plot

set(gca,'FontSize',16);

% overhead/map view with labeling
%runoutview_gca;

%oblique (3D) perspective (uncomment the following):
%sourceview_gca
%axis off


camlight left
lighting gouraud
material dull

% add a colorbar. 
hcbar = colorbar_discrete(flow_colormap,hsurf.Parent);

%Choose labeling for variable set in setplot2
%ylabel(hcbar,'surface elevation (m)');
%ylabel(hcbar,'solid fraction')
%ylabel(hcbar,'fluid pressure ratio')
ylabel(hcbar,'flow depth (m)')

%ticklabels={'< -0.1','0','0.1 to 0.5','0.5 to 1','1 to 2','2 to 5','5 to 10','> 10'};
%ticklabels={'< 0','0','0.1 to 0.2','0.2 to 0.4','0.4 to 0.6','0.6 to 0.8','0.8 to 1.0','1.0 to 2.0','> 2.0'};
%ticklabels={'< 0.1','0.1 to 0.2','0.2 to 0.3','0.3 to 0.4','0.4 to 0.5','0.5 to 0.6','> 0.6'};
%ticklabels={'0 to 0.01','0.01 to 0.2','0.2 to 0.4','0.4 to 0.6','0.6 to 0.8','0.8 to 1.0'};
%set(hcbar,'TickLabels',ticklabels);
set(hcbar,'FontSize',18);
%set(hcbar,'Location','westoutside');
%set(hcbar,'Location','southoutside');


% to make png of each frame uncomment the following:
%makeframepng
