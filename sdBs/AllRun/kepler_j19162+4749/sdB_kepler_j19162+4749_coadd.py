from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[289.050833,47.821111],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kepler_j19162+4749/sdB_kepler_j19162+4749_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kepler_j19162+4749/sdB_kepler_j19162+4749_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
