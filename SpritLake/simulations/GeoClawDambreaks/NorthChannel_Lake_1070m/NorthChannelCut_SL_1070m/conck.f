c
c -----------------------------------------------------------
c
      subroutine conck(level, nvar, time, rest)
c
      implicit double precision (a-h,o-z)

      include  "call.i"
      logical  rest

      iadd(i,j,ivar)  = loc + i - 1 + mitot*((ivar-1)*mjtot+j-1)
      iaddaux(i,j,iaux) = locaux + i - 1 + mitot*((iaux-1)*mjtot+j-1)
c
c ******************************************************************
c conck - conservation check  for specified level
c         mostly a debugging tool
c         this assumes grids don't overlap
c ******************************************************************
c
c
c  grid loop for given level
c
      hx      = hxposs(level)
      hy      = hyposs(level)
      dt      = possk(level)
      totmass = 0.d0
      totvol  = 0.d0
      totarea = 0.d0
      totkinetic = 0.0
      centermassx = 0.0
      centermassy = 0.0
      totpotential = 0.0
      totwork = 0.0
      grav = 9.81
      F_x = 0.0
      F_y = 0.0
      F_z = 0.0


      mptr = lstart(level)
 20   if (mptr .eq. 0) go to 85
         loc    = node(store1,mptr)
         locaux = node(storeaux,mptr)
         nx     = node(ndihi,mptr) - node(ndilo,mptr) + 1
         ny     = node(ndjhi,mptr) - node(ndjlo,mptr) + 1
         mitot  = nx + 2*nghost
         mjtot  = ny + 2*nghost
         xlow   = rnode(cornxlo,mptr)
         ylow   = rnode(cornylo,mptr)
         xhi    = rnode(cornxhi,mptr)
         yhi    = rnode(cornyhi,mptr)
c
         if (mcapa .eq. 0) then
           do 50 j  = nghost+1, mjtot-nghost
           do 50 i  = nghost+1, mitot-nghost
              x = xlow + (i-0.5)*hx
              y = ylow + (j-0.5)*hy
              if (dabs(alloc(iadd(i,j,1))).gt.1.d-3) then
                  depth = alloc(iadd(i,j,1))
                  topo = alloc(iaddaux(i,j,1)) - 70.0
                  sv = alloc(iadd(i,j,4))/alloc(iadd(i,j,1))
                  rho = 1000.d0*(1.d0-sv) + 2700.d0*sv
                  hvnorm =
     &              sqrt(alloc(iadd(i,j,2))**2 + alloc(iadd(i,j,3))**2)
                  totpotential = totpotential +
     &                  0.5*grav*rho*depth*(depth+2.0*topo)
                  totwork = totwork + rho*grav*hvnorm
                  totmass = totmass + rho*alloc(iadd(i,j,1))
                  centermassx = centermassx+rho*alloc(iadd(i,j,1))*x
                  centermassy = centermassy+rho*alloc(iadd(i,j,1))*y
                  totarea = totarea + hx*hy
                  totkinetic = totkinetic + rho*0.5*
     &               (alloc(iadd(i,j,2))**2 + alloc(iadd(i,j,3))**2)
     &                  /alloc(iadd(i,j,1))

