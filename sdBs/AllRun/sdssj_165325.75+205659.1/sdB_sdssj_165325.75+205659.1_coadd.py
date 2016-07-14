from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[253.357292,20.94975],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_165325.75+205659.1/sdB_sdssj_165325.75+205659.1_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_165325.75+205659.1/sdB_sdssj_165325.75+205659.1_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()