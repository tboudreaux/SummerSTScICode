from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[132.8345,32.887342],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kuv_08482+3304/sdB_kuv_08482+3304_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kuv_08482+3304/sdB_kuv_08482+3304_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
