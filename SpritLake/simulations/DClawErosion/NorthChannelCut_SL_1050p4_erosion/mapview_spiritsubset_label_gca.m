
xll = 4.94107e5;
xur = 5.73137e5;
yll = 5.098310e6;
yur = 5.140460e6;

x1=5.55e5-15.e3;
x2=6.07e5;
y1=5.37e6;
y2=5.414e6+15.e3;
axis([x1,x2,y1,y2]);
axis off;
set(gca,'DataAspectRatio',[1 1 1])

hold on;
xs = x1+1.e3;
xe = xs+10.e3;
ys = y1+1.e3;
line([xs,xe],[ys,ys],[8e3,8e3],'linewidth',4,'color','k')
tstr = ['10 km'];
text((xs+xe)/2.0 -3.5e3,ys+2.6e3,8e3,tstr,'fontsize',26);

hours = floor(t/3600.);
minutes = floor((t-3600*hours)/60.);
seconds = t-3600*hours - 60*minutes;
secondsstr=sprintf('%0.0f',seconds + 100);
hoursstr = sprintf('%0.0f', hours + 100);
minutesstr = sprintf('%0.0f',minutes + 100);
tstr = ['t = ',hoursstr(2:end),':',minutesstr(2:end),':',secondsstr(2:end)];
%tstr = ['t = ',num2str(t-0*10), ' s'];
text(xs,ys+7.5e3,8e3,tstr,'fontsize',26);
%axis equal;


