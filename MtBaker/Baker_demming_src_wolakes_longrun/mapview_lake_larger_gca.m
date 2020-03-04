
x1=5.84e5-5e3;
x2=6.06e5;
y1=5.375e6-5e3;
y2=5.405e6;
axis([x1,x2,y1,y2]);
axis off;
set(gca,'DataAspectRatio',[1 1 1])

hold on;
xs = x1+13.e3;
xe = xs+5.e3;
ys = y1+1.e3;
line([xs,xe],[ys,ys],[8e3,8e3],'linewidth',4,'color','k')
tstr = ['5 km'];
text((xs+xe)/2.0 -1.8e3,ys+0.8e3,8e3,tstr,'fontsize',26);

hours = floor(t/3600.);
minutes = floor((t-3600*hours)/60.);
seconds = t-3600*hours - 60*minutes;
secondsstr=sprintf('%0.0f',seconds + 100);
hoursstr = sprintf('%0.0f', hours + 100);
minutesstr = sprintf('%0.0f',minutes + 100);
tstr = ['t = ',hoursstr(2:end),':',minutesstr(2:end),':',secondsstr(2:end)];
%tstr = ['t = ',num2str(t-0*10), ' s'];
text(xs,y2-4.5e3,8e3,tstr,'fontsize',26);
%axis equal;


