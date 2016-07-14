from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[19.791667,26.588806],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_011910.00+263519.7/sdB_SDSSJ_011910.00+263519.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_011910.00+263519.7/sdB_SDSSJ_011910.00+263519.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
