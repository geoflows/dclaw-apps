
xll = 5.60703e5 - 5.e3;
xur = 5.71420e5;
yll = 5.121002e6 - 2.e3;
yur = 5.129321e6;

x1=xll;
x2=xur;
y1=yll;
y2=yur;
axis([x1,x2,y1,y2]);
axis off;
set(gca,'DataAspectRatio',[1 1 1])

hold on;
xs = x1+2.e2;
xe = xs+1.e3;
ys = y1+3.e2;
line([xs,xe],[ys,ys],[8e3,8e3],'linewidth',4,'color','k')
tstr = ['1 km'];
text((xs+xe)/2.0 -6.5e2,ys+ 5e2,8e3,tstr,'fontsize',26);

hours = floor(t/3600.);
minutes = floor((t-3600*hours)/60.);
seconds = t-3600*hours - 60*minutes;
secondsstr=sprintf('%0.0f',seconds + 100);
hoursstr = sprintf('%0.0f', hours + 100);
minutesstr = sprintf('%0.0f',minutes + 100);
tstr = ['t = ',hoursstr(2:end),':',minutesstr(2:end),':',secondsstr(2:end)];
%tstr = ['t = ',num2str(t-0*10), ' s'];
text(xs,y2-2.e3,8e3,tstr,'fontsize',26);
%axis equal;


