from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[279.08675,40.994028],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSS_J183620.82+405938.5/sdB_SDSS_J183620.82+405938.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSS_J183620.82+405938.5/sdB_SDSS_J183620.82+405938.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
