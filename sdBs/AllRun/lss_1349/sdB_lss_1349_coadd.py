from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[146.737792,-50.204542],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_lss_1349/sdB_lss_1349_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_lss_1349/sdB_lss_1349_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
