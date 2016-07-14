from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[334.841625,0.867139],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_221921.99-005201.7/sdB_sdssj_221921.99-005201.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_221921.99-005201.7/sdB_sdssj_221921.99-005201.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
