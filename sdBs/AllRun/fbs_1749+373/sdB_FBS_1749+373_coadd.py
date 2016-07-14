from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[267.905667,37.33075],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_FBS_1749+373/sdB_FBS_1749+373_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_FBS_1749+373/sdB_FBS_1749+373_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
