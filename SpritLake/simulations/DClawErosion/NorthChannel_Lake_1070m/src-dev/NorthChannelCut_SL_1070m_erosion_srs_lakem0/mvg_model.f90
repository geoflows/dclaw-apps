!--------------------------------------------------------------------------------------------
!
!              MVG model for unsaturated soil pressure
!                    Written by Colton J. Conroy
!                             @ APAM
!                        Columbia University
!                             3.5.20
!
!
!   sm : soil moisture content
!    h : pressure head in cm
!  sms : saturated soil moisture content (cm^3/cm^3)
!  smr : residual soil moisture content (cm^3/cm^3)
! alpha: inverse of air entry pressure
!    m : porosity parameter
!    n : binomial distribution coefficent (a function of m)
!   Se : percent saturation
!   Note: pressure head is controlled by the minimum statistic in
!         terms of pore size distribution. For details see,
!  M.Th. van Genuchten, A Closed-form Equation for Predicting the Hydraulic Conductivity of Unsaturated Soils, Soil Sci. Soc. Am. J., 44 pp.892-898, 1980.
!
!-------------------------------------------------------------------------------------------
subroutine mvg_model(sm,h,sms,smr,alpha,m,Se)

implicit none

double precision :: sm, sms, smr, alpha
double precision :: n, m, Se, h
double precision, parameter :: cmin = 1.0d-6

n    = (1.0d0/(1.0d0-m))
Se   = (sm - smr)/(sms - smr);
if (Se > 1.0d0) then
    Se = 1.0d0
endif
if (Se <= 0.0d0) then
    Se = cmin
endif
h = -1.0d0/alpha*((1.0d0/Se)**(1.0d0/m)-1.0d0)**(1.0d0/n)


return
end subroutine mvg_model
