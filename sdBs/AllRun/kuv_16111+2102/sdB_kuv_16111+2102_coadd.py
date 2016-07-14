from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[243.31075,20.911092],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kuv_16111+2102/sdB_kuv_16111+2102_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kuv_16111+2102/sdB_kuv_16111+2102_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
