


view(2);axis fill;axis equal
light 
lighting gouraud
material dull

xll = 4.94107e5;
xur = 5.73137e5;
yll = 5.098310e6;
yur = 5.140460e6;

axis([xll,xur,yll,yur]);

xt = 9.5e5-1e5;
yt = 1.15e6;
hours = floor(t/3600.);
minutes = floor((t-3600*hours)/60.);
hoursstr = sprintf('%0.0f', hours + 1000);
minutesstr = sprintf('%0.2f',minutes + 100);
tstr = ['t = ',hoursstr(2:end),' : ',minutesstr(2:end)];
text(xt,yt,3000.,tstr,'fontsize',16);

xt = 9.5e5-1e5;
yt = 1.2e6;
tstr = ['Scenario 3a'];
text(xt,yt,3000.,tstr,'fontsize',16);hold on;

x1 = 4.e5;
y1 = 1.15e6;
xs = x1 + 10.e3;
xe = xs+200e3;
ys = y1 + 10e3;
line([xs,xe],[ys,ys],[8e3,8e3],'linewidth',4,'color','k')
tstr = ['200 km'];
text(xs+50.e3,ys+20.0e3,8e3,tstr,'fontsize',26);

