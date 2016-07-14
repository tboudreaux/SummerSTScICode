from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[340.685917,-4.237556],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_EGGR_229/sdB_EGGR_229_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_EGGR_229/sdB_EGGR_229_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
