%use this routine to set axis properties and whatever else you wish to the
%plot

%zoom choices


% top view
%set(gca,'PlotBoxAspectRatio',[1 1 1],'DataAspectRatio',[1 1.2 .5])
%axis off
set(gca,'FontSize',16);

%sourceview_radial_gca;
%mapview_channelcut_label_gca;
mapview_domain_label_gca;
camlight left
lighting gouraud
material dull

hcbar = colorbar_discrete(flow_colormap,hsurf.Parent);
set(hcbar,'FontSize',12)
ylabel(hcbar,'flow depth (m)');

%ylabel(hcbar,'surface elevation (m)');

%axis([5.2e5,5.8e5,1.28e6,1.32e6]) %the grid dam
%axis equal;
%axis off;
%to call makeframejpg which makes a jpeg of the plot uncomment next line
%plotgaugelocations
makeframepng
%axis([.87e6,.9e6,1.55e6,1.6e6,0,10000])


%set(gca,aba)