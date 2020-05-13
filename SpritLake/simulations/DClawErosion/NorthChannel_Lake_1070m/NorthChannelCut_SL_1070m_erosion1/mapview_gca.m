

xll = 5.99e5;
yll = 4.885e6;

x0d = 599793.125-80;
y0d = 4885536.223+30;
z0d = 7900.0*0.3048+500;

if mview==1

	xL = xll;
	yL = yll;
	xR = xL + 8.e3;
	yT = yL + 7.e3;

	xtext = xL + 500.;
	ytext = yT - 1000.;

%h = scalebar()
	
end

if mview==2

	xL = xll +7.e3;
	xR = xL + 8.e3;
	yL = yll + 6.e3;
	yT = yL + 7.e3;

	xtext = xL + 500.;
	ytext = yT - 1000.;

	img = scalebar1mi;
	leng = 5280.*.3048*1.2;
end

if mview==3

	xL = xll ;
	xR = xL + 18.e3;
	yL = yll ;
	yT = yL + 18.e3;

	xtext = xL + 500.;
	ytext = yT - 1000.;
	PlotGrid=[1 0 0];

	img = scalebar4k;
	leng = 5000.;
	
end

tstr = ['t = ',num2str(t), ' s'];
text(xtext,ytext,z0d,tstr,'fontsize',26);

% top view
view(0,90)
set(gca,'PlotBoxAspectRatio',[1 1 1],'DataAspectRatio',[1 1 1])
axis off
axis([xL,xR,yL,yT])

sz = size(img);
height = leng*sz(1)/sz(2);
[xImage,yImage] =meshgrid([xR-leng-100,xR-100],[yL+100, yL+100+height]);
yImage = flipud(yImage);
zImage = [2.5e3, 2.5e3; 2.5e3, 2.5e3];
hold on;
surf(xImage,yImage,zImage, 'Cdata', img, 'FaceColor','texturemap')
