from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[344.183542,37.598306],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_FBS_2254+373/sdB_FBS_2254+373_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_FBS_2254+373/sdB_FBS_2254+373_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
