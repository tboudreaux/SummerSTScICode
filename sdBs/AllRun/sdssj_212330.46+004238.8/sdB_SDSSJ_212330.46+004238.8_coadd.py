from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[320.876917,0.710778],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_212330.46+004238.8/sdB_SDSSJ_212330.46+004238.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_212330.46+004238.8/sdB_SDSSJ_212330.46+004238.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
