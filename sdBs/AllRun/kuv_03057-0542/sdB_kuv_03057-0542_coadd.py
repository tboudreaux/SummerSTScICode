from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[47.046542,-5.515353],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kuv_03057-0542/sdB_kuv_03057-0542_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kuv_03057-0542/sdB_kuv_03057-0542_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
