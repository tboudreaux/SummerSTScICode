from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[349.119,28.122017],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kuv_23140+2751/sdB_kuv_23140+2751_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kuv_23140+2751/sdB_kuv_23140+2751_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
