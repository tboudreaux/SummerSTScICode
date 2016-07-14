from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[272.450958,-26.697083],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_OGLE_BUL-SC16335/sdB_OGLE_BUL-SC16335_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_OGLE_BUL-SC16335/sdB_OGLE_BUL-SC16335_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
