	
axis off;

campos= [5.6438e+04 -1.1030e+04 9.8101e+03];
camtarg = [3.9744e+03 -3.1134 1.0540e+03];

%camtarg=[300,0,500];
%campos = camtarg + [3000,500,2500];
camang = [5];



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
     'Projection' , 'orthographic')
%     'Position' , [0.13 0.11 0.775 0.815], ...
%     'XLim' , [598000 602000], ...
%     'YLim' , [4.884e+06 4.889e+06], ...
%     'ZLim' , [2228.74-1000 3155.71])%, ...
%     %'View' , [11 24])
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
   
