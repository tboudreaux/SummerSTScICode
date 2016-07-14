from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[192.321417,56.537719],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sbss_1247+568/sdB_sbss_1247+568_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sbss_1247+568/sdB_sbss_1247+568_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
