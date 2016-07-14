from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[223.553292,21.537778],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_145412.79+213216.0/sdB_SDSSJ_145412.79+213216.0_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_145412.79+213216.0/sdB_SDSSJ_145412.79+213216.0_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
