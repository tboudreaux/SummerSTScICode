from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[300.717875,-51.872461],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J20028-5152/sdB_GALEX_J20028-5152_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J20028-5152/sdB_GALEX_J20028-5152_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
