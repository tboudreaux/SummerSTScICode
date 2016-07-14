from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[+42¡3250,286.91875],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_Kepler_BD/sdB_Kepler_BD_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_Kepler_BD/sdB_Kepler_BD_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
