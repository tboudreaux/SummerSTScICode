from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[27.015292,-5.929197],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_Feige_14/sdB_Feige_14_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_Feige_14/sdB_Feige_14_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
