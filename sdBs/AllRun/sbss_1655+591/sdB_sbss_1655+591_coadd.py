from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[254.127958,59.079469],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sbss_1655+591/sdB_sbss_1655+591_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sbss_1655+591/sdB_sbss_1655+591_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
