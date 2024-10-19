// Gmsh project created on Fri Mar 24 18:54:49 2023
SetFactory("OpenCASCADE");
 
meshQual=3;
MYCASE = 1;
bluntness=2;  //Base line is  2

If(MYCASE==1)
  angle1=6;
  angle2=42;
  X1 = 2.6422604;
  X2 = 0.2100072;
  angTot=180-(angle2-angle1);
  Upstream= -5;
  Downstream=5;
ElseIf(MYCASE==2)
  angle1=7;
  angle2=40;
  X1 = 2.353056;
  X2 = 0.15130;
  angTot=180-(angle2-angle1);
  Upstream= -5;
  Downstream=5;
EndIf
 
corner= X1*Tan(angle1 * Pi / 180);
totLength=X1+X2;

//firstPt=0.005    #NOMINAL: 0.025 investigate 0.001, 0.005, 0.0125, 0.03 0.035
 
If(bluntness==1)
  firstPt=0.001 ;
ElseIf(bluntness==2)
  firstPt=0.005 ;
ElseIf(bluntness==3)
  firstPt=0.0125 ;
ElseIf(bluntness==4)
  firstPt=0.03 ;
EndIf

firstPtY=firstPt*Tan(angle1 * Pi / 180);
 
 
FirstGridPoint= 1E-6;
 
offset= firstPtY*Sin(angle1 * Pi / 180);
radiusTip= (offset^2+firstPtY^2)^0.5;
 
center=firstPt+offset;
Point(1) = {firstPt+offset-radiusTip,0, 0};
Point(2) = {firstPt, firstPtY , 0};
Point(3) = {center,0, 0};
Point(4) = {X1, corner, 0};
Point(5) = {totLength, X2*Tan(angle2 * 3.1416 / 180)+corner , 0};
 
radiusLeading= 2;
 
Point(6) = {center-radiusLeading, 0 ,0};
Point(7) = {center, radiusLeading ,0};
Point(8) = {X1, radiusLeading, 0};
Point(9) = {totLength, radiusLeading, 0};
 
//a=l*(r-1)/(r^n - 1)
//
// n= 100
// r= 1.15
 
If(meshQual==1)
  l = 2;
  n=150;
  r= 1.05;
  Tip=10;
  nx1=1000;
  nx2=100;

ElseIf(meshQual==3)
  l = 2;
  n=200;
  r= 1.05;
  Tip=12;
  nx1=2000;
  nx2=250;
ElseIf(meshQual==5)
  l = 2;
  n=300;
  r= 1.05;
  Tip=15;
  nx1=4000;
  nx2=500;
ElseIf(meshQual==6)
  l = 2;
  n=500;
  r= 1.025;
  Tip=15;
  nx1=6000;
  nx2=750;
EndIf
 
//+
Circle(1) = {1, 3, 2};
 
//+
Circle(2) = {6, 3, 7};
//+
Line(3) = {1, 6};
//+
Line(4) = {2, 7};
//+
Line(5) = {7, 8};
//+
Line(6) = {8, 9};
//+
Line(7) = {9, 5};
//+
Line(8) = {5, 4};
//+
Line(9) = {4, 2};
//+
Line(10) = {4, 8};
 
 
 
//+
Curve Loop(1) = {2, -4, -1, 3};
//+
Curve Loop(2) = {2, -4, -1, 3};
//+
Plane Surface(1) = {2};
//+
Curve Loop(3) = {5, -10, 9, 4};
//+
Plane Surface(2) = {3};
//+
Curve Loop(4) = {6, 7, 8, 10};
//+
Plane Surface(3) = {4};
 
 
 
Transfinite Curve {3,4,10,-7} = n Using Progression r;
Transfinite Curve {1,2} = Tip Using Progression 1;
Transfinite Curve {9,5} = nx1 Using Progression 1;
Transfinite Curve {8,6} = nx2 Using Progression 1;
 
Transfinite Surface "*";
Recombine Surface "*";
//+
Physical Curve("Inlet", 11) = {2, 5, 6};
//+
Physical Curve("outlet", 12) = {7};
//+
Physical Curve("wall", 13) = {1, 9, 8};
//+
Physical Curve("leadingEdge", 14) = {3};
//+
Recursive Delete {
  Point{3};
}