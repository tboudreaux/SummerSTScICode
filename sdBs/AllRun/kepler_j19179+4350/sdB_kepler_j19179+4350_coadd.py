from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[289.494583,43.839167],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kepler_j19179+4350/sdB_kepler_j19179+4350_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kepler_j19179+4350/sdB_kepler_j19179+4350_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
