from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[280.676667,44.068056],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kepler_j18427+4404/sdB_kepler_j18427+4404_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kepler_j18427+4404/sdB_kepler_j18427+4404_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
