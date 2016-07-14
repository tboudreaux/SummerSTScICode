from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[293.66625,47.97],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_Kepler_J19346+4758/sdB_Kepler_J19346+4758_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_Kepler_J19346+4758/sdB_Kepler_J19346+4758_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
