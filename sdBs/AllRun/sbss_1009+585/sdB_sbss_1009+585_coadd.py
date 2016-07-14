from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[153.341125,58.328469],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sbss_1009+585/sdB_sbss_1009+585_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sbss_1009+585/sdB_sbss_1009+585_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
