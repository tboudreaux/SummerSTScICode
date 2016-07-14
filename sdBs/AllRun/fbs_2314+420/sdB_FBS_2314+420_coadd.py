from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[349.15275,42.357972],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_FBS_2314+420/sdB_FBS_2314+420_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_FBS_2314+420/sdB_FBS_2314+420_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
