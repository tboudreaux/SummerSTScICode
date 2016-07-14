from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[176.792333,-32.358717],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_EC_11446-3204/sdB_EC_11446-3204_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_EC_11446-3204/sdB_EC_11446-3204_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
