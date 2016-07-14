from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[62.792208,0.813361],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J04111-0048/sdB_GALEX_J04111-0048_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J04111-0048/sdB_GALEX_J04111-0048_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
