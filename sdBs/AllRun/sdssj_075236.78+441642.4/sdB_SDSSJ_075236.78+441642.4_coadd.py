from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[118.15325,44.278444],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_075236.78+441642.4/sdB_SDSSJ_075236.78+441642.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_075236.78+441642.4/sdB_SDSSJ_075236.78+441642.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
