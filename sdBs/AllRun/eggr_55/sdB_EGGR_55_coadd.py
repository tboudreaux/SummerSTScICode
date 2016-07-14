from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[117.885542,-38.476469],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_EGGR_55/sdB_EGGR_55_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_EGGR_55/sdB_EGGR_55_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
