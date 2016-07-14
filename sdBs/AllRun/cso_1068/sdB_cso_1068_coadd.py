from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[222.091292,31.519358],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_cso_1068/sdB_cso_1068_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_cso_1068/sdB_cso_1068_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
