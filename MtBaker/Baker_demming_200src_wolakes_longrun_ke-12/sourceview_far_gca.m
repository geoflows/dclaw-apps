	

camtarg=[5.868e5,5.4031e6,2600]+[-1000,+500,-5400];
r = 5000.0;
rang = deg2rad*(180.0+45);
campos =camtarg + [r*cos(rang),r*sin(rang),r*sin(85*deg2rad)];
camang = [135];



set(gca, ...
     'CameraPosition' , campos , ...
     'CameraPositionMode' , 'manual', ...
     'CameraTarget' , camtarg , ...
     'CameraTargetMode' , 'manual', ...
     'CameraUpVector' , [0 0 1], ...
 	 'CameraUpVectorMode' , 'auto', ...
 	 'CameraViewAngle' , camang, ...
 	 'CameraViewAngleMode' , 'manual', ...
     'DataAspectRatio' , [1 1 1], ...
     'OuterPosition' , [0 0 1 1], ...
     'PlotBoxAspectRatio' , [1 1 1], ...
     'PlotBoxAspectRatioMode' , 'manual', ...
     'Projection' , 'perspective', ...
     'XLim' , [5.74e5,5.92e5], ...
     'YLim' , [5.39e6,5.406e6], ...
     'ZLim' , [0.,4000], ...
     'Position' , [0.13 0.11 0.775 0.815])%, ...

xs = camtarg(1) + 0.3*(campos(1)-camtarg(1))-5000;
ys = camtarg(2)+ 0.3*(campos(2)-camtarg(2)) +5000;
zs = camtarg(3)+ 5500;
hours = floor(t/3600.);
minutes = floor((t-3600*hours)/60.);
seconds = t-3600*hours - 60*minutes;
secondsstr=sprintf('%0.0f',seconds + 100);
hoursstr = sprintf('%0.0f', hours + 100);
minutesstr = sprintf('%0.0f',minutes + 100);
tstr = ['t = ',hoursstr(2:end),':',minutesstr(2:end),':',secondsstr(2:end)];
%tstr = ['t = ',num2str(t-0*10), ' s'];
text(xs,ys,zs,tstr,'fontsize',26);
axis off;