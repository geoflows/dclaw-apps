x1=592803.601535;           
x2=595670.4930767842;     
y1=5325333.86647;        
y2=5327098.903808075;  
%x1=5.55e5;
%x2=6.07e5;
%y1=5.37e6;
%y2=5.414e6;
axis([x1,x2,y1,y2]);
axis off;
set(gca,'DataAspectRatio',[1 1 1])

hold on;
xs = x1+1.e2;
xe = xs+500.;
ys = y1+0.5e2;
line([xs,xe],[ys,ys],[8e3,8e3],'linewidth',4,'color','k')
tstr = ['500 m'];
text(xs+0.25*(xe-xs),ys+ 100.,8e3,tstr,'fontsize',26);

hours = floor(t/3600.);
minutes = floor((t-3600*hours)/60.);
seconds = t-3600*hours - 60*minutes;
secondsstr=sprintf('%0.0f',seconds + 100);
hoursstr = sprintf('%0.0f', hours + 100);
minutesstr = sprintf('%0.0f',minutes + 100);
tstr = ['t = ',hoursstr(2:end),':',minutesstr(2:end),':',secondsstr(2:end)];
%tstr = ['t = ',num2str(t-0*10), ' s'];
text(xs,ys+1.5e3,8e3,tstr,'fontsize',26);
%axis equal;


