from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[157.5705,49.755692],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sbss_1027+500/sdB_sbss_1027+500_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sbss_1027+500/sdB_sbss_1027+500_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
