from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[343.992667,33.719583],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_FBS_2253+335/sdB_FBS_2253+335_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_FBS_2253+335/sdB_FBS_2253+335_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()