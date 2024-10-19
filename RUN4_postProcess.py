import numpy as np


def sortArray(data):
  data[1,-1]=0
  return data[1,:]

import matplotlib.pyplot as plt


import pdb

data_coarse=np.loadtxt("./coarse/surface.csv",unpack=True,delimiter=",",skiprows=20)
#data_medium=np.loadtxt("./medium_nominal/surface.csv",unpack=True,delimiter=",",skiprows=1)
data_fine=np.loadtxt("./fineMesh/surface.csv",unpack=True,delimiter=",",skiprows=22)
#data_vfine=np.loadtxt("./superDupperMesh/surface.csv",unpack=True,delimiter=",",skiprows=22)
data_sefine=np.loadtxt("./superFineMesh/surface.csv",unpack=True,delimiter=",",skiprows=22)

myX_coarse=sortArray(data_coarse)
#myX_medium=sortArray(data_medium)
myX_fine=sortArray(data_fine)
myX_sefine=sortArray(data_sefine)

#pdb.set_trace()

run4_hf=np.loadtxt("../../../RUN4_influenceLE/refdata/run4_heatFlux.csv",unpack=True,delimiter=",",skiprows=1)
run4_p=np.loadtxt("../../../RUN4_influenceLE/refdata/run4_pressure.csv",unpack=True,delimiter=",",skiprows=1)
resultFile='../results/'
resultFile='../results2D/'
ix=1
ipressure=9
iheatflux=18
itemp=12
psiToPa=6894.7573
butTokWm=11356.538527 
InchesToMeters=0.0254

plt.scatter(run4_p[0,:]*InchesToMeters,run4_p[1,:]*psiToPa)
plt.plot(data_coarse[ix,:-2],data_coarse[ipressure,:-2],label="coarse")
#plt.plot(data_medium[ix,myX_medium],data_medium[ipressure,myX_medium],label="medium")
plt.plot(data_fine[ix,:-2],data_fine[ipressure,:-2],label="medium")
plt.plot(data_sefine[ix,:-2],data_sefine[ipressure,:-2],label="fine")
plt.legend()
plt.xlim([2.5,2.85])
plt.xlabel('x (m)')
plt.ylabel('Wall static pressure (kPa)')
plt.tight_layout()
plt.savefig(resultFile+'RUN4_SU2_gridConvergence_pressure.pdf')



plt.figure()
plt.scatter(run4_hf[0,:]*InchesToMeters,run4_hf[1,:]*butTokWm)
plt.plot(data_coarse[ix,:-10],data_coarse[iheatflux,:-10],label="coarse")
#plt.plot(data_medium[ix,myX_medium],data_medium[iheatflux,myX_medium],label="medium")
plt.plot(data_fine[ix,:-2],data_fine[iheatflux,:-2],label="medium")
#plt.plot(data_vfine[ix,:-2],data_vfine[iheatflux,:-2],label="fine (1E-6)")
plt.plot(data_sefine[ix,:-10],data_sefine[iheatflux,:-10],label="fine")
plt.legend()
plt.xlabel('x (m)')
plt.ylabel('Heat flux (W/m^2)')
plt.xlim([2.5,2.85])
plt.tight_layout()
plt.savefig(resultFile+'RUN4_SU2_gridConvergence_heatflux.pdf')

plt.figure()
plt.scatter(run4_hf[0,:]*InchesToMeters,run4_hf[1,:]*butTokWm)
plt.plot(data_coarse[ix,:-10],data_coarse[iheatflux,:-10],label="coarse")
#plt.plot(data_medium[ix,myX_medium],data_medium[iheatflux,myX_medium],label="medium")
plt.plot(data_fine[ix,:-2],data_fine[iheatflux,:-2],label="fine (5E-6)")
#plt.plot(data_vfine[ix,:-2],data_vfine[iheatflux,:-2],label="fine (1E-6)")
plt.plot(data_sefine[ix,:-10],data_sefine[iheatflux,:-10],label="fine (5E-7)")
plt.legend()
plt.xlabel('x (m)')
plt.ylabel('Heat flux (W/m^2)')
plt.ylim([0,400000])
plt.xlim([0.,2.0])
plt.tight_layout()

plt.show()
resultFile='../results2D/'
np.savetxt(resultFile+'run4_wallP_meshXX-SST.dat', list(zip(data_sefine[ix,:-10],data_sefine[ipressure,:-10])) )

np.savetxt(resultFile+'run4_wallHeatFlux_meshXX-SST.dat', list(zip(data_sefine[ix,:-10],data_sefine[iheatflux,:-10])) )

np.savetxt(resultFile+'run4_wallP_mesh01-SST.dat', list(zip(data_coarse[ix,:-2],data_coarse[ipressure,:-2])) )
np.savetxt(resultFile+'run4_wallHeatFlux_mesh01-SST.dat', list(zip(data_coarse[ix,:-2],data_coarse[iheatflux,:-2])) )


np.savetxt(resultFile+'run4_wallP_mesh03-SST.dat', list(zip(data_fine[ix,:-2],data_fine[ipressure,:-2])) )
np.savetxt(resultFile+'run4_wallHeatFlux_mesh03-SST.dat', list(zip(data_fine[ix,:-2],data_fine[iheatflux,:-2])) )

np.savetxt(resultFile+'run4_wallP_mesh05-SST.dat', list(zip(data_sefine[ix,:-10],data_sefine[ipressure,:-10])) )
np.savetxt(resultFile+'run4_wallHeatFlux_mesh05-SST.dat', list(zip(data_sefine[ix,:-10],data_sefine[iheatflux,:-10])) )


plt.show()


