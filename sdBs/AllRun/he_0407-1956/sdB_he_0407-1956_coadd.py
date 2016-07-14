from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[62.546417,-19.814889],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_he_0407-1956/sdB_he_0407-1956_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_he_0407-1956/sdB_he_0407-1956_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
