from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[133.593292,1.614139],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_085422.39+013650.9/sdB_SDSSJ_085422.39+013650.9_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_085422.39+013650.9/sdB_SDSSJ_085422.39+013650.9_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
