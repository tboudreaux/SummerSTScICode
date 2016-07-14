from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[38.360958,30.686653],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_KUV_02305+3028/sdB_KUV_02305+3028_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_KUV_02305+3028/sdB_KUV_02305+3028_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
