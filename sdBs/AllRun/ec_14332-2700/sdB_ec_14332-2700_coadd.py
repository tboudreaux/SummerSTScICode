from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[219.030542,-27.220639],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_ec_14332-2700/sdB_ec_14332-2700_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_ec_14332-2700/sdB_ec_14332-2700_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
