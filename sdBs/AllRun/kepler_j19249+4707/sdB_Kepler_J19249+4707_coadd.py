from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[291.2425,47.131667],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_Kepler_J19249+4707/sdB_Kepler_J19249+4707_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_Kepler_J19249+4707/sdB_Kepler_J19249+4707_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
