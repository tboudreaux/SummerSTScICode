from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[295.392917,49.120556],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kepler_j19415+4907/sdB_kepler_j19415+4907_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kepler_j19415+4907/sdB_kepler_j19415+4907_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
