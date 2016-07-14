from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[300.475,49.065],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_O11_J200154+490354/sdB_O11_J200154+490354_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_O11_J200154+490354/sdB_O11_J200154+490354_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()