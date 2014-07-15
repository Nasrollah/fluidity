# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.

solution_dict = {

    "domain_extents" : (1.0, 1.2, 0.8),

    "finish_time" : 1.0,

    "pressure1_scale" : 1.0,

    "saturation2_scale" : 0.1,

    "GRAVITY_MAGNITUDE" : "1.0",

    "VISCOSITY1" : "1.725e-05",

    "VISCOSITY2" : "0.001",

    "DENSITY1" : "1.284",

    "DENSITY2" : "1000.0",

    "POROSITY" : "0.4",

    "ABSOLUTE_PERMEABILITY" : "1.567346939e-09",

    "GRAVITY_DIRECTION_1D" : "1",

    "PRESSURE_1D" : "(0.25*cos(1.0*pi*t) + 0.75)*cos(1.0*pi*X[0])",

    "SATURATION1_1D" : "1 - 0.1*exp(-1.0*X[0])/(1.0*t + 1.)",

    "SATURATION2_1D" : "0.1*exp(-1.0*X[0])/(1.0*t + 1.)",

    "DARCY_VELOCITY1_X_1D" : "-9.0860692115942e-5*(1.0 - 0.117647058823529*exp(-1.0*X[0])/(1.0*t + 1.))**4*(-1.0*pi*(0.25*cos(1.0*pi*t) + 0.75)*sin(1.0*pi*X[0]) - 1.284)",

    "DARCY_VELOCITY1_MAGNITUDE_1D" : "9.0860692115942e-5*((1.0 - 0.117647058823529*exp(-1.0*X[0])/(1.0*t + 1.))**8)**(1/2.)*abs(-1.0*pi*(0.25*cos(1.0*pi*t) + 0.75)*sin(1.0*pi*X[0]) - 1.284)",

    "SOURCE_SATURATION1_1D" : "9.0860692115942e-5*pi**2*(1.0 - 0.117647058823529*exp(-1.0*X[0])/(1.0*t + 1.))**4*(0.25*cos(1.0*pi*t) + 0.75)*cos(1.0*pi*X[0]) - 4.27579727604433e-5*(1.0 - 0.117647058823529*exp(-1.0*X[0])/(1.0*t + 1.))**3*(-1.0*pi*(0.25*cos(1.0*pi*t) + 0.75)*sin(1.0*pi*X[0]) - 1.284)*exp(-1.0*X[0])/(1.0*t + 1.) + 0.04*exp(-1.0*X[0])/(1.0*t + 1.)**2",

    "DARCY_VELOCITY2_X_1D" : "-2.16933832387543e-8*(-1.0*pi*(0.25*cos(1.0*pi*t) + 0.75)*sin(1.0*pi*X[0]) - 1000.0)*(-(1.0 - 0.117647058823529*exp(-1.0*X[0])/(1.0*t + 1.))**2 + 1.)*exp(-2.0*X[0])/(1.0*t + 1.)**2",

    "DARCY_VELOCITY2_MAGNITUDE_1D" : "2.16933832387543e-8*((-(1.0 - 0.117647058823529*exp(-1.0*X[0])/(1.0*t + 1.))**2 + 1.)**2*exp(-4.0*X[0])/(1.0*t + 1.)**4)**(1/2.)*abs(-1.0*pi*(0.25*cos(1.0*pi*t) + 0.75)*sin(1.0*pi*X[0]) - 1000.0)",

    "SOURCE_SATURATION2_1D" : "5.1043254679422e-9*(1.0 - 0.117647058823529*exp(-1.0*X[0])/(1.0*t + 1.))*(-1.0*pi*(0.25*cos(1.0*pi*t) + 0.75)*sin(1.0*pi*X[0]) - 1000.0)*exp(-2.0*X[0])*exp(-1.0*X[0])/(1.0*t + 1.)**3 + 4.33867664775087e-8*(-1.0*pi*(0.25*cos(1.0*pi*t) + 0.75)*sin(1.0*pi*X[0]) - 1000.0)*(-(1.0 - 0.117647058823529*exp(-1.0*X[0])/(1.0*t + 1.))**2 + 1.)*exp(-2.0*X[0])/(1.0*t + 1.)**2 + 2.16933832387543e-8*pi**2*(-(1.0 - 0.117647058823529*exp(-1.0*X[0])/(1.0*t + 1.))**2 + 1.)*(0.25*cos(1.0*pi*t) + 0.75)*exp(-2.0*X[0])*cos(1.0*pi*X[0])/(1.0*t + 1.)**2 - 0.04*exp(-1.0*X[0])/(1.0*t + 1.)**2",

    "GRAVITY_DIRECTION_2D" : "1 0. ",

    "PRESSURE_2D" : "(0.25*cos(1.0*pi*t) + 0.75)*sin(0.833333333333333*pi*X[1])**2*cos(1.0*pi*X[0])",

    "SATURATION1_2D" : "-0.15625*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.",

    "SATURATION2_2D" : "0.15625*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.)",

    "DARCY_VELOCITY1_X_2D" : "-9.0860692115942e-5*(-1.0*pi*(0.25*cos(1.0*pi*t) + 0.75)*sin(1.0*pi*X[0])*sin(0.833333333333333*pi*X[1])**2 - 1.284)*(-0.183823529411765*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**4",

    "DARCY_VELOCITY1_Y_2D" : "-0.000151434486859903*pi*(-0.183823529411765*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**4*(0.25*cos(1.0*pi*t) + 0.75)*sin(0.833333333333333*pi*X[1])*cos(1.0*pi*X[0])*cos(0.833333333333333*pi*X[1])",

    "DARCY_VELOCITY1_MAGNITUDE_2D" : "(8.25566537178801e-9*(-1.0*pi*(0.25*cos(1.0*pi*t) + 0.75)*sin(1.0*pi*X[0])*sin(0.833333333333333*pi*X[1])**2 - 1.284)**2*(-0.183823529411765*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**8 + 2.29324038105222e-8*pi**2*(-0.183823529411765*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**8*(0.25*cos(1.0*pi*t) + 0.75)**2*sin(0.833333333333333*pi*X[1])**2*cos(1.0*pi*X[0])**2*cos(0.833333333333333*pi*X[1])**2)**(1/2.)",

    "SOURCE_SATURATION1_2D" : "-6.68093324381927e-5*X[1]**2*(-2.5*X[1] + 3.0)*(-1.0*pi*(0.25*cos(1.0*pi*t) + 0.75)*sin(1.0*pi*X[0])*sin(0.833333333333333*pi*X[1])**2 - 1.284)*(-0.183823529411765*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**3*exp(-1.0*X[0])/(1.0*t + 1.) + 0.0625*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.)**2 - 0.000151434486859903*pi*(1.83823529411765*X[1]**2*exp(-1.0*X[0])/(1.0*t + 1.) - 1.47058823529412*X[1]*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.))*(-0.183823529411765*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**3*(0.25*cos(1.0*pi*t) + 0.75)*sin(0.833333333333333*pi*X[1])*cos(1.0*pi*X[0])*cos(0.833333333333333*pi*X[1]) + 0.000217056097832528*pi**2*(-0.183823529411765*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**4*(0.25*cos(1.0*pi*t) + 0.75)*sin(0.833333333333333*pi*X[1])**2*cos(1.0*pi*X[0]) - 0.000126195405716586*pi**2*(-0.183823529411765*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**4*(0.25*cos(1.0*pi*t) + 0.75)*cos(1.0*pi*X[0])*cos(0.833333333333333*pi*X[1])**2",

    "DARCY_VELOCITY2_X_2D" : "-5.29623614227401e-8*X[1]**4*(-2.5*X[1] + 3.0)**2*(-1.0*pi*(0.25*cos(1.0*pi*t) + 0.75)*sin(1.0*pi*X[0])*sin(0.833333333333333*pi*X[1])**2 - 1000.0)*(-(-0.183823529411765*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)*exp(-2.0*X[0])/(1.0*t + 1.)**2",

    "DARCY_VELOCITY2_Y_2D" : "-8.82706023712334e-8*pi*X[1]**4*(-2.5*X[1] + 3.0)**2*(-(-0.183823529411765*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)*(0.25*cos(1.0*pi*t) + 0.75)*exp(-2.0*X[0])*sin(0.833333333333333*pi*X[1])*cos(1.0*pi*X[0])*cos(0.833333333333333*pi*X[1])/(1.0*t + 1.)**2",

    "DARCY_VELOCITY2_MAGNITUDE_2D" : "(2.80501172747294e-15*X[1]**8*(-2.5*X[1] + 3.0)**4*(-1.0*pi*(0.25*cos(1.0*pi*t) + 0.75)*sin(1.0*pi*X[0])*sin(0.833333333333333*pi*X[1])**2 - 1000.0)**2*(-(-0.183823529411765*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)**2*exp(-4.0*X[0])/(1.0*t + 1.)**4 + 7.7916992429804e-15*pi**2*X[1]**8*(-2.5*X[1] + 3.0)**4*(-(-0.183823529411765*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)**2*(0.25*cos(1.0*pi*t) + 0.75)**2*exp(-4.0*X[0])*sin(0.833333333333333*pi*X[1])**2*cos(1.0*pi*X[0])**2*cos(0.833333333333333*pi*X[1])**2/(1.0*t + 1.)**4)**(1/2.)",

    "SOURCE_SATURATION2_2D" : "1.94714564054191e-8*X[1]**6*(-2.5*X[1] + 3.0)**3*(-1.0*pi*(0.25*cos(1.0*pi*t) + 0.75)*sin(1.0*pi*X[0])*sin(0.833333333333333*pi*X[1])**2 - 1000.0)*(-0.183823529411765*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)*exp(-2.0*X[0])*exp(-1.0*X[0])/(1.0*t + 1.)**3 + 8.82706023712334e-8*pi*X[1]**4*(-2.5*X[1] + 3.0)**2*(0.919117647058824*X[1]**2*exp(-1.0*X[0])/(1.0*t + 1.) - 0.735294117647059*X[1]*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.))*(-0.183823529411765*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)*(0.25*cos(1.0*pi*t) + 0.75)*exp(-2.0*X[0])*sin(0.833333333333333*pi*X[1])*cos(1.0*pi*X[0])*cos(0.833333333333333*pi*X[1])/(1.0*t + 1.)**2 + 1.0592472284548e-7*X[1]**4*(-2.5*X[1] + 3.0)**2*(-1.0*pi*(0.25*cos(1.0*pi*t) + 0.75)*sin(1.0*pi*X[0])*sin(0.833333333333333*pi*X[1])**2 - 1000.0)*(-(-0.183823529411765*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)*exp(-2.0*X[0])/(1.0*t + 1.)**2 + 1.26521196732101e-7*pi**2*X[1]**4*(-2.5*X[1] + 3.0)**2*(-(-0.183823529411765*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)*(0.25*cos(1.0*pi*t) + 0.75)*exp(-2.0*X[0])*sin(0.833333333333333*pi*X[1])**2*cos(1.0*pi*X[0])/(1.0*t + 1.)**2 - 7.35588353093612e-8*pi**2*X[1]**4*(-2.5*X[1] + 3.0)**2*(-(-0.183823529411765*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)*(0.25*cos(1.0*pi*t) + 0.75)*exp(-2.0*X[0])*cos(1.0*pi*X[0])*cos(0.833333333333333*pi*X[1])**2/(1.0*t + 1.)**2 - 8.82706023712334e-8*pi*X[1]**4*(12.5*X[1] - 15.0)*(-(-0.183823529411765*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)*(0.25*cos(1.0*pi*t) + 0.75)*exp(-2.0*X[0])*sin(0.833333333333333*pi*X[1])*cos(1.0*pi*X[0])*cos(0.833333333333333*pi*X[1])/(1.0*t + 1.)**2 - 3.53082409484934e-7*pi*X[1]**3*(-2.5*X[1] + 3.0)**2*(-(-0.183823529411765*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)*(0.25*cos(1.0*pi*t) + 0.75)*exp(-2.0*X[0])*sin(0.833333333333333*pi*X[1])*cos(1.0*pi*X[0])*cos(0.833333333333333*pi*X[1])/(1.0*t + 1.)**2 - 0.0625*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.)**2",

    "GRAVITY_DIRECTION_3D" : "1 0. 0. ",

    "PRESSURE_3D" : "(0.25*cos(1.0*pi*t) + 0.75)*sin(0.833333333333333*pi*X[1])**2*sin(1.25*pi*X[2])**2*cos(1.0*pi*X[0])",

    "SATURATION1_3D" : "-0.54931640625*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.",

    "SATURATION2_3D" : "0.54931640625*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.)",

    "DARCY_VELOCITY1_X_3D" : "-9.0860692115942e-5*(-1.0*pi*(0.25*cos(1.0*pi*t) + 0.75)*sin(1.0*pi*X[0])*sin(0.833333333333333*pi*X[1])**2*sin(1.25*pi*X[2])**2 - 1.284)*(-0.646254595588235*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**4",

    "DARCY_VELOCITY1_Y_3D" : "-0.000151434486859903*pi*(-0.646254595588235*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**4*(0.25*cos(1.0*pi*t) + 0.75)*sin(0.833333333333333*pi*X[1])*sin(1.25*pi*X[2])**2*cos(1.0*pi*X[0])*cos(0.833333333333333*pi*X[1])",

    "DARCY_VELOCITY1_Z_3D" : "-0.000227151730289855*pi*(-0.646254595588235*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**4*(0.25*cos(1.0*pi*t) + 0.75)*sin(0.833333333333333*pi*X[1])**2*sin(1.25*pi*X[2])*cos(1.0*pi*X[0])*cos(1.25*pi*X[2])",

    "DARCY_VELOCITY1_MAGNITUDE_3D" : "(8.25566537178801e-9*(-1.0*pi*(0.25*cos(1.0*pi*t) + 0.75)*sin(1.0*pi*X[0])*sin(0.833333333333333*pi*X[1])**2*sin(1.25*pi*X[2])**2 - 1.284)**2*(-0.646254595588235*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**8 + 5.15979085736751e-8*pi**2*(-0.646254595588235*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**8*(0.25*cos(1.0*pi*t) + 0.75)**2*sin(0.833333333333333*pi*X[1])**4*sin(1.25*pi*X[2])**2*cos(1.0*pi*X[0])**2*cos(1.25*pi*X[2])**2 + 2.29324038105222e-8*pi**2*(-0.646254595588235*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**8*(0.25*cos(1.0*pi*t) + 0.75)**2*sin(0.833333333333333*pi*X[1])**2*sin(1.25*pi*X[2])**4*cos(1.0*pi*X[0])**2*cos(0.833333333333333*pi*X[1])**2)**(1/2.)",

    "SOURCE_SATURATION1_3D" : "-0.000234876559353021*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*(-1.0*pi*(0.25*cos(1.0*pi*t) + 0.75)*sin(1.0*pi*X[0])*sin(0.833333333333333*pi*X[1])**2*sin(1.25*pi*X[2])**2 - 1.284)*(-0.646254595588235*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**3*exp(-1.0*X[0])/(1.0*t + 1.) + 0.2197265625*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.)**2 - 0.000227151730289855*pi*(9.69381893382353*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) - 5.17003676470588*X[1]**2*X[2]*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.))*(-0.646254595588235*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**3*(0.25*cos(1.0*pi*t) + 0.75)*sin(0.833333333333333*pi*X[1])**2*sin(1.25*pi*X[2])*cos(1.0*pi*X[0])*cos(1.25*pi*X[2]) - 0.000151434486859903*pi*(6.46254595588235*X[1]**2*X[2]**2*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) - 5.17003676470588*X[1]*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.))*(-0.646254595588235*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**3*(0.25*cos(1.0*pi*t) + 0.75)*sin(0.833333333333333*pi*X[1])*sin(1.25*pi*X[2])**2*cos(1.0*pi*X[0])*cos(0.833333333333333*pi*X[1]) + 0.000500995760694847*pi**2*(-0.646254595588235*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**4*(0.25*cos(1.0*pi*t) + 0.75)*sin(0.833333333333333*pi*X[1])**2*sin(1.25*pi*X[2])**2*cos(1.0*pi*X[0]) - 0.000283939662862319*pi**2*(-0.646254595588235*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**4*(0.25*cos(1.0*pi*t) + 0.75)*sin(0.833333333333333*pi*X[1])**2*cos(1.0*pi*X[0])*cos(1.25*pi*X[2])**2 - 0.000126195405716586*pi**2*(-0.646254595588235*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**4*(0.25*cos(1.0*pi*t) + 0.75)*sin(1.25*pi*X[2])**2*cos(1.0*pi*X[0])*cos(0.833333333333333*pi*X[1])**2",

    "DARCY_VELOCITY2_X_3D" : "-6.54594615973197e-7*X[1]**4*X[2]**4*(-2.5*X[1] + 3.0)**2*(-3.75*X[2] + 3.0)**2*(-1.0*pi*(0.25*cos(1.0*pi*t) + 0.75)*sin(1.0*pi*X[0])*sin(0.833333333333333*pi*X[1])**2*sin(1.25*pi*X[2])**2 - 1000.0)*(-(-0.646254595588235*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)*exp(-2.0*X[0])/(1.0*t + 1.)**2",

    "DARCY_VELOCITY2_Y_3D" : "-1.090991026622e-6*pi*X[1]**4*X[2]**4*(-2.5*X[1] + 3.0)**2*(-3.75*X[2] + 3.0)**2*(-(-0.646254595588235*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)*(0.25*cos(1.0*pi*t) + 0.75)*exp(-2.0*X[0])*sin(0.833333333333333*pi*X[1])*sin(1.25*pi*X[2])**2*cos(1.0*pi*X[0])*cos(0.833333333333333*pi*X[1])/(1.0*t + 1.)**2",

    "DARCY_VELOCITY2_Z_3D" : "-1.63648653993299e-6*pi*X[1]**4*X[2]**4*(-2.5*X[1] + 3.0)**2*(-3.75*X[2] + 3.0)**2*(-(-0.646254595588235*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)*(0.25*cos(1.0*pi*t) + 0.75)*exp(-2.0*X[0])*sin(0.833333333333333*pi*X[1])**2*sin(1.25*pi*X[2])*cos(1.0*pi*X[0])*cos(1.25*pi*X[2])/(1.0*t + 1.)**2",

    "DARCY_VELOCITY2_MAGNITUDE_3D" : "(4.28494111261097e-13*X[1]**8*X[2]**8*(-2.5*X[1] + 3.0)**4*(-3.75*X[2] + 3.0)**4*(-1.0*pi*(0.25*cos(1.0*pi*t) + 0.75)*sin(1.0*pi*X[0])*sin(0.833333333333333*pi*X[1])**2*sin(1.25*pi*X[2])**2 - 1000.0)**2*(-(-0.646254595588235*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)**2*exp(-4.0*X[0])/(1.0*t + 1.)**4 + 2.67808819538186e-12*pi**2*X[1]**8*X[2]**8*(-2.5*X[1] + 3.0)**4*(-3.75*X[2] + 3.0)**4*(-(-0.646254595588235*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)**2*(0.25*cos(1.0*pi*t) + 0.75)**2*exp(-4.0*X[0])*sin(0.833333333333333*pi*X[1])**4*sin(1.25*pi*X[2])**2*cos(1.0*pi*X[0])**2*cos(1.25*pi*X[2])**2/(1.0*t + 1.)**4 + 1.19026142016971e-12*pi**2*X[1]**8*X[2]**8*(-2.5*X[1] + 3.0)**4*(-3.75*X[2] + 3.0)**4*(-(-0.646254595588235*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)**2*(0.25*cos(1.0*pi*t) + 0.75)**2*exp(-4.0*X[0])*sin(0.833333333333333*pi*X[1])**2*sin(1.25*pi*X[2])**4*cos(1.0*pi*X[0])**2*cos(0.833333333333333*pi*X[1])**2/(1.0*t + 1.)**4)**(1/2.)",

    "SOURCE_SATURATION2_3D" : "8.46069557639989e-7*X[1]**6*X[2]**6*(-2.5*X[1] + 3.0)**3*(-3.75*X[2] + 3.0)**3*(-1.0*pi*(0.25*cos(1.0*pi*t) + 0.75)*sin(1.0*pi*X[0])*sin(0.833333333333333*pi*X[1])**2*sin(1.25*pi*X[2])**2 - 1000.0)*(-0.646254595588235*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)*exp(-2.0*X[0])*exp(-1.0*X[0])/(1.0*t + 1.)**3 + 1.30918923194639e-6*X[1]**4*X[2]**4*(-2.5*X[1] + 3.0)**2*(-3.75*X[2] + 3.0)**2*(-1.0*pi*(0.25*cos(1.0*pi*t) + 0.75)*sin(1.0*pi*X[0])*sin(0.833333333333333*pi*X[1])**2*sin(1.25*pi*X[2])**2 - 1000.0)*(-(-0.646254595588235*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)*exp(-2.0*X[0])/(1.0*t + 1.)**2 + 1.63648653993299e-6*pi*X[1]**4*X[2]**4*(-2.5*X[1] + 3.0)**2*(-3.75*X[2] + 3.0)**2*(4.84690946691176*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) - 2.58501838235294*X[1]**2*X[2]*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.))*(-0.646254595588235*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)*(0.25*cos(1.0*pi*t) + 0.75)*exp(-2.0*X[0])*sin(0.833333333333333*pi*X[1])**2*sin(1.25*pi*X[2])*cos(1.0*pi*X[0])*cos(1.25*pi*X[2])/(1.0*t + 1.)**2 + 1.090991026622e-6*pi*X[1]**4*X[2]**4*(-2.5*X[1] + 3.0)**2*(-3.75*X[2] + 3.0)**2*(3.23127297794118*X[1]**2*X[2]**2*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) - 2.58501838235294*X[1]*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.))*(-0.646254595588235*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)*(0.25*cos(1.0*pi*t) + 0.75)*exp(-2.0*X[0])*sin(0.833333333333333*pi*X[1])*sin(1.25*pi*X[2])**2*cos(1.0*pi*X[0])*cos(0.833333333333333*pi*X[1])/(1.0*t + 1.)**2 + 3.6093619797411e-6*pi**2*X[1]**4*X[2]**4*(-2.5*X[1] + 3.0)**2*(-3.75*X[2] + 3.0)**2*(-(-0.646254595588235*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)*(0.25*cos(1.0*pi*t) + 0.75)*exp(-2.0*X[0])*sin(0.833333333333333*pi*X[1])**2*sin(1.25*pi*X[2])**2*cos(1.0*pi*X[0])/(1.0*t + 1.)**2 - 2.04560817491624e-6*pi**2*X[1]**4*X[2]**4*(-2.5*X[1] + 3.0)**2*(-3.75*X[2] + 3.0)**2*(-(-0.646254595588235*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)*(0.25*cos(1.0*pi*t) + 0.75)*exp(-2.0*X[0])*sin(0.833333333333333*pi*X[1])**2*cos(1.0*pi*X[0])*cos(1.25*pi*X[2])**2/(1.0*t + 1.)**2 - 9.09159188851663e-7*pi**2*X[1]**4*X[2]**4*(-2.5*X[1] + 3.0)**2*(-3.75*X[2] + 3.0)**2*(-(-0.646254595588235*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)*(0.25*cos(1.0*pi*t) + 0.75)*exp(-2.0*X[0])*sin(1.25*pi*X[2])**2*cos(1.0*pi*X[0])*cos(0.833333333333333*pi*X[1])**2/(1.0*t + 1.)**2 - 1.63648653993299e-6*pi*X[1]**4*X[2]**4*(-2.5*X[1] + 3.0)**2*(28.125*X[2] - 22.5)*(-(-0.646254595588235*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)*(0.25*cos(1.0*pi*t) + 0.75)*exp(-2.0*X[0])*sin(0.833333333333333*pi*X[1])**2*sin(1.25*pi*X[2])*cos(1.0*pi*X[0])*cos(1.25*pi*X[2])/(1.0*t + 1.)**2 - 1.090991026622e-6*pi*X[1]**4*X[2]**4*(12.5*X[1] - 15.0)*(-3.75*X[2] + 3.0)**2*(-(-0.646254595588235*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)*(0.25*cos(1.0*pi*t) + 0.75)*exp(-2.0*X[0])*sin(0.833333333333333*pi*X[1])*sin(1.25*pi*X[2])**2*cos(1.0*pi*X[0])*cos(0.833333333333333*pi*X[1])/(1.0*t + 1.)**2 - 6.54594615973197e-6*pi*X[1]**4*X[2]**3*(-2.5*X[1] + 3.0)**2*(-3.75*X[2] + 3.0)**2*(-(-0.646254595588235*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)*(0.25*cos(1.0*pi*t) + 0.75)*exp(-2.0*X[0])*sin(0.833333333333333*pi*X[1])**2*sin(1.25*pi*X[2])*cos(1.0*pi*X[0])*cos(1.25*pi*X[2])/(1.0*t + 1.)**2 - 4.36396410648798e-6*pi*X[1]**3*X[2]**4*(-2.5*X[1] + 3.0)**2*(-3.75*X[2] + 3.0)**2*(-(-0.646254595588235*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)*(0.25*cos(1.0*pi*t) + 0.75)*exp(-2.0*X[0])*sin(0.833333333333333*pi*X[1])*sin(1.25*pi*X[2])**2*cos(1.0*pi*X[0])*cos(0.833333333333333*pi*X[1])/(1.0*t + 1.)**2 - 0.2197265625*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.)**2",

    }