from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[254.101375,58.802417],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sbss_1655+588/sdB_sbss_1655+588_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sbss_1655+588/sdB_sbss_1655+588_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
