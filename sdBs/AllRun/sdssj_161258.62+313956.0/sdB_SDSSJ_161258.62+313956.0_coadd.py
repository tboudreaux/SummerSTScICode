from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[243.24425,31.665556],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_161258.62+313956.0/sdB_SDSSJ_161258.62+313956.0_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_161258.62+313956.0/sdB_SDSSJ_161258.62+313956.0_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
