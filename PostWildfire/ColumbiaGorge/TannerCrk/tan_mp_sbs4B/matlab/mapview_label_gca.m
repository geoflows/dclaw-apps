
x1=5.805e5;
x2=5.825e5+500;
y1=5.052e6-1300;
y2=5.054e6;
axis([x1,x2,y1,y2]);
axis off;
set(gca,'DataAspectRatio',[1 1 1])

hold on;
xs = x1+0.1e3;
xe = xs+1.0e3;
ys = y1+300;
line([xs,xe],[ys,ys],[8e3,8e3],'linewidth',4,'color','k')
tstr = ['1 km'];
text((xs+xe)/2.0 -0.15e3,ys+0.1e3,8e3,tstr,'fontsize',26);


hours = floor(t/3600.);
minutes = floor((t-3600*hours)/60.);
seconds = t-3600*hours - 60*minutes;
secondsstr=sprintf('%0.0f',seconds + 100);
hoursstr = sprintf('%0.0f', hours + 100);
minutesstr = sprintf('%0.0f',minutes + 100);
tstr = ['t = ',hoursstr(2:end),':',minutesstr(2:end),':',secondsstr(2:end)];
%tstr = ['t = ',num2str(t-0*10), ' s'];
text(xs+.0e3,ys+.4e3,8e3,tstr,'fontsize',26);
%axis equal;


