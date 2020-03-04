%use this routine to set axis properties and whatever else you wish to the
%plot

%zoom choices
%zoom choices


% top view
%set(gca,'PlotBoxAspectRatio',[1 1 1],'DataAspectRatio',[1 1 1])
%axis off

%for 3d type view
set(gca,'FontSize',16);

%axis off
%slideview_gca;
%camproj('perspective')
%mapview_label_gca;
mapview_larger_label_gca;
%damview2_gca;
%sourceview_radial_gca;
%lakeview_gca;
camlight left
lighting gouraud
material dull
hcbar = colorbar_discrete(flow_colormap,hsurf.Parent);
%ylabel(hcbar,'surface elevation (m)');
ylabel(hcbar,'solid fraction')
%ylabel(hcbar,'fluid pressure ratio')
%ylabel(hcbar,'flow depth (m)')

%ticklabels={'< -0.1','0','0.1 to 0.5','0.5 to 1','1 to 2','2 to 5','5 to 10','> 10'};
%ticklabels={'< 0','0','0.1 to 0.2','0.2 to 0.4','0.4 to 0.6','0.6 to 0.8','0.8 to 1.0','1.0 to 2.0','> 2.0'};
%ticklabels={'< 0.1','0.1 to 0.2','0.2 to 0.3','0.3 to 0.4','0.4 to 0.5','0.5 to 0.6','> 0.6'};
%ticklabels={'0 to 0.01','0.01 to 0.2','0.2 to 0.4','0.4 to 0.6','0.6 to 0.8','0.8 to 1.0'};
%set(hcbar,'TickLabels',ticklabels);
set(hcbar,'FontSize',18);
%set(hcbar,'Location','westoutside');
%set(hcbar,'Location','southoutside');

%damview_gca;
%sourceview2_gca;
%camproj('perspective')
%axis off
%axis equal
%axis tight
%axis([424300,425000,143000,143550,0,900])
%axis([4.2420e5    4.2510e5    1.4270e5    1.4360e5 0 900])
%view(10,30)
%view(10,90)
%view(2)
%axis off;

%tstr = ['t = ',num2str(t-0*10), ' s'];
%text(4.25e5,1.436e5 +40,tstr,'fontsize',26);

%axis off;
%to call makeframejpg which makes a jpeg of the plot uncomment next line
%plotgaugelocations
%makeframepng




%set(gca,aba)