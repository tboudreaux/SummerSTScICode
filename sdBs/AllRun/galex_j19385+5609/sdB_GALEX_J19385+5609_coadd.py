from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[294.635667,56.162314],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J19385+5609/sdB_GALEX_J19385+5609_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J19385+5609/sdB_GALEX_J19385+5609_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
