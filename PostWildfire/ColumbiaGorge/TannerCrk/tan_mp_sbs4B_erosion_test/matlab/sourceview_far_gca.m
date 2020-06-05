cp=2000;
campos = [5.9e5,5.1902e6,4200.]+[0,-3000,00];
camtarg = [5.93e5,5.1902e6,4200.]+[0,0,-cp];
set(gca, ...
     'CameraPosition' , campos , ...
     'CameraPositionMode' , 'manual', ...
     'CameraTarget' , camtarg , ...
     'CameraTargetMode' , 'manual', ...
     'CameraUpVector' , [0 0 1], ...
 	 'CameraUpVectorMode' , 'auto', ...
 	 'CameraViewAngle' , [75], ...
 	 'CameraViewAngleMode' , 'manual', ...
     'DataAspectRatio' , [1 1 1], ...
     'OuterPosition' , [0 0 1 1], ...
     'PlotBoxAspectRatio' , [5.37356 4.56752 1], ...
     'PlotBoxAspectRatioMode' , 'manual', ...
     'Projection' , 'perspective', ...
     'Position' , [0.13 0.11 0.775 0.815])
 
xs = camtarg(1);
ys = camtarg(2);
zs = camtarg(3);
hours = floor(t/3600.);
minutes = floor((t-3600*hours)/60.);
seconds = t-3600*hours - 60*minutes;
secondsstr=sprintf('%0.0f',seconds + 100);
hoursstr = sprintf('%0.0f', hours + 100);
minutesstr = sprintf('%0.0f',minutes + 100);
tstr = ['t = ',hoursstr(2:end),':',minutesstr(2:end),':',secondsstr(2:end)];
%tstr = ['t = ',num2str(t-0*10), ' s'];
text(xs,ys-1000,zs+500+cp,tstr,'fontsize',26);

     %'XLim' , [599374 600014], ...
     %'YLim' , [4.88513e+06 4.88568e+06], ...
     %'ZLim' , [2337.61 2456.71])%, ...
     %'View' , [11 24])
% 	CLim , [0 1]
% 	CLimMode , auto, ...
% 	Color , [1 1 1], ...
% 	CurrentPoint , [ (2 by 3) double array]
% 	ColorOrder , [ (7 by 3) double array]
% 	DataAspectRatioMode , manual, ...
% 	DrawMode , normal
% 	FontAngle , normal
% 	FontName , Helvetica
% 	FontSize , [10]
% 	FontUnits , points
% 	FontWeight , normal
% 	GridLineStyle , :
% 	Layer , bottom
% 	LineStyleOrder , -
% 	LineWidth , [0.5]
% 	MinorGridLineStyle , :
% 	NextPlot , replace

% 	TickLength , [0.01 0.025]
% 	TickDir , out
% 	TickDirMode , auto
% 	TightInset , [0 0 0 0]
% 	Title , [163.006]
% 	Units , normalized

% 	XColor , [0 0 0]
% 	XDir , normal
% 	XGrid , off
% 	XLabel , [168.007]
% 	XAxisLocation , bottom

%  	'XLimMode' , 'manual', ...
% 	XMinorGrid , off
% 	XMinorTick , off
 %	'XScale' , 'linear')%, ...
% 	XTick , [954000 955000 956000 957000 958000 959000]
% 	XTickLabel , 
% 		9.54
% 		9.55
% 		9.56
% 		9.57
% 		9.58
% 		9.59
% 	XTickLabelMode , auto
% 	XTickMode , auto
% 	YColor , [0 0 0]
% 	YDir , normal
% 	YGrid , off
% 	YLabel , [169.007]
% 	YAxisLocation , left
 %	
% 	YLimMode , manual
% 	YMinorGrid , off
% 	YMinorTick , off
% 	YScale , linear
% 	YTick , [ (1 by 8) double array]
% 	YTickLabel , 
% 		1.834
% 		1.836
% 		1.838
% 		1.84 
% 		1.842
% 		1.844
% 		1.846
% 		1.848
% 	YTickLabelMode , auto
% 	YTickMode , auto
% 	ZColor , [0 0 0]
% 	ZDir , normal
% 	ZGrid , off
% 	ZLabel , [170.007]
% 	
% 	'ZLimMode' , 'manual', ...
% 	ZMinorGrid , off
% 	ZMinorTick , off
 %	'ZScale' , 'linear', ...
% 	ZTick , [ (1 by 8) double array]
% 	ZTickLabel , 
% 		-50
% 		0  
% 		50 
% 		100
% 		150
% 		200
% 		250
% 		300
% 	ZTickLabelMode , auto
% 	ZTickMode , auto
% 
% 	BeingDeleted , off
% 	ButtonDownFcn , 
% 	Children , [ (4 by 1) double array]
 %	'Clipping' , 'on', ...
% 	CreateFcn , 
% 	DeleteFcn , 
% 	BusyAction , queue
% 	HandleVisibility , on
% 	HitTest , on
% 	Interruptible , on
% 	Parent , [1]
% 	Selected , off
% 	SelectionHighlight , on
% 	Tag , 
% 	Type , axes
% 	UIContextMenu , []
% 	UserData , []
%'Visible' , 'off'
%)
   
