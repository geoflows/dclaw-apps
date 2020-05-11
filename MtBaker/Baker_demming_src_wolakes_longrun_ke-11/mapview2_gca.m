
x1=5.55e5-10.e3;
x2=5.95e5;
y1=5.176e6-.5e3;
y2=5.21e6+5e3+10e3;
axis([x1,x2,y1,y2]);
axis off;
set(gca,'DataAspectRatio',[1 1 1])

hold on;
xs = (x1+x2)/2.0 + 8e3;
xe = xs+10e3;
ys = y2-3e3;
line([xs,xe],[ys,ys],[8e3,8e3],'linewidth',6,'color','k')
tstr = ['10 km'];
text((xs+xe)/2.0 -2.0e3,ys+1e3,8e3,tstr,'fontsize',26);


hours = floor(t/3600.);
minutes = floor((t-3600*hours)/60.);
seconds = t-3600*hours - 60*minutes;
secondsstr=sprintf('%0.0f',seconds + 100);
hoursstr = sprintf('%0.0f', hours + 100);
minutesstr = sprintf('%0.0f',minutes + 100);
tstr = ['t = ',hoursstr(2:end),':',minutesstr(2:end),':',secondsstr(2:end)];
%tstr = ['t = ',num2str(t-0*10), ' s'];
text(xs,ys-3e3,8e3,tstr,'fontsize',26);
%axis equal;