%use this routine to set axis properties and whatever else you wish to the
%plot

%zoom choices

%axis equal

% top view
%set(gca,'DataAspectRatio',[1 1 1])
%view(89,10)
%axis off
%view(2)
view(2);
axis on
%axis([-4,4,-1,3])
%axis([69,115,-2,4]);axis equal


%for 3d type view
%set(gca,'PlotBoxAspectRatio',[1 1 1],'DataAspectRatio',[1 1.2 .5])
%set(gca,'CameraViewAngle',get(gca,'CameraViewAngle')-3)
%hopperview_bn_gca
runoutview_gca

%midview_gca
%baseview_bn_gca
%view(2)

%tstr = ['t = ',num2str(t-4)];
%text(1,-4,tstr,'fontsize',42);


%to call makeframejpg which makes a jpeg of the plot uncomment next line
%makeframepng

%plotgaugelocations

%set(gca,aba)