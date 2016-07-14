from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[281.931667,46.273889],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kepler_j18477+4616/sdB_kepler_j18477+4616_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kepler_j18477+4616/sdB_kepler_j18477+4616_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
