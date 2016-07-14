from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[328.82125,-10.417278],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PHL_211/sdB_PHL_211_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PHL_211/sdB_PHL_211_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
