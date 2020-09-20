class Crystalcalculate():
    def __init__(self,dire):

        self.dire = dire

    def latticeplane(self,crystalsystem,a,b,c,alpha,beta,gamma,h1,k1,l1,):
        import os
        import pandas as pd
        import numpy as np
        import math
        from decimal import Decimal as D
        from decimal import getcontext
        getcontext().prec = 5



        sys=crystalsystem
        a1=D(str(math.radians(alpha))).quantize(D('0.0000'))
        a2=D(str(math.radians(beta))).quantize(D('0.0000'))
        a3=D(str(math.radians(gamma))).quantize(D('0.0000'))
        sin1=D(str(math.sin(a1))).quantize(D('0.0000'))
        sin2=D(str(math.sin(a2))).quantize(D('0.0000'))
        sin3=D(str(math.sin(a3))).quantize(D('0.0000'))
        cos1=D(str(math.cos(a1))).quantize(D('0.0000'))
        cos21=D(str(math.cos(2*a1))).quantize(D('0.0000'))
        cos2=D(str(math.cos(a2))).quantize(D('0.0000'))
        cos3=D(str(math.cos(a3))).quantize(D('0.0000'))
        a=D(str(a)).quantize(D('0.0000'))
        b=D(str(b)).quantize(D('0.0000'))
        c=D(str(c)).quantize(D('0.0000'))
        parr=[]
        vert=[]

        # if 'cubic' or 'tetragonal' or 'orthorhombic' or 'hexagonal' or 'trigonal' or 'monoclinic' or 'triclinic' not in str(sys):
        #     print ('Crystal system error, plase enter one of cubic tetragonal orthorhombic hexagonal trigonal monoclinic triclinic')
          



        if sys=='cubic':

            for h2 in range(0,10):
                for k2 in range(0,10):
                    for l2 in range(0,10):
                        if h2+k2+l2 != 0:
                            v1=h2*h1+k1*k2+l1*l2
                            v2=h1**2+k1**2+l1**2
                            v3=h2**2+k2**2+l2**2
                            cospsi=v1/(v2*v3)**0.5
                            cospsi=D(str(cospsi)).quantize(D('0.00'))
                            if cospsi==1:
                                notd='('+str(h2)+' '+str(k2)+' '+str(l2)+')'
                                parr.append(notd)
                            if cospsi==0:
                                verd='('+str(h2)+' '+str(k2)+' '+str(l2)+')'
                                vert.append(verd)


        if sys=='tetragonal':

            for h2 in range(0,10):
                for k2 in range(0,10):
                    for l2 in range(0,10):
                        if h2+k2+l2 != 0:
                            v1=(h2*h1+k1*k2)/(a**2)+(l1*l)/(c**2)
                            v2=(h1**2+k1**2)/(a**2)+(l1**2)/(c**2)
                            v3=(h2**2+k2**2)/(a**2)+(l2**2)/(c**2)
                            cospsi=v1/(v2*v3)**0.5
                            cospsi=D(str(cospsi)).quantize(D('0.00'))
                            if cospsi==1:
                                notd='('+str(h2)+' '+str(k2)+' '+str(l2)+')'
                                parr.append(notd)
                            if cospsi==0:
                                verd='('+str(h2)+' '+str(k2)+' '+str(l2)+')'
                                vert.append(verd)



        if sys=='orthorhombic':

            for h2 in range(0,10):
                for k2 in range(0,10):
                    for l2 in range(0,10):
                        if h2+k2+l2 != 0:
                            v1=(h2*h1)/(a**2)+(k1*k2)/(b**2)+(l1*l2)/(c**2)
                            v2=(h1**2)/(a**2)+(k1**2)/(b**2)+(l1**2)/(c**2)
                            v3=(h2**2)/(a**2)+(k2**2)/(b**2)+(l2**2)/(c**2)
                            cospsi=v1/(v2*v3)**0.5
                            cospsi=D(str(cospsi)).quantize(D('0.00'))
                            if cospsi==1:
                                notd='('+str(h2)+' '+str(k2)+' '+str(l2)+')'
                                parr.append(notd)
                            if cospsi==0:
                                verd='('+str(h2)+' '+str(k2)+' '+str(l2)+')'
                                vert.append(verd)




        if sys=='hexagonal':

            for h2 in range(0,10):
                for k2 in range(0,10):
                    for l2 in range(0,10):
                        if h2+k2+l2 != 0:
                            v1=(h2*h1+k1*k2)+(h2*k2+h2*k1)*0.5+((3*(a**2))/(4*(c**2)))*(l1*l2)

                            v2=h1**2+k1**2+h1*k1+((3*(a**2))/(4*(c**2)))*(l1**2)

                            v3=h2**2+k2**2+h2*k2+((3*(a**2))/(4*(c**2)))*(l2**2)
                            cospsi=v1/(v2*v3)**0.5
                            cospsi=D(str(cospsi)).quantize(D('0.00'))
                            if cospsi==1:
                                notd='('+str(h2)+' '+str(k2)+' '+str(l2)+')'
                                parr.append(notd)
                            if cospsi==0:
                                verd='('+str(h2)+' '+str(k2)+' '+str(l2)+')'
                                vert.append(verd)

            



        if sys=='trigonal':

            for h2 in range(0,2):
                for k2 in range(0,2):
                    for l2 in range(0,2):
                        if h2+k2+l2 != 0:
                            print(h2,k2,l2)
                            # vo=a*b*c*(1-((cos1)**2)-((cos2)**2)-(cos3**2+2*cos1*cos2*cos3))**D(str(0.5))
                            vo=a**3*(1-3*cos21+2*cos1**3)

                            print(vo)
                            d1=((a**2*(1-3*cos1**2+2*cos1**3))/((h1**2+k1**2+l1**2)*sin1+2*(k1*l1+l1*h1+h1*k1)*(cos1**2-cos1)))**D(str(0.5))
                            d2=((a**2*(1-3*cos1**2+2*cos1**3))/((h2**2+k2**2+l2**2)*sin1+2*(k2*l2+l2*h2+h2*k2)*(cos1**2-cos1)))**D(str(0.5))
                            print (d2)
                            v1=a**4*d1*d2/322**2

                            v2=(sin1**2)*(h1*h2+k1*k2+l1*l2)

                            v3=(cos1**2-cos1)*(k1*l2+k2*l1+l1*h2+l2*h1+h1*k2+h2*k1)
                            cospsi=v1*(v2+v3)
                            cospsi=D(str(cospsi)).quantize(D('0.00'))
                            print(cospsi)
                            if cospsi==1:
                                notd='('+str(h2)+' '+str(k2)+' '+str(l2)+')'
                                parr.append(notd)
                            if cospsi==0:
                                verd='('+str(h2)+' '+str(k2)+' '+str(l2)+')'
                                vert.append(verd)




        if sys=='monoclinic':

            for h2 in range(0,10):
                for k2 in range(0,10):
                    for l2 in range(0,10):
                        if h2+k2+l2 != 0:
                            print(h2,k2,l2)

                            vo=a*b*c*(1-((cos1)**2)-((cos2)**2)-(cos3**2+2*cos1*cos2*cos3))**D(str(0.5))
                            print (vo)

                            d1=((a**2(1-3*cos1**2+2*cos1**3))/((h1**2+k1**2+l1**2)*sin1+2(k1*l1+l1*h1+h1*k1)*(cos1**2-cos1)))**D(str(0.5))
                            d2=((a**2(1-3*cos1**2+2*cos1**3))/((h2**2+k2**2+l2**2)*sin1+2(k2*l2+l2*h2+h2*k2)*(cos1**2-cos1)))**D(str(0.5))

                            v1=(d1*d2)/math.sin(a2)**2

                            v2=h1*h2/a**2+k1*k2*math.sin(a2)**2/b**2+l1*l2/c**2

                            v3=((l1*h2+l2*h1)*cos2)/(a*c)
                            cospsi=v1*(v2-v3)
                            cospsi=D(str(cospsi)).quantize(D('0.00'))
                            if cospsi==1:
                                notd='('+str(h2)+' '+str(k2)+' '+str(l2)+')'
                                parr.append(notd)
                            if cospsi==0:
                                verd='('+str(h2)+' '+str(k2)+' '+str(l2)+')'
                                vert.append(verd)





        if sys=='triclinic':

            for h2 in range(0,10):
                for k2 in range(0,10):
                    for l2 in range(0,10):
                        if h2+k2+l2 != 0:
                            s11=b**2*c**2*(sin1**2)
                            s22=a**2*c**2*(sin2**2)
                            s33=a**2*b**2*sin3**2
                            s12=a*b*c**2*(cos1*cos2-cos3)
                            s23=a**2*b*c*(cos2*cos3-cos1)
                            s13=a*b**2*c*(cos3*cos1-cos2)
                            


                            vo=a*b*c*(1-(cos1**2-cos2**2-cos3**2+2*cos1*cos2*cos3))**D(str(0.5))
                            # print(vo)

                            d1=(vo**2/(s11*h1**2+s22*k1**2+s33*l1**2+2*s12*h1*k1+2*s23*k1*l1+2*s13*l1*h1))**D(str(0.5))
                            # print(s33)


                            d2=(vo**2/(s11*h2**2+s22*k2**2+s33*l2**2+2*s12*h2*k2+2*s23*k2*l2+2*s13*l2*h2))**D(str(0.5))
                            
                            v1=d1*d2/vo**D(str(2))
                            # print(v1)
                            v2=s11*h1*h2+s22*k1*k2+s33*l1*l2
                            # print(sin3,s33)
                            v3=s23*(k1*l2+k2*l1)+s13*(l1*h2+l2*h1)+s12*(h1*k2+h2*k1)
                            cospsi=v1*(v2+v3)
                            cospsi=D(str(cospsi)).quantize(D('0.00'))
                            if cospsi==1:
                                notd='('+str(h2)+' '+str(k2)+' '+str(l2)+')'
                                parr.append(notd)
                            if cospsi==0:
                                verd='('+str(h2)+' '+str(k2)+' '+str(l2)+')'
                                vert.append(verd)

                                
        result1=' '.join(parr)
        result2=' '.join(vert)
        print('Parallel crystal plane:'+str(result1))
        print ('Vertical crystal plane:'+str(result2))

