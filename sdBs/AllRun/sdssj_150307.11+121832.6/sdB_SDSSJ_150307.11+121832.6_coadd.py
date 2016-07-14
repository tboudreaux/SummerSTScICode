from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[225.779625,12.309056],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_150307.11+121832.6/sdB_SDSSJ_150307.11+121832.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_150307.11+121832.6/sdB_SDSSJ_150307.11+121832.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
