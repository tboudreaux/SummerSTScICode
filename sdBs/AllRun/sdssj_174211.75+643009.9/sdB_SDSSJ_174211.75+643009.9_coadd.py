from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[265.548958,64.50275],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_174211.75+643009.9/sdB_SDSSJ_174211.75+643009.9_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_174211.75+643009.9/sdB_SDSSJ_174211.75+643009.9_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
