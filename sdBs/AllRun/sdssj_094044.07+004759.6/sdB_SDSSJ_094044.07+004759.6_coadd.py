from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[145.183625,0.799889],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_094044.07+004759.6/sdB_SDSSJ_094044.07+004759.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_094044.07+004759.6/sdB_SDSSJ_094044.07+004759.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
