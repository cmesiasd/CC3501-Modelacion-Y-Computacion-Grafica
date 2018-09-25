module esferas(radio){
    color([0/255,80/255,92/255]) 
    union(){
        translate([radio*cos(0), radio*sin(0), 0]) sphere(r = radio/5);
        translate([radio*cos(60), radio*sin(60), 0]) sphere(r = radio/5);
        translate([radio*cos(120), radio*sin(120), 0]) sphere(r = radio/5);
        translate([radio*cos(180), radio*sin(180), 0]) sphere(r = radio/5);
        translate([radio*cos(240), radio*sin(240), 0]) sphere(r = radio/5);
        translate([radio*cos(300), radio*sin(300), 0]) sphere(r = radio/5);
    }
}

module cilindros(radio){
    altura = radio/10;
    union(){
        translate([0,0,6])color("black") difference(){
             circle(r=radio*0.505);
             circle(r=radio*0.5);
            }
        color([0/255,80/255,92/255]) cylinder(r =(radio*0.5), h = altura+1        ,center =true);
        color([0/255,80/255,92/255]) difference(){
            cylinder(r =(radio*0.75)-0.1, h = altura+0.5,center =true);
            cylinder(r =(radio*0.5), h = altura+5,center =true);
        }
        color([17/255,158/255,181/255]) difference(){
            cylinder(r =radio, h = altura,center =true);
            cylinder(r =radio*0.75, h = altura+10,center =true);
        }
        
    }
}


module nariz(radio){
     translate([0,0,5]) color([17/255,158/255,181/255]) difference(){
        sphere(radio/2);
        translate([-radio/2,-radio/2,-radio])cube(radio);
        }
}

module ojos(radio){
    color([17/255,158/255,181/255])union(){
        translate([radio*0.5*cos(40),radio*0.5*sin(40),6])circle(r = radio*0.1);
        translate([radio*0.5*cos(145),radio*0.5*sin(145),6])circle(r = radio*0.1);
        translate([radio*0.5*cos(215),radio*0.5*sin(215),6])circle(r = radio*0.1);
        translate([radio*0.5*cos(325),radio*0.5*sin(325),6])circle(r = radio*0.1);
                }
    union(){
        translate([0,radio*0.5,6])scale([1,.6]) circle(radio/5);
        color("black") translate([0,radio*0.5,7])scale([1.2,.6]) circle(radio/11);
        mirror([0,1,0]) translate([0,radio*0.5,6]) scale([1,.6]) circle(radio/5);
        mirror([0,1,0])color("black") translate([0,radio*0.5,7])scale([1.2,.6]) circle(radio/11);
    }
}
module bronzor(radio, $fn = 100){
    esferas(radio);
    cilindros(radio);
    nariz(radio/3);
    ojos(radio);
    
}

rotate([0,90,0])bronzor(100);