c             !=========begin ==========================================
                  vu = (alloc(iadd(i,j,2)))/depth
                  vv = (alloc(iadd(i,j,3)))/depth
                  if ((vu**2+vv*2).le.0.0) cycle
                  b_x =(alloc(iaddaux(i+1,j,1))
     &                  -alloc(iaddaux(i-1,j,1)))/(2.d0*hx)
                  b_y =(alloc(iaddaux(i,j+1,1))
     &                  -alloc(iaddaux(i,j-1,1)))/(2.d0*hy)

                  b_xx=(alloc(iaddaux(i+1,j,1))-2.d0*alloc(iaddaux
     &                     (i,j,1))+alloc(iaddaux(i-1,j,1)))/(hx**2)
                  b_yy=(alloc(iaddaux(i,j+1,1))-2.d0*alloc(iaddaux
     &                     (i,j,1))+alloc(iaddaux(i,j-1,1)))/(hy**2)
                  b_xy= (alloc(iaddaux(i+1,j+1,1))
     &                  -alloc(iaddaux(i-1,j+1,1))
     &                  -alloc(iaddaux(i+1,j-1,1))
     &                  +alloc(iaddaux(i-1,j-1,1)))/(4.0*hx*hy)

                  c = 1.d0/dsqrt(b_x**2 + b_y**2 + 1.d0)
                  un_x = -c*b_x
                  un_y = -c*b_y
                  un_z = c
                  alpha = 1.0/dsqrt(vu**2+vv**2+(vu*b_x+vv*b_y)**2)
                  t_x = alpha*vu
                  t_y = alpha*vv
                  t_z = alpha*(vu*b_x + vv*b_y)
                  if ((b_x**2+b_y*2).gt.0.0) then
                  alpha = 1.0/dsqrt(b_x**2+b_y**2+(b_x**2+b_y**2)**2)
                  else
                  alpha = 0.0
                  endif
                  d_x = -alpha*b_x
                  d_y = -alpha*b_y
                  d_z = -alpha*(b_x**2 + b_y**2)
                  sina = alpha*(b_x**2 + b_y**2)
                  chi = (vu**2*b_xx + vv**2*b_yy + 2.0*vu*vv*b_xy)/grav
                  chi = max(chi,-1.0)

                  phi = alloc(iaddaux(i,j,4))
                  rgh = rho*grav*depth
                  gamma = alloc(iadd(i,j,5))/rgh

                  F_x = F_x + c*rgh*chi*un_x
                  F_y = F_y + c*rgh*chi*un_y
                  F_z = F_z + c*rgh*chi*un_z

                  shearmag = -c*rgh*(1.0+chi)*max(0.0,(1.0-gamma))
     &                                                   *dtan(phi)
                  F_x = F_x + shearmag*t_x
                  F_y = F_y + shearmag*t_y
                  F_z = F_z + shearmag*t_z

                  F_x = F_x + sina*rgh*d_x
                  F_y = F_y + sina*rgh*d_y
                  F_z = F_z + sina*rgh*d_z


cc             !=========end ============================================
              endif
              totvol = totvol + alloc(iadd(i,j,1))
 50           continue
          else
c          # with capa array:

          endif
c
       mptr = node(levelptr,mptr)
       go to 20
c
 85    totmass = totmass * hx * hy
 86    totvol = totvol * hx * hy
       totkinetic = totkinetic*hx*hy
       totpotential = totpotential*hx*hy
       totwork = totwork*hx*hy
       centermassx = hx*hy*centermassx/totmass
       centermassy = hx*hy*centermassy/totmass
       F_x = F_x*hx*hy
       F_y = F_y*hx*hy
       F_z = F_z*hx*hy
       if (time.eq.tstart .and. (level.eq.1) .and. .not. rest) then
           tmass0 = totmass
           tvol0 = totvol
           totarea0 = totarea
           write(6,*) 'Total mass at initial time: ',tmass0
           write(6,*) 'Total volume at initial time: ',tvol0
           write(6,*) 'Total area at initial time: ',totarea0
       endif

       if (level.eq.3) then
       write(outunit,777) time, totmass, 100.0*(totmass-tmass0)/tmass0
       write(outunit,778) time, totvol, 100.0*(totvol-tvol0)/tvol0
       write(outunit,779) time, totarea
       write(outunit,780) time, totkinetic
       write(outunit,781) time, centermassx,centermassy
       write(outunit,782) time, totpotential,totwork
       write(outunit,783) time, F_x,F_y,F_z
       endif
 777   format('time t = ',e12.5,'  total mass = ',e22.15, ' diff % = ',
     &         e11.4)
 778   format('time t = ',e12.5,'  total vol = ',e22.15, '  diff % = ',
     &         e11.4)
 779   format('time t = ',e12.5,'  total area = ',e22.15)
 780   format('time t = ',e12.5,'  total kinetic = ',e22.15)
 781   format('time t = ',e12.5,'  center of mass = ',e22.15,e22.15)
 782   format('time t = ',e12.5,'  total potential work = ',e22.15,
     &            e22.15)
 783   format('time t = ',e12.5,'  F_net = ',e22.14,e22.14,e22.14)
c
 99   return
      end
