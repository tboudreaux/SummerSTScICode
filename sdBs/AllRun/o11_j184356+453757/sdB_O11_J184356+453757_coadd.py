from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[280.983333,45.6325],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_O11_J184356+453757/sdB_O11_J184356+453757_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_O11_J184356+453757/sdB_O11_J184356+453757_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
