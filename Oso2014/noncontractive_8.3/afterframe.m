%use this routine to set axis properties and whatever else you wish to the
%plot

%zoom choices


% top view
%set(gca,'PlotBoxAspectRatio',[1 1 1],'DataAspectRatio',[1 1.2 .5])
%axis off

%for 3d type view
set(gca,'FontSize',16);
%sourceview_gca;
axis equal
%axis([424300,425000,143000,143550,0,900])
axis([4.2420e5    4.2510e5    1.4270e5    1.4360e5 0 900])
%view(10,30)
%view(10,90)
view(2)
%axis off;

tstr = ['t = ',num2str(t-10), ' s'];
text(4.25e5,1.436e5 +40,tstr,'fontsize',26);

%axis off;
%to call makeframejpg which makes a jpeg of the plot uncomment next line
%makeframepng


%plotgaugelocations

%set(gca,aba)