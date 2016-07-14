from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[137.717792,7.826278],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_091052.27+074934.6/sdB_SDSSJ910_091052.27+074934.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_091052.27+074934.6/sdB_SDSSJ910_091052.27+074934.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
