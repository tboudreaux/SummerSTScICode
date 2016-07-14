from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[188.399208,49.174528],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SBSS_1231+494/sdB_SBSS_1231+494_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SBSS_1231+494/sdB_SBSS_1231+494_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
