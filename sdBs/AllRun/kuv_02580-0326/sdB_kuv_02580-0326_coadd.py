from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[45.125875,-3.235933],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kuv_02580-0326/sdB_kuv_02580-0326_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kuv_02580-0326/sdB_kuv_02580-0326_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
